#!/bin/bash

# Script de backup completo para Odoo 14
# Realiza backup de PostgreSQL, filestore y configuraciones

set -e

# Configuración
BACKUP_DIR="/home/carvajal/Desarrollo/odoo14-prod/backups"
DATE=$(date +%Y%m%d_%H%M%S)
COMPOSE_FILE="/home/carvajal/Desarrollo/odoo14-prod/docker-compose.yml"
RETENTION_DAYS=30

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar que Docker Compose está funcionando
if ! docker-compose -f "$COMPOSE_FILE" ps | grep -q "Up"; then
    log_error "Los contenedores no están ejecutándose. Inicia con: docker-compose up -d"
    exit 1
fi

# Crear directorio de backup si no existe
mkdir -p "$BACKUP_DIR"

log_info "Iniciando backup completo - $DATE"

# 1. Backup de PostgreSQL
log_info "Realizando backup de PostgreSQL..."
DB_BACKUP="$BACKUP_DIR/db_backup_$DATE.sql"

if docker-compose -f "$COMPOSE_FILE" exec -T db pg_dump -U odoo -h localhost odoo > "$DB_BACKUP"; then
    log_info "✅ Backup de PostgreSQL completado: $(basename $DB_BACKUP)"
    
    # Comprimir backup de DB
    gzip "$DB_BACKUP"
    log_info "✅ Backup comprimido: $(basename $DB_BACKUP).gz"
else
    log_error "❌ Error en backup de PostgreSQL"
    exit 1
fi

# 2. Backup de filestore (datos de archivos de Odoo)
log_info "Realizando backup del filestore..."
FILESTORE_BACKUP="$BACKUP_DIR/filestore_backup_$DATE.tar.gz"

# Crear backup del volumen de datos de Odoo
if docker run --rm -v odoo14-prod_odoo_data:/data -v "$BACKUP_DIR":/backup alpine tar -czf "/backup/$(basename $FILESTORE_BACKUP)" -C /data .; then
    log_info "✅ Backup del filestore completado: $(basename $FILESTORE_BACKUP)"
else
    log_warn "⚠️  Error en backup del filestore (puede ser normal si no hay datos)"
fi

# 3. Backup de configuraciones y módulos personalizados
log_info "Realizando backup de configuraciones..."
CONFIG_BACKUP="$BACKUP_DIR/config_backup_$DATE.tar.gz"

cd "$(dirname "$COMPOSE_FILE")"
if tar -czf "$CONFIG_BACKUP" \
    --exclude='backups' \
    --exclude='logs/*.log' \
    --exclude='.git' \
    --exclude='__pycache__' \
    config/ addons/ *.yml *.conf Caddyfile environment.env 2>/dev/null; then
    log_info "✅ Backup de configuraciones completado: $(basename $CONFIG_BACKUP)"
else
    log_warn "⚠️  Algunos archivos de configuración no pudieron ser respaldados"
fi

# 4. Crear backup completo
log_info "Creando backup completo..."
FULL_BACKUP="$BACKUP_DIR/odoo_full_backup_$DATE.tar.gz"

cd "$BACKUP_DIR"
if tar -czf "$FULL_BACKUP" \
    "db_backup_$DATE.sql.gz" \
    "filestore_backup_$DATE.tar.gz" \
    "config_backup_$DATE.tar.gz" 2>/dev/null; then
    log_info "✅ Backup completo creado: $(basename $FULL_BACKUP)"
    
    # Limpiar archivos individuales
    rm -f "db_backup_$DATE.sql.gz" "filestore_backup_$DATE.tar.gz" "config_backup_$DATE.tar.gz"
    log_info "✅ Archivos individuales limpiados"
else
    log_error "❌ Error creando backup completo"
fi

# 5. Limpiar backups antiguos
log_info "Limpiando backups antiguos (>$RETENTION_DAYS días)..."
find "$BACKUP_DIR" -name "odoo_full_backup_*.tar.gz" -mtime +$RETENTION_DAYS -delete
find "$BACKUP_DIR" -name "db_backup_*.sql.gz" -mtime +$RETENTION_DAYS -delete
find "$BACKUP_DIR" -name "*.tar.gz" -mtime +$RETENTION_DAYS -delete

# 6. Mostrar información del backup
BACKUP_SIZE=$(du -h "$FULL_BACKUP" | cut -f1)
log_info "📊 Información del backup:"
log_info "   Archivo: $(basename $FULL_BACKUP)"
log_info "   Tamaño: $BACKUP_SIZE"
log_info "   Ubicación: $BACKUP_DIR"

# 7. Verificar integridad del backup
log_info "Verificando integridad del backup..."
if tar -tzf "$FULL_BACKUP" >/dev/null 2>&1; then
    log_info "✅ Backup verificado correctamente"
else
    log_error "❌ Error en la verificación del backup"
    exit 1
fi

log_info "🎉 Backup completado exitosamente!"
echo ""
log_info "Para restaurar este backup, usa:"
log_info "   ./scripts/restore.sh $(basename $FULL_BACKUP)"
