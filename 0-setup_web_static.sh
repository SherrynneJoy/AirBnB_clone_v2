#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static

#Install Nginx if it not already installed
sudo apt-get update
sudo apt-get -y install nginx
#sudo ufw allow 'HTTP nginx'

#creating folders if they don't exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#a symbolic link /data/web_static/current linked to the test folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

service nginx restart
