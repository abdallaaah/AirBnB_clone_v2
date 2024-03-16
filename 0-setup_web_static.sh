#!/usr/bin/env bash
# this is script to configure a new ubuntu machine
apt-get install nginx -y
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "hello from index nginx work " >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current 
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '58i\	location /hbnb_static/ {
        alias /data/web_static/current/;
        }' /etc/nginx/sites-available/default
sudo systemctl restart nginx





