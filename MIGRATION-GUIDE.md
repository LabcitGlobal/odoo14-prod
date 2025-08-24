# 🚀 Guía de Migración: Desarrollo Local → Producción VPS

## 🎯 Resumen

Esta guía te ayuda a migrar tu instalación de Odoo 14 desde desarrollo local hacia el VPS de producción en `multiacceso.labcit.com`.

## 📋 Fases de la Migración

### **Fase 1: Desarrollo Local** 
✅ Configuración actual optimizada para desarrollo
- Acceso: `http://localhost`
- SSL: Deshabilitado
- Workers: 0 (modo development)
- Configuración simplificada

### **Fase 2: Preparación para Producción**
🔄 Ajustar configuraciones para VPS
- Cambiar URLs y dominios
- Configurar SSL automático
- Optimizar para producción

### **Fase 3: Despliegue en VPS**
🚀 Migración completa al servidor
- Subir código y datos
- Configurar entorno de producción
- Activar backups automáticos

## 🛠️ Scripts de Migración

### **Para Desarrollo Local:**
```bash
# Iniciar desarrollo local
./scripts/start-local.sh

# Detener desarrollo local
./scripts/stop-local.sh
```

### **Para Migración:**
```bash
# Preparar configuración para producción
./scripts/migrate-to-production.sh prepare

# Crear paquete de migración completo
./scripts/migrate-to-production.sh backup

# Ver comandos de despliegue
./scripts/migrate-to-production.sh deploy

# Revertir a desarrollo (si es necesario)
./scripts/migrate-to-production.sh revert
```

## 🚀 Proceso Paso a Paso

### **Paso 1: Desarrollo y Pruebas Locales**

1. **Iniciar entorno local:**
   ```bash
   ./scripts/start-local.sh
   ```

2. **Desarrollar y configurar:**
   - Accede a http://localhost
   - Configura tu empresa
   - Instala módulos necesarios
   - Carga datos de prueba
   - Desarrolla módulos personalizados en `addons/`

3. **Hacer backups regulares:**
   ```bash
   ./scripts/backup-db-only.sh  # Backup rápido
   ./scripts/backup.sh          # Backup completo
   ```

### **Paso 2: Preparar para Producción**

1. **Preparar configuración:**
   ```bash
   ./scripts/migrate-to-production.sh prepare
   ```
   
   Esto actualiza automáticamente:
   - ✅ Caddyfile → SSL y dominio de producción
   - ✅ odoo.conf → URL base y workers optimizados
   - ✅ environment.env → Variables de producción

2. **Personalizar configuración:**
   ```bash
   # Editar variables seguras
   nano environment.env
   ```
   
   **Cambiar obligatoriamente:**
   ```env
   POSTGRES_PASSWORD=TU_PASSWORD_SUPER_SEGURO
   ```

3. **Crear paquete de migración:**
   ```bash
   ./scripts/migrate-to-production.sh backup
   ```
   
   Esto crea:
   - 📦 `migration_package_FECHA.tar.gz` (código + configuraciones)
   - 💾 Backup completo de datos

### **Paso 3: Desplegar en VPS**

1. **Subir al VPS:**
   ```bash
   # Desde tu máquina local
   scp migration_package_*.tar.gz user@tu-vps-ip:/home/user/
   ```

2. **En el VPS, preparar sistema:**
   ```bash
   # Instalar Docker y dependencias
   wget https://raw.githubusercontent.com/tu-repo/odoo14-prod/main/install-ubuntu.sh
   chmod +x install-ubuntu.sh
   ./install-ubuntu.sh
   sudo reboot
   ```

3. **Configurar proyecto:**
   ```bash
   # Extraer proyecto
   tar -xzf migration_package_*.tar.gz
   cd odoo14-prod
   
   # Configurar entorno
   cp environment.env .env
   nano .env  # Ajustar contraseñas y configuraciones
   
   # Permisos
   sudo chown -R 101:101 addons/ logs/ backups/
   chmod +x scripts/*.sh
   ```

4. **Verificar DNS:**
   ```bash
   # Verificar que el dominio apunta al VPS
   nslookup multiacceso.labcit.com
   ```

5. **Iniciar servicios:**
   ```bash
   docker-compose up -d --build
   ```

6. **Verificar despliegue:**
   ```bash
   # Ver estado de servicios
   docker-compose ps
   
   # Ver logs
   docker-compose logs -f
   
   # Verificar SSL (puede tardar unos minutos)
   curl -I https://multiacceso.labcit.com
   ```

7. **Configurar backups automáticos:**
   ```bash
   ./scripts/backup-scheduler.sh install
   ./scripts/backup-scheduler.sh status
   ```

## 🔄 Sincronización Continua

### **Desarrollo Local → Producción**

1. **Desarrollar localmente:**
   ```bash
   # Hacer cambios en desarrollo
   ./scripts/backup-db-only.sh  # Backup antes de cambios
   ```

2. **Sincronizar código:**
   ```bash
   # Subir solo cambios de código
   rsync -avz --exclude='backups/' --exclude='logs/' \
         ./addons/ user@vps:/path/to/odoo14-prod/addons/
   ```

3. **Actualizar producción:**
   ```bash
   # En el VPS
   docker-compose restart odoo
   ```

### **Producción → Desarrollo Local**

1. **Descargar datos de producción:**
   ```bash
   # En el VPS, crear backup
   ./scripts/backup.sh
   
   # Descargar backup
   scp user@vps:/path/to/backups/odoo_full_backup_*.tar.gz ./backups/
   ```

2. **Restaurar en local:**
   ```bash
   # Revertir a configuración de desarrollo
   ./scripts/migrate-to-production.sh revert
   
   # Restaurar datos
   ./scripts/restore.sh odoo_full_backup_*.tar.gz
   ```

## ⚠️ Consideraciones Importantes

### **Seguridad**
- ✅ Cambia todas las contraseñas por defecto
- ✅ Configura firewall en el VPS
- ✅ Usa contraseñas fuertes para PostgreSQL
- ✅ Configura backups externos (S3, etc.)

### **Rendimiento**
- ✅ Ajusta workers según CPU del VPS
- ✅ Configura límites de memoria
- ✅ Monitorea recursos del servidor

### **Monitoreo**
- ✅ Configura alertas de backup
- ✅ Monitorea logs regularmente
- ✅ Verifica renovación automática de SSL

## 🚨 Solución de Problemas

### **SSL no funciona**
```bash
# Ver logs de Caddy
docker-compose logs caddy

# Verificar DNS
dig multiacceso.labcit.com

# Reiniciar Caddy
docker-compose restart caddy
```

### **Odoo no inicia**
```bash
# Ver logs detallados
docker-compose logs odoo

# Verificar configuración
docker-compose exec odoo cat /etc/odoo/odoo.conf

# Verificar permisos
ls -la addons/ logs/
```

### **Base de datos no conecta**
```bash
# Verificar PostgreSQL
docker-compose logs db

# Probar conexión
docker-compose exec db psql -U odoo -l
```

### **Revertir migración**
```bash
# Volver a configuración de desarrollo
./scripts/migrate-to-production.sh revert

# Reiniciar servicios
docker-compose down && docker-compose up -d
```

## 📞 Checklist de Migración

### **Pre-migración:**
- [ ] Desarrollo local funcionando correctamente
- [ ] Backup completo creado
- [ ] VPS configurado con Docker
- [ ] DNS configurado correctamente
- [ ] Contraseñas seguras definidas

### **Durante migración:**
- [ ] Archivos subidos al VPS
- [ ] Configuración ajustada
- [ ] Servicios iniciados
- [ ] SSL funcionando
- [ ] Aplicación accesible

### **Post-migración:**
- [ ] Backups automáticos configurados
- [ ] Monitoreo activo
- [ ] Documentación actualizada
- [ ] Equipo notificado de nueva URL

## 🎉 ¡Migración Exitosa!

Una vez completada la migración:

- 🌐 **Producción:** https://multiacceso.labcit.com
- 💻 **Desarrollo:** http://localhost
- 📊 **Monitoreo:** `docker-compose logs -f`
- 💾 **Backups:** Automáticos cada día

¡Tu Odoo 14 está listo para producción con todas las funcionalidades de desarrollo y backup incluidas!
