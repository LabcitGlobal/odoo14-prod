# 🚀 Despliegue VPS - multiacceso.labcit.com

## ✅ **Estado Actual:**
- ✅ IP VPS: `34.123.185.85`
- ✅ DNS configurado: `multiacceso.labcit.com`
- ✅ SSH Key: `multiacceso.pub`
- ✅ Configuración de producción lista
- ✅ Contraseñas seguras configuradas

## 🎯 **Plan de Despliegue con GitHub:**

### **Paso 1: Subir a GitHub**
```bash
# En tu máquina local (desde el directorio del proyecto):
git init
git add .
git commit -m "Initial commit - Odoo 14 production ready"
git branch -M main
git remote add origin https://github.com/tu-usuario/odoo14-multiacceso.git
git push -u origin main
```

### **Paso 2: Conectar al VPS**
```bash
# Desde tu máquina local:
ssh -i multiacceso.pub root@34.123.185.85
```

### **Paso 3: Preparar VPS**
```bash
# En el VPS:
apt update && apt upgrade -y

# Instalar dependencias
wget https://raw.githubusercontent.com/tu-usuario/odoo14-multiacceso/main/install-ubuntu.sh
chmod +x install-ubuntu.sh
./install-ubuntu.sh

# Reiniciar
reboot
```

### **Paso 4: Desplegar desde GitHub**
```bash
# Reconectar después del reboot:
ssh -i multiacceso.pub root@34.123.185.85

# Clonar repositorio
git clone https://github.com/tu-usuario/odoo14-multiacceso.git
cd odoo14-multiacceso

# Desplegar automáticamente
./scripts/deploy-vps.sh
```

### **Paso 5: Verificar Despliegue**
1. **Verificar servicios:**
   ```bash
   docker-compose ps
   ```

2. **Ver logs:**
   ```bash
   docker-compose logs -f odoo
   ```

3. **Acceder a la aplicación:**
   - https://multiacceso.labcit.com

## 🔐 **Credenciales de Producción:**

### **Base de Datos PostgreSQL:**
- Usuario: `odoo`
- Contraseña: `MultiAcceso2024!SecureDB#VPS`

### **Admin Odoo:**
- Contraseña: `MultiAcceso2024!AdminVPS#Secure`

## 📊 **Verificaciones Post-Despliegue:**

### **1. SSL Automático:**
```bash
# Verificar certificado SSL
curl -I https://multiacceso.labcit.com
```

### **2. Backups Automáticos:**
```bash
# Verificar configuración de backups
./scripts/backup-scheduler.sh status
```

### **3. Servicios:**
```bash
# Estado de contenedores
docker-compose ps

# Logs en tiempo real
docker-compose logs -f
```

## 🛠️ **Comandos de Mantenimiento:**

### **Actualizar desde GitHub:**
```bash
cd /root/odoo14-multiacceso
git pull origin main
docker-compose down
docker-compose up -d --build
```

### **Backup Manual:**
```bash
./scripts/backup.sh
```

### **Restaurar Backup:**
```bash
./scripts/restore.sh backup_file.tar.gz
```

### **Ver Logs:**
```bash
# Odoo
docker-compose logs -f odoo

# Caddy (proxy)
docker-compose logs -f caddy

# PostgreSQL
docker-compose logs -f db
```

## 🔧 **Troubleshooting:**

### **Si SSL no funciona:**
1. Verificar DNS: `nslookup multiacceso.labcit.com`
2. Verificar logs de Caddy: `docker-compose logs caddy`
3. Reiniciar Caddy: `docker-compose restart caddy`

### **Si Odoo no inicia:**
1. Ver logs: `docker-compose logs odoo`
2. Verificar permisos: `ls -la addons/ logs/`
3. Reiniciar: `docker-compose restart odoo`

### **Problemas de conectividad:**
1. Verificar firewall: `sudo ufw status`
2. Verificar puertos: `netstat -tulpn | grep :80`
3. Verificar Docker: `docker ps`

## 📱 **Monitoreo:**

### **Recursos del sistema:**
```bash
# CPU y memoria
htop

# Espacio en disco
df -h

# Uso de Docker
docker system df
```

### **Logs importantes:**
- `/var/log/syslog` - Sistema
- `logs/` - Odoo
- Logs de Docker: `docker-compose logs`

## 🎉 **¡Despliegue Exitoso!**

Una vez completado, tendrás:
- ✅ Odoo 14 en https://multiacceso.labcit.com
- ✅ SSL automático con Let's Encrypt
- ✅ Backups automáticos configurados
- ✅ Módulos personalizados funcionando
- ✅ Sistema de backup/restore completo
