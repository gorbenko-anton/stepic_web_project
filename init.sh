sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo gunicorn --bind='0.0.0.0:8080' hello:return_params &
sudo mkdir ask
cd ask
sudo django-admin.py startproject ask .
sudo ./manage.py startapp qa
sudo cp ../uploads/views.py ./qa/
sudo cp ../uploads/urls.py ./ask/
sudo gunicorn -w 2 -c /home/box/web/etc/hello.py hello:app &
sudo gunicorn -w 2 -c /home/box/web/etc/qa.py ask.wsgi:application