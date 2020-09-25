# Sales App

This is a web-based system where the store manager can upload a CSV file into system.
A tabular display then show all sales conducted in a specific period 

## Features

- Django 2.0+
- Uses [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org). 
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).


## How to install

- Install pipenv 

```bash
$ pipenv install --dev
```
- Run the project 
```bash
$ python manage.py migrate
$ python manage.py runserver
```




