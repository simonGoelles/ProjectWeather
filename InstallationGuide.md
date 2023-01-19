# Installation Guide

Go into the Backend Folder.
create a venv and execute these commands:

pip install -r requirements.txt
pip install -e .

You can run the tests with:
python weather_project/manage.py test

And start the server with:
python weather_project/manage.py runserver


## Docker

sudo docker build . -t docker-django-v0.0
sudo docker run docker-django-v0.0
sudo docker run -it docker-django-v0.0 bash
