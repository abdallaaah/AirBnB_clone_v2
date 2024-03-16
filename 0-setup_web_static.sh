#!/usr/bin/env bash
# this is script to configure a new ubuntu machine
sudo apt-get install nginx -qq -y
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
sudo bash -c 'echo "hello from index nginx work " >> /data/web_static/releases/test/index.html'
sudo rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/
# nginx configuations
sudo sed -i '/^\s*location \/hbnb_static\//d' /etc/nginx/sites-available/default
sudo sed -i '/^\s*root\s*/s|^\s*root\s*/[^;]*|root /data/web_static/current|' /etc/nginx/sites-available/default
sudo sed -i '/^\s*server_name _;/a\       location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' /etc/nginx/sites-available/default
sudo systemctl restart nginx
exit 0
