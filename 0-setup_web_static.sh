#!/usr/bin/env bash
# Sets up server for the deployment of web_static
FILE=/etc/nginx/sites-available/default
STRING="location /hbnb_static/ {\n alias /data/web_static/current/; \n}\n"

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "39i $STRING" $FILE
sudo service nginx restart
