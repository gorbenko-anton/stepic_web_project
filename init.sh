sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo gunicorn --bind='0.0.0.0:8080' hello:return_params &
sudo django-admin.py startproject ask .
#sudo ./manage.py startapp qa
#cp ./uploads/views.py ./ask/qa/