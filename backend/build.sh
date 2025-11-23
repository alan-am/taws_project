#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

#reinicio de tablas
python manage.py migrate pedidos zero
python manage.py migrate usuario zero

python manage.py migrate

#Carga de datos
python manage.py cargar_usuarios