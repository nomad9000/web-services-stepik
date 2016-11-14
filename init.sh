sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE 'ask'"
sudo mysql -uroot -e "CREATE USER 'usr' IDENTIFIED BY 'pwd'"
sudo mysql -uroot -e "GRANT ALL ON ask.* TO 'usr'"
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/hello.py hello:wsgi_application --daemon --error-logfile error.log
sudo gunicorn -c /home/box/web/etc/django.py wsgi --daemon --error-logfile error.log