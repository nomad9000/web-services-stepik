#!/usr/bin/env bash
#sudo /etc/init.d/mysql start
#sudo mysql -uroot -e "CREATE DATABASE ask;"
#sudo mysql -uroot -e "CREATE USER 'usr'@'localhost' IDENTIFIED BY 'pwd';"
#sudo mysql -uroot -e "GRANT ALL ON ask.* TO 'usr'@'localhost';"
sudo sqlite3 ask/ask.db .exit
sudo ask/manage.py migrate
#sudo rm /etc/nginx/sites-enabled/default
#sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pkill gunicorn
sudo gunicorn -c /home/box/web/etc/django.py wsgi --daemon --error-logfile error.log