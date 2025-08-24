#!/bin/bash

# Script de backup rápido solo de base de datos PostgreSQL
# Útil para backups frecuentes durante desarrollo

set -e

# Configuración
BACKUP_DIR="/home/carvajal/Desarrollo/odoo14-prod/backups"
DATE=$(date +%Y%m%d_%H%M%S)
COMPOSE_FILE="/home/carvajal/Desarrollo/odoo14-prod/docker-compose.yml"

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar que Docker Compose está funcionando
if ! docker-compose -f "$COMPOSE_FILE" ps | grep -q "db.*Up"; then
    log_error "El contenedor de PostgreSQL no está ejecutándose"
    exit 1
fi

# Crear directorio de backup si no existe
mkdir -p "$BACKUP_DIR"

log_info "Iniciando backup de base de datos - $DATE"

# Backup de PostgreSQL con información adicional
DB_BACKUP="$BACKUP_DIR/db_quick_backup_$DATE.sql"

# Obtener información de la base de datos
log_info "Obteniendo información de la base de datos..."
DB_SIZE=$(docker-compose -f "$COMPOSE_FILE" exec -T db psql -U odoo -d odoo -t -c "SELECT pg_size_pretty(pg_database_size('odoo'));" | tr -d ' \n')
TABLE_COUNT=$(docker-compose -f "$COMPOSE_FILE" exec -T db psql -U odoo -d odoo -t -c "SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public';" | tr -d ' \n')

log_info "Base de datos: odoo"
log_info "Tamaño: $DB_SIZE"
log_info "Tablas: $TABLE_COUNT"

# Realizar backup
if docker-compose -f "$COMPOSE_FILE" exec -T db pg_dump -U odoo -h localhost \
    --verbose \
    --format=plain \
    --no-owner \
    --no-privileges \
    odoo > "$DB_BACKUP" 2>/dev/null; then
    
    log_info "✅ Backup de PostgreSQL completado: $(basename $DB_BACKUP)"
    
    # Comprimir backup
    gzip "$DB_BACKUP"
    COMPRESSED_BACKUP="$DB_BACKUP.gz"
    
    # Información del archivo
    BACKUP_SIZE=$(du -h "$COMPRESSED_BACKUP" | cut -f1)
    log_info "✅ Backup comprimido: $(basename $COMPRESSED_BACKUP)"
    log_info "📊 Tamaño del backup: $BACKUP_SIZE"
    
    # Verificar integridad
    if gunzip -t "$COMPRESSED_BACKUP" 2>/dev/null; then
        log_info "✅ Integridad del backup verificada"
    else
        log_error "❌ Error en la verificación del backup"
        exit 1
    fi
    
    log_info "🎉 Backup rápido completado exitosamente!"
    echo ""
    log_info "Para restaurar solo la base de datos:"
    log_info "  gunzip -c $(basename $COMPRESSED_BACKUP) | docker-compose exec -T db psql -U odoo -d odoo"
    
else
    log_error "❌ Error en backup de PostgreSQL"
    exit 1
fi
