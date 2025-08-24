#!/bin/bash

# Script de instalación para Ubuntu 22.04 LTS
# Instala Docker, Docker Compose y prepara el sistema para Odoo 14

set -e

echo "🚀 Instalando dependencias para Odoo 14 en Ubuntu 22.04 LTS"

# Actualizar sistema
echo "📦 Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar dependencias básicas
echo "🔧 Instalando dependencias básicas..."
sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    software-properties-common \
    git \
    htop \
    unzip \
    wget

# Instalar Docker
echo "🐳 Instalando Docker..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Instalar Docker Compose (standalone)
echo "🔗 Instalando Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Agregar usuario al grupo docker
echo "👤 Configurando permisos de Docker..."
sudo usermod -aG docker $USER

# Habilitar Docker al inicio
sudo systemctl enable docker
sudo systemctl start docker

# Configurar firewall básico
echo "🔒 Configurando firewall..."
sudo ufw --force enable
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443

# Configurar límites del sistema para containers
echo "⚙️  Configurando límites del sistema..."
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
echo "fs.file-max=65536" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Crear usuario para Odoo (opcional)
echo "👥 Creando usuario odoo..."
if ! id "odoo" &>/dev/null; then
    sudo useradd -m -s /bin/bash odoo
    sudo usermod -aG docker odoo
fi

# Optimizaciones de memoria para PostgreSQL
echo "🗄️  Configurando optimizaciones..."
echo "kernel.shmmax = 134217728" | sudo tee -a /etc/sysctl.conf
echo "kernel.shmall = 2097152" | sudo tee -a /etc/sysctl.conf

# Configurar logrotate para Docker
sudo tee /etc/logrotate.d/docker > /dev/null <<EOF
/var/lib/docker/containers/*/*.log {
  rotate 7
  daily
  compress
  size=1M
  missingok
  delaycompress
  copytruncate
}
EOF

echo "✅ Instalación completada!"
echo ""
echo "🔄 IMPORTANTE: Reinicia el servidor para aplicar todos los cambios:"
echo "   sudo reboot"
echo ""
echo "📝 Después del reinicio, verifica la instalación:"
echo "   docker --version"
echo "   docker-compose --version"
echo "   docker run hello-world"
echo ""
echo "🚀 Luego puedes clonar tu proyecto Odoo y ejecutar:"
echo "   git clone <tu-repo> odoo14-prod"
echo "   cd odoo14-prod"
echo "   cp environment.env .env"
echo "   # Edita .env con tus configuraciones"
echo "   docker-compose up -d --build"
