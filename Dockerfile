FROM odoo:14

# Cambiar a usuario root para instalar dependencias
USER root

# Actualizar sistema e instalar dependencias adicionales
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    libevent-dev \
    libsasl2-dev \
    libldap2-dev \
    libpq-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    zlib1g-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python adicionales (opcional)
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Crear directorio para módulos personalizados
RUN mkdir -p /mnt/extra-addons

# Copiar módulos personalizados si existen
COPY ./addons /mnt/extra-addons/

# Cambiar permisos
RUN chown -R odoo:odoo /mnt/extra-addons

# Volver al usuario odoo
USER odoo

# Exponer puerto
EXPOSE 8069

# Comando por defecto
CMD ["odoo"]
