#!/bin/bash

output=$(python3 manage.py makemigrations api_pedidos)

if [ "$(echo $output | grep -c 'No changes')" != "1" ]
then
	echo "corriendo makemigrations y migrate"
	python3 manage.py makemigrations api_pedidos &&\
		python3 manage.py migrate
else
	echo "sin cambios en composicion de db"
fi

python3 manage.py runserver 0.0.0.0:8000
