#!/usr/bin/env bash
# set up my web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "Simple Content" >> /data/web_static/releases/test/index.html

ln -fs /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data

sed -i "/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default

sudo service nginx restart

