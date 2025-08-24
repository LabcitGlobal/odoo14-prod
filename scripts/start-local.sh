#!/bin/bash

# Script para iniciar Odoo 14 en desarrollo local
# Configura el entorno y verifica que todo esté listo

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

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_step() {
    echo -e "${BLUE}[PASO]${NC} $1"
}

PROJECT_DIR="/home/carvajal/Desarrollo/odoo14-prod"
cd "$PROJECT_DIR"

echo "🚀 Iniciando Odoo 14 en modo desarrollo local"
echo "================================================"

# Verificar Docker
log_step "1. Verificando Docker..."
if ! command -v docker &> /dev/null; then
    log_error "Docker no está instalado. Ejecuta: ./install-ubuntu.sh"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    log_error "Docker Compose no está instalado. Ejecuta: ./install-ubuntu.sh"
    exit 1
fi

log_info "✅ Docker y Docker Compose están disponibles"

# Verificar archivo .env
log_step "2. Verificando configuración..."
if [ ! -f ".env" ]; then
    log_warn "Archivo .env no existe. Creando desde environment.env..."
    cp environment.env .env
    log_info "✅ Archivo .env creado"
else
    log_info "✅ Archivo .env existe"
fi

# Verificar puertos
log_step "3. Verificando puertos..."
if netstat -tuln 2>/dev/null | grep -q ":80 "; then
    log_warn "⚠️  Puerto 80 está ocupado. Verifica si hay conflictos."
    log_info "Verifica qué proceso usa el puerto 80: sudo netstat -tulpn | grep :80"
fi

if netstat -tuln 2>/dev/null | grep -q ":8014 "; then
    log_warn "⚠️  Puerto 8014 (Odoo) está ocupado. Puede haber conflictos."
    log_info "Verifica qué proceso usa el puerto 8014: sudo netstat -tulpn | grep :8014"
fi

# Detener servicios existentes si están corriendo
log_step "4. Preparando servicios..."
if docker-compose ps | grep -q "Up"; then
    log_info "Deteniendo servicios existentes..."
    docker-compose down
fi

# Crear directorios necesarios
log_step "5. Preparando directorios..."
mkdir -p logs backups addons

# Configurar permisos
log_info "Configurando permisos..."
sudo chown -R $USER:$USER logs/ backups/ addons/ 2>/dev/null || true

# Construir e iniciar servicios
log_step "6. Construyendo e iniciando servicios..."
log_info "Esto puede tomar varios minutos la primera vez..."

if docker-compose up -d --build; then
    log_info "✅ Servicios iniciados correctamente"
else
    log_error "❌ Error iniciando servicios"
    exit 1
fi

# Esperar que los servicios estén listos
log_step "7. Esperando que los servicios estén listos..."
log_info "Esperando PostgreSQL..."
sleep 10

# Verificar PostgreSQL
for i in {1..30}; do
    if docker-compose exec -T db pg_isready -U odoo >/dev/null 2>&1; then
        log_info "✅ PostgreSQL está listo"
        break
    fi
    if [ $i -eq 30 ]; then
        log_error "❌ PostgreSQL no responde después de 30 intentos"
        docker-compose logs db
        exit 1
    fi
    sleep 2
done

# Verificar Odoo
log_info "Esperando Odoo..."
sleep 15

for i in {1..20}; do
    if curl -s http://localhost >/dev/null 2>&1; then
        log_info "✅ Odoo está respondiendo"
        break
    fi
    if [ $i -eq 20 ]; then
        log_warn "⚠️  Odoo no responde en localhost. Verificando logs..."
        docker-compose logs --tail=20 odoo
    fi
    sleep 3
done

# Mostrar estado de servicios
log_step "8. Estado de servicios:"
docker-compose ps

# Mostrar información de acceso
echo ""
echo "🎉 ¡Odoo 14 está ejecutándose en modo desarrollo!"
echo "================================================"
log_info "🌐 Acceso web: http://localhost"
log_info "📊 Base de datos: PostgreSQL en puerto 5432"
log_info "📁 Módulos personalizados: ./addons/"
log_info "📋 Logs: ./logs/"
log_info "💾 Backups: ./backups/"

echo ""
log_info "📝 Comandos útiles:"
echo "  Ver logs:           docker-compose logs -f odoo"
echo "  Detener servicios:  docker-compose down"
echo "  Reiniciar Odoo:     docker-compose restart odoo"
echo "  Backup rápido:      ./scripts/backup-db-only.sh"
echo "  Acceder a Odoo:     docker-compose exec odoo bash"

echo ""
log_info "🔧 Configuración inicial de Odoo:"
echo "  1. Ve a http://localhost"
echo "  2. Crea una nueva base de datos"
echo "  3. Configura tu empresa"
echo "  4. ¡Comienza a desarrollar!"

echo ""
log_warn "💡 Para migrar a producción más tarde:"
echo "  - Ejecuta: ./scripts/migrate-to-production.sh"
echo "  - Lee: MIGRATION-GUIDE.md"
