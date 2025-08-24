#!/bin/bash

# Script para verificar puertos disponibles y conflictos

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
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

log_check() {
    echo -e "${BLUE}[CHECK]${NC} $1"
}

echo "🔍 Verificador de Puertos para Odoo 14"
echo "====================================="

# Puertos que usa nuestra configuración
PORTS=(80 443 5432 8014)
PORT_NAMES=("HTTP (Caddy)" "HTTPS (Caddy)" "PostgreSQL" "Odoo")

log_info "Verificando puertos necesarios para Odoo 14..."
echo ""

conflicts_found=false

for i in "${!PORTS[@]}"; do
    port=${PORTS[$i]}
    name=${PORT_NAMES[$i]}
    
    log_check "Puerto $port ($name):"
    
    if netstat -tuln 2>/dev/null | grep -q ":$port "; then
        log_error "  ❌ Puerto $port está ocupado"
        
        # Mostrar qué proceso lo está usando
        if command -v lsof &> /dev/null; then
            process=$(sudo lsof -i :$port 2>/dev/null | tail -n +2 | head -1)
            if [ -n "$process" ]; then
                echo "     Proceso: $process"
            fi
        fi
        conflicts_found=true
    else
        log_info "  ✅ Puerto $port está disponible"
    fi
done

echo ""

if [ "$conflicts_found" = true ]; then
    log_warn "⚠️  Se encontraron conflictos de puertos"
    echo ""
    log_info "💡 Soluciones:"
    echo "  1. Detener servicios que usan esos puertos"
    echo "  2. Cambiar puertos en la configuración de Odoo"
    echo "  3. Usar docker-compose con puertos diferentes"
    echo ""
    log_info "🔧 Para cambiar el puerto de Odoo (actual: 8014):"
    echo "  - Edita config/odoo.conf → http_port = NUEVO_PUERTO"
    echo "  - Edita Caddyfile → reverse_proxy odoo:NUEVO_PUERTO"
    echo "  - Edita docker-compose.yml → expose NUEVO_PUERTO"
    echo ""
    log_info "🔧 Para usar puertos alternativos:"
    echo "  - Puerto 80 → Cambiar en docker-compose.yml ports: '8080:80'"
    echo "  - Puerto 443 → Cambiar en docker-compose.yml ports: '8443:443'"
else
    log_info "🎉 ¡Todos los puertos están disponibles!"
    echo ""
    log_info "✅ Puedes iniciar Odoo sin problemas:"
    echo "  ./scripts/start-local.sh"
fi

echo ""
log_info "📊 Resumen de configuración actual:"
echo "  - Acceso web: http://localhost (puerto 80)"
echo "  - Odoo interno: puerto 8014"
echo "  - PostgreSQL: puerto 5432 (interno)"
echo "  - HTTPS: puerto 443 (para producción)"

# Verificar Docker
echo ""
log_check "Docker y Docker Compose:"
if command -v docker &> /dev/null; then
    log_info "  ✅ Docker está instalado"
else
    log_error "  ❌ Docker no está instalado"
fi

if command -v docker-compose &> /dev/null; then
    log_info "  ✅ Docker Compose está instalado"
else
    log_error "  ❌ Docker Compose no está instalado"
fi

# Verificar si ya hay contenedores corriendo
echo ""
log_check "Contenedores de Odoo:"
if docker-compose ps 2>/dev/null | grep -q "Up"; then
    log_info "  ✅ Hay contenedores de Odoo ejecutándose"
    docker-compose ps
else
    log_info "  📋 No hay contenedores de Odoo ejecutándose"
fi
