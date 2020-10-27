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
sudo cp ../uploads/settings.py ./ask/
sudo cp ../uploads/urls.py ./ask/
#sudo gunicorn --bind='0.0.0.0:8000' -w 2 -c /home/box/web/etc/hello.py hello:app &
sudo gunicorn --bind='0.0.0.0:8000' -w 2 -c /home/box/web/etc/qa.py ask.wsgi:application &
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database stepic_web;"
sudo mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
sudo cp ../uploads/models.py ../ask/qa/
#sudo ./manage.py syncdb
sudo ./manage.py makemigrations
sudo ./manage.py migrate


#sudo pip3 install virtualenv
#sudo pip3 install pathlib2
#virtualenv -p python3 venv
#source venv/bin/activate
#pip3 install django

#sudo rm -rf /etc/nginx/sites-enabled/default

#sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx_2_1_11.conf

#sudo /etc/init.d/nginx restart

#gunicorn -w 2 -c /home/box/web/etc/hello.py hello:app & gunicorn -w 2 -c /home/box/web/etc/qa.py ask.wsgi:application & curl -vv 'http://127.0.0.1:8000/login/'