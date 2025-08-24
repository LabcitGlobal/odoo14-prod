FROM odoo:14

# Crear directorio para módulos personalizados
USER root
RUN mkdir -p /mnt/extra-addons && chown -R odoo:odoo /mnt/extra-addons

# Copiar módulos personalizados si existen
COPY ./addons /mnt/extra-addons/
RUN chown -R odoo:odoo /mnt/extra-addons

# Instalar python-crontab usando pip (evitamos apt-get)
RUN pip3 install python-crontab==2.6.0

# Crear script wrapper para pg_dump con credenciales
RUN printf '#!/bin/bash\nexport PGPASSWORD="MultiAcceso2024!SecureDB#VPS"\n/usr/lib/postgresql/16/bin/pg_dump -h db -U odoo "$@"\n' > /usr/local/bin/pg_dump_wrapper && \
    chmod +x /usr/local/bin/pg_dump_wrapper && \
    mv /usr/bin/pg_dump /usr/bin/pg_dump.orig && \
    ln -s /usr/local/bin/pg_dump_wrapper /usr/bin/pg_dump

# Volver al usuario odoo
USER odoo

# Configurar .pgpass para backups automáticos
RUN echo 'db:5432:*:odoo:MultiAcceso2024!SecureDB#VPS' > ~/.pgpass && chmod 600 ~/.pgpass

# Exponer puerto actualizado
EXPOSE 8014

# Comando por defecto
CMD ["odoo"]
