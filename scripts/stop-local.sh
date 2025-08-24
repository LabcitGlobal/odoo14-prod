#!/bin/bash

# Script para detener Odoo 14 en desarrollo local de forma segura

set -e

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_step() {
    echo -e "${BLUE}[PASO]${NC} $1"
}

PROJECT_DIR="/home/carvajal/Desarrollo/odoo14-prod"
cd "$PROJECT_DIR"

echo "🛑 Deteniendo Odoo 14 en desarrollo local"
echo "=========================================="

# Verificar si hay servicios corriendo
log_step "1. Verificando servicios activos..."
if ! docker-compose ps | grep -q "Up"; then
    log_info "No hay servicios activos para detener"
    exit 0
fi

# Mostrar servicios que se van a detener
log_info "Servicios activos:"
docker-compose ps

# Ofrecer backup antes de detener
echo ""
read -p "¿Quieres hacer un backup rápido de la BD antes de detener? (s/N): " backup_choice
if [[ "$backup_choice" =~ ^[Ss]$ ]]; then
    log_step "2. Realizando backup rápido..."
    if [ -x "./scripts/backup-db-only.sh" ]; then
        ./scripts/backup-db-only.sh
        log_info "✅ Backup completado"
    else
        log_warn "Script de backup no encontrado"
    fi
fi

# Detener servicios gradualmente
log_step "3. Deteniendo servicios..."

# Detener Caddy primero (proxy)
log_info "Deteniendo Caddy..."
docker-compose stop caddy

# Detener Odoo
log_info "Deteniendo Odoo..."
docker-compose stop odoo

# Detener PostgreSQL al final
log_info "Deteniendo PostgreSQL..."
docker-compose stop db

# Verificar que todo esté detenido
log_step "4. Verificando servicios..."
if docker-compose ps | grep -q "Up"; then
    log_warn "Algunos servicios aún están activos. Forzando detención..."
    docker-compose down
else
    log_info "✅ Todos los servicios detenidos correctamente"
fi

# Mostrar estado final
echo ""
log_info "📊 Estado final de servicios:"
docker-compose ps

# Información adicional
echo ""
log_info "🎯 Servicios detenidos exitosamente"
echo ""
log_info "📝 Para volver a iniciar:"
echo "  ./scripts/start-local.sh"
echo ""
log_info "📝 Para limpiar completamente (¡CUIDADO!):"
echo "  docker-compose down -v  # Elimina también los volúmenes"
echo ""
log_info "📝 Para ver logs de la última ejecución:"
echo "  docker-compose logs"
