# Odoo 14 con Docker Compose, Caddy y Módulos Personalizados

Este proyecto configura un entorno completo de Odoo 14 usando Docker Compose con:
- **Odoo 14**: Servidor principal de aplicaciones
- **PostgreSQL 13**: Base de datos
- **Caddy**: Proxy reverso con SSL automático
- **Soporte para módulos personalizados**

## 🚀 Inicio Rápido

### Prerrequisitos
- Docker
- Docker Compose

### Instalación y Ejecución

1. **Clona o descarga este proyecto**
   ```bash
   git clone <tu-repo>
   cd odoo14-prod
   ```

2. **Configura las variables de entorno**
   ```bash
   cp environment.env .env
   # Edita .env con tus valores personalizados
   ```

3. **Construye y ejecuta los contenedores**
   ```bash
   docker-compose up -d --build
   ```

4. **Accede a Odoo**
   - URL Producción: https://multiacceso.labcit.com
   - URL Desarrollo: http://localhost
   - Usuario: admin
   - Contraseña: admin (configurable en `config/odoo.conf`)

## 📁 Estructura del Proyecto

```
odoo14-prod/
├── docker-compose.yml      # Configuración de servicios Docker
├── Dockerfile             # Imagen personalizada de Odoo
├── Caddyfile              # Configuración del proxy Caddy
├── environment.env        # Variables de entorno
├── requirements.txt       # Dependencias Python adicionales
├── config/
│   └── odoo.conf         # Configuración de Odoo
├── addons/               # Módulos personalizados
├── logs/                 # Logs de aplicación
└── README.md            # Este archivo
```

## 🔧 Configuración

### Variables de Entorno
Edita `environment.env` para personalizar:
- Credenciales de base de datos
- Configuraciones específicas del entorno

### Configuración de Odoo
Modifica `config/odoo.conf` para:
- Ajustar parámetros de rendimiento
- Configurar rutas de módulos
- Establecer niveles de logging

### Módulos Personalizados
1. Coloca tus módulos en el directorio `addons/`
2. Reinicia el contenedor de Odoo:
   ```bash
   docker-compose restart odoo
   ```

### Configuración de Caddy
La configuración está lista para el subdominio `multiacceso.labcit.com`:
- SSL automático habilitado
- Headers de seguridad configurados
- También disponible en `localhost` para desarrollo

## 🛠️ Comandos Útiles

### Gestión de Contenedores
```bash
# Iniciar servicios
docker-compose up -d

# Ver logs
docker-compose logs -f odoo

# Detener servicios
docker-compose down

# Reconstruir imagen de Odoo
docker-compose build --no-cache odoo
```

### Base de Datos
```bash
# Backup de base de datos
docker-compose exec db pg_dump -U odoo odoo > backup.sql

# Restaurar base de datos
docker-compose exec -T db psql -U odoo odoo < backup.sql
```

### Desarrollo
```bash
# Acceder al contenedor de Odoo
docker-compose exec odoo bash

# Ver logs en tiempo real
docker-compose logs -f odoo
```

## 🔒 Seguridad para Producción

### Configuraciones Recomendadas

1. **Cambiar contraseñas por defecto**
   - Modifica `admin_passwd` en `config/odoo.conf`
   - Usa contraseñas fuertes en `environment.env`

2. **SSL ya configurado**
   - Configurado para `multiacceso.labcit.com`
   - Caddy obtendrá certificados SSL automáticamente

3. **Configurar workers**
   - Ajusta `workers` en `config/odoo.conf` según tu hardware
   - Recomendado: (CPU cores * 2) + 1

4. **Límites de memoria**
   - Ajusta `limit_memory_hard` y `limit_memory_soft`
   - Monitorea el uso de recursos

## 🐛 Solución de Problemas

### Problemas Comunes

1. **Puerto 80 ocupado**
   ```bash
   # Cambiar puerto en docker-compose.yml
   ports:
     - "8080:80"  # Usar puerto 8080
   ```

2. **Permisos de archivos**
   ```bash
   sudo chown -R 101:101 addons/
   sudo chown -R 101:101 logs/
   ```

3. **Base de datos no conecta**
   - Verifica que PostgreSQL esté funcionando
   - Revisa las credenciales en `environment.env`

### Logs Útiles
```bash
# Logs de todos los servicios
docker-compose logs

# Logs específicos de Odoo
docker-compose logs odoo

# Logs de base de datos
docker-compose logs db
```

## 📦 Dependencias Adicionales

Para agregar dependencias Python:
1. Edita `requirements.txt`
2. Reconstruye la imagen:
   ```bash
   docker-compose build --no-cache odoo
   ```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para detalles.