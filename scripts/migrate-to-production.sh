#!/bin/bash

# Script para migrar configuración de desarrollo local a producción VPS

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

show_help() {
    echo "Script de migración de desarrollo local a producción VPS"
    echo ""
    echo "Uso: $0 [opción]"
    echo ""
    echo "Opciones:"
    echo "  prepare     Preparar configuración para producción"
    echo "  backup      Crear backup para migración"
    echo "  deploy      Mostrar comandos para desplegar en VPS"
    echo "  revert      Revertir a configuración de desarrollo"
    echo "  help        Mostrar esta ayuda"
}

prepare_production() {
    log_step "Preparando configuración para producción..."
    
    # Backup de configuración actual
    BACKUP_DIR="migration_backup_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    
    log_info "Creando backup de configuración actual..."
    cp Caddyfile "$BACKUP_DIR/"
    cp config/odoo.conf "$BACKUP_DIR/"
    cp environment.env "$BACKUP_DIR/"
    
    # Actualizar Caddyfile para producción
    log_info "Configurando Caddyfile para producción..."
    sed -i 's/^# multiacceso.labcit.com/multiacceso.labcit.com/' Caddyfile
    sed -i 's/^# //' Caddyfile
    sed -i 's/^localhost, 127.0.0.1, :80/# localhost, 127.0.0.1, :80/' Caddyfile
    sed -i '/^# Configuración principal para desarrollo local/,/^}/ s/^/# /' Caddyfile
    
    # Actualizar odoo.conf para producción
    log_info "Configurando odoo.conf para producción..."
    sed -i 's|web.base.url = http://localhost|web.base.url = https://multiacceso.labcit.com|' config/odoo.conf
    sed -i 's|# web.base.url = https://multiacceso.labcit.com|web.base.url = https://multiacceso.labcit.com|' config/odoo.conf
    
    # Actualizar variables de entorno
    log_info "Configurando variables de entorno para producción..."
    sed -i 's|ODOO_BASE_URL=http://localhost|ODOO_BASE_URL=https://multiacceso.labcit.com|' environment.env
    sed -i 's|# ODOO_BASE_URL=https://multiacceso.labcit.com|ODOO_BASE_URL=https://multiacceso.labcit.com|' environment.env
    
    # Configurar workers para producción
    sed -i 's/workers = 0/workers = 4/' config/odoo.conf
    sed -i 's/max_cron_threads = 1/max_cron_threads = 2/' config/odoo.conf
    
    log_info "✅ Configuración preparada para producción"
    log_info "📁 Backup de configuración local guardado en: $BACKUP_DIR"
    
    echo ""
    log_warn "⚠️  IMPORTANTE: Revisa y ajusta las siguientes configuraciones:"
    echo "  1. Cambia las contraseñas en environment.env"
    echo "  2. Ajusta workers según CPU del VPS en config/odoo.conf"
    echo "  3. Configura límites de memoria según RAM del VPS"
    echo ""
    log_info "Archivos modificados:"
    echo "  - Caddyfile (configuración SSL y dominio)"
    echo "  - config/odoo.conf (URL base y workers)"
    echo "  - environment.env (variables de entorno)"
}

create_migration_backup() {
    log_step "Creando backup completo para migración..."
    
    if [ ! -x "./scripts/backup.sh" ]; then
        log_error "Script de backup no encontrado o no ejecutable"
        exit 1
    fi
    
    # Crear backup completo
    ./scripts/backup.sh
    
    LATEST_BACKUP=$(ls -t backups/odoo_full_backup_*.tar.gz | head -1)
    
    if [ -n "$LATEST_BACKUP" ]; then
        log_info "✅ Backup creado: $LATEST_BACKUP"
        
        # Crear paquete de migración
        MIGRATION_PACKAGE="migration_package_$(date +%Y%m%d_%H%M%S).tar.gz"
        
        tar -czf "$MIGRATION_PACKAGE" \
            --exclude='backups/odoo_full_backup_*.tar.gz' \
            --exclude='logs/*.log' \
            --exclude='.git' \
            --exclude='migration_backup_*' \
            . "$LATEST_BACKUP"
        
        log_info "✅ Paquete de migración creado: $MIGRATION_PACKAGE"
        
        echo ""
        log_info "📦 Contenido del paquete de migración:"
        echo "  - Código fuente completo"
        echo "  - Configuraciones de producción"
        echo "  - Backup completo de datos"
        echo "  - Scripts de despliegue"
        
    else
        log_error "No se pudo crear el backup"
        exit 1
    fi
}

show_deploy_commands() {
    log_step "Comandos para desplegar en VPS..."
    
    echo ""
    log_info "🚀 Pasos para desplegar en el VPS:"
    echo ""
    echo "1. 📤 Subir archivos al VPS:"
    echo "   scp migration_package_*.tar.gz user@tu-vps:/home/user/"
    echo ""
    echo "2. 🔧 En el VPS, instalar dependencias:"
    echo "   ./install-ubuntu.sh"
    echo "   sudo reboot"
    echo ""
    echo "3. 📁 Extraer y configurar:"
    echo "   tar -xzf migration_package_*.tar.gz"
    echo "   cd odoo14-prod"
    echo ""
    echo "4. 🔐 Configurar variables de entorno seguras:"
    echo "   cp environment.env .env"
    echo "   nano .env  # Cambiar contraseñas"
    echo ""
    echo "5. 🔒 Configurar permisos:"
    echo "   sudo chown -R 101:101 addons/ logs/"
    echo "   chmod +x scripts/*.sh"
    echo ""
    echo "6. 🚀 Iniciar servicios:"
    echo "   docker-compose up -d --build"
    echo ""
    echo "7. 📊 Verificar despliegue:"
    echo "   docker-compose ps"
    echo "   docker-compose logs -f"
    echo ""
    echo "8. 💾 Restaurar datos (si es necesario):"
    echo "   ./scripts/restore.sh odoo_full_backup_*.tar.gz"
    echo ""
    echo "9. ⚙️  Configurar backups automáticos:"
    echo "   ./scripts/backup-scheduler.sh install"
    echo ""
    
    log_info "🌐 Después del despliegue, Odoo estará disponible en:"
    log_info "   https://multiacceso.labcit.com"
}

revert_to_development() {
    log_step "Revirtiendo a configuración de desarrollo..."
    
    # Buscar backup más reciente
    LATEST_BACKUP=$(ls -t migration_backup_*/Caddyfile 2>/dev/null | head -1)
    
    if [ -n "$LATEST_BACKUP" ]; then
        BACKUP_DIR=$(dirname "$LATEST_BACKUP")
        
        log_info "Restaurando desde: $BACKUP_DIR"
        
        # Restaurar archivos
        cp "$BACKUP_DIR/Caddyfile" .
        cp "$BACKUP_DIR/odoo.conf" config/
        cp "$BACKUP_DIR/environment.env" .
        
        log_info "✅ Configuración de desarrollo restaurada"
        
        # Limpiar backup
        read -p "¿Eliminar backup de migración? (s/N): " clean_backup
        if [[ "$clean_backup" =~ ^[Ss]$ ]]; then
            rm -rf "$BACKUP_DIR"
            log_info "Backup de migración eliminado"
        fi
        
    else
        log_warn "No se encontró backup de configuración de desarrollo"
        log_info "Restaurando configuración manual..."
        
        # Revertir manualmente
        sed -i 's|web.base.url = https://multiacceso.labcit.com|web.base.url = http://localhost|' config/odoo.conf
        sed -i 's|ODOO_BASE_URL=https://multiacceso.labcit.com|ODOO_BASE_URL=http://localhost|' environment.env
        sed -i 's/workers = 4/workers = 0/' config/odoo.conf
        sed -i 's/max_cron_threads = 2/max_cron_threads = 1/' config/odoo.conf
        
        log_info "✅ Configuración básica de desarrollo restaurada"
    fi
    
    echo ""
    log_info "🔄 Para aplicar cambios, reinicia los servicios:"
    echo "  docker-compose down && docker-compose up -d"
}

# Procesar argumentos
case "${1:-help}" in
    prepare)
        prepare_production
        ;;
    backup)
        create_migration_backup
        ;;
    deploy)
        show_deploy_commands
        ;;
    revert)
        revert_to_development
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "Opción desconocida: $1"
        show_help
        exit 1
        ;;
esac
