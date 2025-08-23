# Guía de Despliegue para multiacceso.labcit.com

## 🚀 Configuración para Producción

### Prerrequisitos del Servidor
- Docker y Docker Compose instalados
- Puertos 80 y 443 abiertos
- DNS configurado para `multiacceso.labcit.com` apuntando al servidor

### Pasos de Despliegue

1. **Preparar el servidor**
   ```bash
   # Actualizar sistema
   sudo apt update && sudo apt upgrade -y
   
   # Instalar Docker si no está instalado
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   
   # Instalar Docker Compose
   sudo apt install docker-compose -y
   ```

2. **Clonar y configurar el proyecto**
   ```bash
   git clone <tu-repositorio> odoo14-prod
   cd odoo14-prod
   
   # Configurar variables de entorno
   cp environment.env .env
   ```

3. **Configurar variables de entorno para producción**
   Edita `.env` con valores seguros:
   ```bash
   POSTGRES_DB=odoo_prod
   POSTGRES_USER=odoo_user
   POSTGRES_PASSWORD=TU_PASSWORD_SUPER_SEGURO_AQUI
   COMPOSE_PROJECT_NAME=odoo14-multiacceso
   ```

4. **Configurar permisos**
   ```bash
   sudo chown -R 101:101 addons/
   sudo chown -R 101:101 logs/
   sudo chmod -R 755 addons/
   sudo chmod -R 755 logs/
   ```

5. **Ejecutar en producción**
   ```bash
   docker-compose up -d --build
   ```

6. **Verificar el despliegue**
   ```bash
   # Ver logs
   docker-compose logs -f
   
   # Verificar servicios
   docker-compose ps
   ```

### Configuración DNS

Asegúrate de que el DNS esté configurado correctamente:
```
multiacceso.labcit.com A 192.168.1.100  # IP de tu servidor
```

### Verificación SSL

Caddy obtendrá automáticamente los certificados SSL. Puedes verificar:
```bash
# Ver logs de Caddy para certificados SSL
docker-compose logs caddy | grep -i ssl
```

### Monitoreo

1. **Logs en tiempo real**
   ```bash
   docker-compose logs -f odoo
   ```

2. **Estado de servicios**
   ```bash
   docker-compose ps
   ```

3. **Uso de recursos**
   ```bash
   docker stats
   ```

### Backup Automatizado

Crea un script de backup:
```bash
#!/bin/bash
# backup.sh
DATE=$(date +%Y%m%d_%H%M%S)
docker-compose exec -T db pg_dump -U odoo odoo > "backup_${DATE}.sql"
tar -czf "backup_full_${DATE}.tar.gz" backup_${DATE}.sql addons/
```

### Troubleshooting

1. **Si SSL no funciona**
   ```bash
   # Verificar logs de Caddy
   docker-compose logs caddy
   
   # Reiniciar Caddy
   docker-compose restart caddy
   ```

2. **Si Odoo no arranca**
   ```bash
   # Verificar logs
   docker-compose logs odoo
   
   # Verificar configuración
   docker-compose exec odoo cat /etc/odoo/odoo.conf
   ```

3. **Problemas de permisos**
   ```bash
   sudo chown -R 101:101 addons/ logs/
   docker-compose restart odoo
   ```

### Actualizaciones

Para actualizar el sistema:
```bash
# Hacer backup primero
./backup.sh

# Actualizar código
git pull

# Reconstruir y reiniciar
docker-compose down
docker-compose up -d --build
```
