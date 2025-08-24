#!/bin/bash

# Script de restauración para Odoo 14
# Restaura backup completo de PostgreSQL, filestore y configuraciones

set -e

# Configuración
BACKUP_DIR="/home/carvajal/Desarrollo/odoo14-prod/backups"
COMPOSE_FILE="/home/carvajal/Desarrollo/odoo14-prod/docker-compose.yml"
TEMP_DIR="/tmp/odoo_restore_$(date +%s)"

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
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

log_question() {
    echo -e "${BLUE}[?]${NC} $1"
}

# Función de ayuda
show_help() {
    echo "Uso: $0 <archivo_backup.tar.gz> [opciones]"
    echo ""
    echo "Opciones:"
    echo "  --db-only       Restaurar solo la base de datos"
    echo "  --files-only    Restaurar solo los archivos"
    echo "  --config-only   Restaurar solo las configuraciones"
    echo "  --force         No pedir confirmación"
    echo "  --help          Mostrar esta ayuda"
    echo ""
    echo "Ejemplo:"
    echo "  $0 odoo_full_backup_20241201_143000.tar.gz"
    echo "  $0 odoo_full_backup_20241201_143000.tar.gz --db-only"
}

# Verificar argumentos
if [ $# -eq 0 ] || [ "$1" = "--help" ]; then
    show_help
    exit 0
fi

BACKUP_FILE="$1"
DB_ONLY=false
FILES_ONLY=false
CONFIG_ONLY=false
FORCE=false

# Procesar argumentos adicionales
shift
while [[ $# -gt 0 ]]; do
    case $1 in
        --db-only)
            DB_ONLY=true
            shift
            ;;
        --files-only)
            FILES_ONLY=true
            shift
            ;;
        --config-only)
            CONFIG_ONLY=true
            shift
            ;;
        --force)
            FORCE=true
            shift
            ;;
        *)
            log_error "Opción desconocida: $1"
            show_help
            exit 1
            ;;
    esac
done

# Verificar que el archivo de backup existe
if [[ ! "$BACKUP_FILE" = /* ]]; then
    BACKUP_FILE="$BACKUP_DIR/$BACKUP_FILE"
fi

if [ ! -f "$BACKUP_FILE" ]; then
    log_error "Archivo de backup no encontrado: $BACKUP_FILE"
    echo ""
    log_info "Backups disponibles:"
    ls -la "$BACKUP_DIR"/*.tar.gz 2>/dev/null || log_warn "No hay backups disponibles"
    exit 1
fi

log_info "Iniciando restauración desde: $(basename $BACKUP_FILE)"

# Confirmación
if [ "$FORCE" = false ]; then
    log_warn "⚠️  ADVERTENCIA: Esta operación sobrescribirá los datos actuales."
    log_question "¿Estás seguro de continuar? (s/N): "
    read -r confirmation
    if [[ ! "$confirmation" =~ ^[Ss]$ ]]; then
        log_info "Restauración cancelada."
        exit 0
    fi
fi

# Crear directorio temporal
mkdir -p "$TEMP_DIR"
log_info "Directorio temporal: $TEMP_DIR"

# Extraer backup
log_info "Extrayendo backup..."
if ! tar -xzf "$BACKUP_FILE" -C "$TEMP_DIR"; then
    log_error "Error extrayendo el backup"
    rm -rf "$TEMP_DIR"
    exit 1
fi

# Verificar contenido del backup
DB_BACKUP=$(find "$TEMP_DIR" -name "db_backup_*.sql.gz" | head -1)
FILESTORE_BACKUP=$(find "$TEMP_DIR" -name "filestore_backup_*.tar.gz" | head -1)
CONFIG_BACKUP=$(find "$TEMP_DIR" -name "config_backup_*.tar.gz" | head -1)

log_info "Contenido del backup encontrado:"
[ -n "$DB_BACKUP" ] && log_info "  ✅ Base de datos: $(basename $DB_BACKUP)"
[ -n "$FILESTORE_BACKUP" ] && log_info "  ✅ Filestore: $(basename $FILESTORE_BACKUP)"
[ -n "$CONFIG_BACKUP" ] && log_info "  ✅ Configuraciones: $(basename $CONFIG_BACKUP)"

# Detener servicios
log_info "Deteniendo servicios..."
docker-compose -f "$COMPOSE_FILE" down

# Restaurar base de datos
if [ "$FILES_ONLY" = false ] && [ "$CONFIG_ONLY" = false ] && [ -n "$DB_BACKUP" ]; then
    log_info "Restaurando base de datos..."
    
    # Iniciar solo PostgreSQL
    docker-compose -f "$COMPOSE_FILE" up -d db
    sleep 10
    
    # Eliminar base de datos existente y crear nueva
    docker-compose -f "$COMPOSE_FILE" exec -T db psql -U odoo -c "DROP DATABASE IF EXISTS odoo;"
    docker-compose -f "$COMPOSE_FILE" exec -T db psql -U odoo -c "CREATE DATABASE odoo;"
    
    # Restaurar datos
    if gunzip -c "$DB_BACKUP" | docker-compose -f "$COMPOSE_FILE" exec -T db psql -U odoo -d odoo; then
        log_info "✅ Base de datos restaurada correctamente"
    else
        log_error "❌ Error restaurando la base de datos"
        docker-compose -f "$COMPOSE_FILE" down
        rm -rf "$TEMP_DIR"
        exit 1
    fi
    
    docker-compose -f "$COMPOSE_FILE" down
fi

# Restaurar filestore
if [ "$DB_ONLY" = false ] && [ "$CONFIG_ONLY" = false ] && [ -n "$FILESTORE_BACKUP" ]; then
    log_info "Restaurando filestore..."
    
    # Eliminar volumen existente y crear nuevo
    docker volume rm odoo14-prod_odoo_data 2>/dev/null || true
    docker volume create odoo14-prod_odoo_data
    
    # Restaurar datos del filestore
    if docker run --rm -v odoo14-prod_odoo_data:/data -v "$TEMP_DIR":/backup alpine tar -xzf "/backup/$(basename $FILESTORE_BACKUP)" -C /data; then
        log_info "✅ Filestore restaurado correctamente"
    else
        log_warn "⚠️  Error restaurando filestore (puede ser normal si no había datos)"
    fi
fi

# Restaurar configuraciones
if [ "$DB_ONLY" = false ] && [ "$FILES_ONLY" = false ] && [ -n "$CONFIG_BACKUP" ]; then
    log_info "Restaurando configuraciones..."
    
    # Hacer backup de configuraciones actuales
    CURRENT_CONFIG_BACKUP="/tmp/current_config_$(date +%s).tar.gz"
    cd "$(dirname "$COMPOSE_FILE")"
    tar -czf "$CURRENT_CONFIG_BACKUP" config/ addons/ *.yml *.conf Caddyfile environment.env 2>/dev/null || true
    log_info "Configuraciones actuales respaldadas en: $CURRENT_CONFIG_BACKUP"
    
    # Restaurar configuraciones
    if tar -xzf "$CONFIG_BACKUP" -C "$(dirname "$COMPOSE_FILE")"; then
        log_info "✅ Configuraciones restauradas correctamente"
    else
        log_error "❌ Error restaurando configuraciones"
        rm -rf "$TEMP_DIR"
        exit 1
    fi
fi

# Iniciar servicios
log_info "Iniciando servicios..."
if docker-compose -f "$COMPOSE_FILE" up -d --build; then
    log_info "✅ Servicios iniciados correctamente"
else
    log_error "❌ Error iniciando servicios"
    rm -rf "$TEMP_DIR"
    exit 1
fi

# Limpiar archivos temporales
rm -rf "$TEMP_DIR"

# Verificar que los servicios están funcionando
log_info "Verificando servicios..."
sleep 15

if docker-compose -f "$COMPOSE_FILE" ps | grep -q "Up"; then
    log_info "✅ Servicios verificados correctamente"
    log_info ""
    log_info "🎉 Restauración completada exitosamente!"
    log_info ""
    log_info "Servicios disponibles:"
    log_info "  - Odoo: https://multiacceso.labcit.com"
    log_info "  - Desarrollo: http://localhost"
    log_info ""
    log_info "Verifica los logs con: docker-compose logs -f"
else
    log_error "❌ Algunos servicios no están funcionando correctamente"
    log_info "Verifica los logs con: docker-compose logs"
    exit 1
fi
