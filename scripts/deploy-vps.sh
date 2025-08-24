#!/bin/bash

# Script de despliegue para VPS - multiacceso.labcit.com
# Ejecutar en el VPS después de clonar el repositorio

set -e

# Configuración
VPS_IP="34.123.185.85"
DOMAIN="multiacceso.labcit.com"
PROJECT_DIR="/opt/odoo14-prod"

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

echo "🚀 Desplegando Odoo 14 en VPS - multiacceso.labcit.com"
echo "======================================================="

# Verificar que estamos en el VPS correcto
log_step "1. Verificando entorno..."
CURRENT_IP=$(curl -s ifconfig.me)
if [ "$CURRENT_IP" != "$VPS_IP" ]; then
    log_warn "⚠️  IP actual ($CURRENT_IP) no coincide con VPS esperado ($VPS_IP)"
    read -p "¿Continuar de todas formas? (s/N): " continue_deploy
    if [[ ! "$continue_deploy" =~ ^[Ss]$ ]]; then
        log_error "Despliegue cancelado"
        exit 1
    fi
fi

# Verificar Docker
log_step "2. Verificando Docker..."
if ! command -v docker &> /dev/null; then
    log_error "Docker no está instalado. Ejecuta primero: ./install-ubuntu.sh"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    log_error "Docker Compose no está instalado. Ejecuta primero: ./install-ubuntu.sh"
    exit 1
fi

log_info "✅ Docker y Docker Compose disponibles"

# Verificar DNS
log_step "3. Verificando DNS..."
DNS_IP=$(nslookup $DOMAIN | grep "Address:" | tail -1 | cut -d' ' -f2)
if [ "$DNS_IP" != "$VPS_IP" ]; then
    log_warn "⚠️  DNS de $DOMAIN apunta a $DNS_IP, pero VPS es $VPS_IP"
    log_warn "El SSL automático puede fallar si el DNS no está configurado correctamente"
fi

# Crear directorio del proyecto si no existe
log_step "4. Configurando directorio del proyecto..."
if [ ! -d "$PROJECT_DIR" ]; then
    sudo mkdir -p "$PROJECT_DIR"
    sudo chown -R $USER:$USER "$PROJECT_DIR"
    log_info "✅ Directorio $PROJECT_DIR creado"
fi

# Si estamos ejecutando desde otro directorio, copiar archivos
if [ "$(pwd)" != "$PROJECT_DIR" ]; then
    log_info "Copiando archivos a $PROJECT_DIR..."
    sudo cp -r . "$PROJECT_DIR/"
    sudo chown -R $USER:$USER "$PROJECT_DIR"
    cd "$PROJECT_DIR"
    log_info "✅ Archivos copiados a $PROJECT_DIR"
fi

# Configurar variables de entorno
log_step "5. Configurando variables de entorno..."
if [ ! -f ".env" ]; then
    cp environment.env .env
    log_info "✅ Archivo .env creado desde environment.env"
else
    log_info "✅ Archivo .env ya existe"
fi

# Configurar permisos
log_step "6. Configurando permisos..."
sudo chown -R 101:101 addons/ logs/ backups/ 2>/dev/null || true
chmod +x scripts/*.sh
log_info "✅ Permisos configurados"

# Configurar firewall
log_step "7. Configurando firewall..."
sudo ufw --force enable
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
log_info "✅ Firewall configurado (puertos 22, 80, 443)"

# Detener servicios existentes si están corriendo
log_step "8. Preparando servicios..."
if docker-compose ps | grep -q "Up"; then
    log_info "Deteniendo servicios existentes..."
    docker-compose down
fi

# Construir e iniciar servicios
log_step "9. Construyendo e iniciando servicios..."
log_info "Esto puede tomar varios minutos..."

if docker-compose up -d --build; then
    log_info "✅ Servicios iniciados correctamente"
else
    log_error "❌ Error iniciando servicios"
    exit 1
fi

# Esperar que los servicios estén listos
log_step "10. Esperando que los servicios estén listos..."
sleep 30

# Verificar servicios
log_info "Estado de servicios:"
docker-compose ps

# Verificar conectividad
log_step "11. Verificando conectividad..."
if curl -s -o /dev/null -w "%{http_code}" http://localhost:8014 | grep -q "200\|303"; then
    log_info "✅ Odoo responde correctamente en puerto 8014"
else
    log_warn "⚠️  Odoo no responde en puerto 8014. Verificando logs..."
    docker-compose logs --tail=10 odoo
fi

# Verificar Caddy
sleep 10
if curl -s -o /dev/null http://localhost; then
    log_info "✅ Caddy proxy funcionando"
else
    log_warn "⚠️  Problemas con Caddy proxy"
fi

# Configurar backups automáticos
log_step "12. Configurando backups automáticos..."
if [ -x "./scripts/backup-scheduler.sh" ]; then
    ./scripts/backup-scheduler.sh install
    log_info "✅ Backups automáticos configurados"
else
    log_warn "⚠️  Script de backup no encontrado"
fi

# Mostrar información final
echo ""
echo "🎉 ¡Despliegue completado exitosamente!"
echo "======================================"
log_info "🌐 URLs de acceso:"
log_info "   Producción: https://$DOMAIN"
log_info "   Gestión BD: https://$DOMAIN/web/database/manager"
log_info "   Desarrollo: http://localhost:8014 (solo desde VPS)"

echo ""
log_info "🔐 Credenciales importantes:"
log_info "   Admin Odoo: MultiAcceso2024!AdminVPS#Secure"
log_info "   PostgreSQL: MultiAcceso2024!SecureDB#VPS"

echo ""
log_info "📝 Comandos útiles:"
echo "   Ver logs:        docker-compose logs -f odoo"
echo "   Estado:          docker-compose ps"
echo "   Reiniciar:       docker-compose restart odoo"
echo "   Backup:          ./scripts/backup.sh"
echo "   Detener:         docker-compose down"

echo ""
log_info "📊 Próximos pasos:"
echo "   1. Accede a https://$DOMAIN"
echo "   2. Crea/restaura tu base de datos"
echo "   3. Configura tu empresa"
echo "   4. ¡Comienza a usar Odoo!"

echo ""
log_warn "⚠️  IMPORTANTE:"
echo "   - Guarda las credenciales en lugar seguro"
echo "   - Configura backups externos (S3, etc.)"
echo "   - Monitorea los logs regularmente"
