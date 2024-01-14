#!/usr/bin/env bash
# Script to set up web servers for web_static deployment

# Update package list
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Allow Nginx HTTP traffic
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a test index.html file
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create symbolic link to the test release
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership to ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Add alias for hbnb_static in Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx service
sudo service nginx restart

