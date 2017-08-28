#!/bin/sh

./manage.py makemigrations connection
./manage.py makemigrations
./manage.py migrate
./manage.py compilemessages

./manage.py loaddata accessories
./manage.py shell < ./scripts/init_data.shell.py

echo -n "Do you want to create super user? [y/n] "
read answer2
if [ "$answer2" = "y" ];then
    ./manage.py createsuperuser
fi

echo -n "Do you want to start dev server on 0:8000 ? [y/n] "
read answer
if [ "$answer" = "y" ];then
	./manage.py runserver 0:8000
fi