sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/hello.py hello:wsgi_application --daemon --error-logfile error.log
sudo gunicorn -c /home/box/web/etc/django.py wsgi --daemon --error-logfile error.log