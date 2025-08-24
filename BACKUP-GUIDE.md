# 📦 Guía Completa de Backups para Odoo 14

## 🎯 Resumen Rápido

Esta configuración incluye un sistema completo de backups para Odoo 14 que protege:
- **Base de datos PostgreSQL** (datos de aplicación)
- **Filestore** (archivos adjuntos, imágenes, documentos)
- **Configuraciones** (módulos personalizados, configuraciones)

## 🚀 Scripts Disponibles

### 1. **Backup Completo** (`scripts/backup.sh`)
Realiza backup completo del sistema:
```bash
./scripts/backup.sh
```

**Incluye:**
- ✅ Base de datos PostgreSQL
- ✅ Filestore (archivos de Odoo)
- ✅ Configuraciones y módulos personalizados
- ✅ Compresión automática
- ✅ Verificación de integridad
- ✅ Limpieza automática de backups antiguos (30 días)

### 2. **Backup Solo Base de Datos** (`scripts/backup-db-only.sh`)
Backup rápido solo de PostgreSQL:
```bash
./scripts/backup-db-only.sh
```

**Ideal para:**
- Backups frecuentes durante desarrollo
- Antes de actualizaciones de módulos
- Pruebas rápidas

### 3. **Programador de Backups** (`scripts/backup-scheduler.sh`)
Configura backups automáticos:
```bash
# Instalar backups automáticos
./scripts/backup-scheduler.sh install

# Ver estado
./scripts/backup-scheduler.sh status

# Remover backups automáticos
./scripts/backup-scheduler.sh remove

# Ejecutar backup de prueba
./scripts/backup-scheduler.sh test
```

### 4. **Restauración** (`scripts/restore.sh`)
Restaura backups completos o parciales:
```bash
# Restauración completa
./scripts/restore.sh odoo_full_backup_20241201_143000.tar.gz

# Solo base de datos
./scripts/restore.sh backup.tar.gz --db-only

# Solo archivos
./scripts/restore.sh backup.tar.gz --files-only

# Solo configuraciones
./scripts/restore.sh backup.tar.gz --config-only

# Sin confirmación
./scripts/restore.sh backup.tar.gz --force
```

## ⏰ Programación Automática

### Configuración Recomendada
Al ejecutar `./scripts/backup-scheduler.sh install` se configuran:

- **🔄 Backup Completo**: Domingos 2:00 AM
- **💾 Backup BD Diario**: Lunes-Sábado 2:00 AM  
- **⚡ Backup Rápido**: Cada 4 horas (días laborables)
- **🧹 Limpieza de Logs**: Primer día del mes

### Logs de Backups
Los logs se guardan en:
```
logs/backup.log          # Backups completos
logs/backup-db.log       # Backups de base de datos
logs/backup-quick.log    # Backups rápidos
```

## 📁 Estructura de Backups

```
backups/
├── odoo_full_backup_20241201_143000.tar.gz    # Backup completo
├── db_quick_backup_20241201_150000.sql.gz     # Solo BD
└── .gitkeep
```

### Contenido de Backup Completo
```
backup.tar.gz
├── db_backup_FECHA.sql.gz      # Base de datos
├── filestore_backup_FECHA.tar.gz   # Archivos
└── config_backup_FECHA.tar.gz      # Configuraciones
```

## 🛠️ Uso Práctico

### Antes de Actualizar Módulos
```bash
# Backup rápido de seguridad
./scripts/backup-db-only.sh
```

### Antes de Cambios Importantes
```bash
# Backup completo
./scripts/backup.sh
```

### Migrar a Otro Servidor
```bash
# En servidor origen
./scripts/backup.sh

# Copiar backup al servidor destino
scp backups/odoo_full_backup_*.tar.gz user@nuevo-servidor:/path/

# En servidor destino
./scripts/restore.sh odoo_full_backup_*.tar.gz
```

### Restaurar Solo Datos Después de Error
```bash
# Restaurar solo la base de datos
./scripts/restore.sh backup.tar.gz --db-only --force
```

## 🔍 Verificación y Monitoreo

### Verificar Último Backup
```bash
# Ver backups disponibles
ls -la backups/

# Ver información del último backup
./scripts/backup-scheduler.sh status
```

### Verificar Integridad
```bash
# Los backups se verifican automáticamente
# Para verificar manualmente:
tar -tzf backups/odoo_full_backup_*.tar.gz
```

### Espacio Usado
```bash
# Ver espacio usado por backups
du -sh backups/

# Ver detalles por archivo
du -h backups/*.tar.gz
```

## ⚠️ Consideraciones Importantes

### Seguridad
- ❌ **NO subas backups al repositorio** (contienen datos sensibles)
- ✅ **Configura backups externos** (S3, NAS, otro servidor)
- ✅ **Usa contraseñas fuertes** en producción
- ✅ **Encripta backups** para almacenamiento externo

### Rendimiento
- Los backups pueden afectar el rendimiento durante su ejecución
- Programa backups completos en horarios de baja actividad
- Los backups de solo BD son más rápidos y menos intrusivos

### Almacenamiento
- Los backups se limpian automáticamente después de 30 días
- Configura almacenamiento externo para retención a largo plazo
- Monitorea el espacio disponible regularmente

## 🚨 Recuperación de Emergencia

### Si Odoo No Inicia
```bash
# 1. Ver logs
docker-compose logs odoo

# 2. Restaurar último backup
./scripts/restore.sh $(ls -t backups/*.tar.gz | head -1) --force

# 3. Verificar servicios
docker-compose ps
```

### Si Solo Hay Problemas con BD
```bash
# Restaurar solo base de datos
./scripts/restore.sh backup.tar.gz --db-only --force
```

### Si Se Perdieron Archivos
```bash
# Restaurar solo filestore
./scripts/restore.sh backup.tar.gz --files-only --force
```

## 📞 Troubleshooting

### Error: "Contenedores no están ejecutándose"
```bash
docker-compose up -d
sleep 10
./scripts/backup.sh
```

### Error: "No se puede conectar a PostgreSQL"
```bash
# Verificar contenedor de BD
docker-compose logs db

# Reiniciar servicio
docker-compose restart db
```

### Backup Muy Grande
```bash
# Verificar qué está ocupando espacio
docker-compose exec db psql -U odoo -c "
SELECT schemaname,tablename,attname,n_distinct,correlation 
FROM pg_stats 
WHERE schemaname = 'public' 
ORDER BY n_distinct DESC LIMIT 10;"
```

### Restauración Lenta
- Los backups grandes pueden tardar varios minutos
- Verifica espacio disponible en disco
- Considera restaurar solo lo necesario (--db-only, etc.)

## 🔗 Integración con Servicios Externos

### Subir a AWS S3
```bash
# Después del backup
aws s3 cp backups/odoo_full_backup_*.tar.gz s3://tu-bucket/odoo-backups/
```

### Subir a Google Drive (con rclone)
```bash
# Configurar rclone primero
rclone copy backups/ gdrive:odoo-backups/
```

### Notificaciones por Email
```bash
# Agregar al final de backup.sh
echo "Backup completado: $(date)" | mail -s "Odoo Backup OK" admin@tudominio.com
```
