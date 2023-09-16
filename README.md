
# Django API

## Acerca de este proyecto

En el siguiente repositorio se podrá encontrar los archivos Python con el framework de django. en un ambiente WINDOWS

## Se debe de tener instalado Python 3.10 y mysql,

## Crear la base de datos en mysql y agregar lo datos en el archivo: Api_proyecto\Api_proyecto\settings.py (los datos de la base de datos puede cambiar)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASS': '',
        'NAME': 'django4-api-labclinico',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

```
## Se debe de tener PIP que viene con Python, el siguiente comando puede ayudar a ver que paquetes se deben de tener.

```python

>pip list
Package           Version
----------------- -------
asgiref           3.7.2
distlib           0.3.7
Django            4.2.5
filelock          3.12.3
pip               23.2.1
platformdirs      3.10.0
setuptools        63.2.0
sqlparse          0.4.4
typing_extensions 4.7.1
tzdata            2023.3
virtualenv        20.24.5

```

## Se debe de generar las migraciones.

```python

> python Api_proyecto\manage.py makemigrations

# Debe tener las configuraciones bien, y la base de datos configurada.

```

## Se debe de aplicar las migraciones la base de datos.

```python

> python Api_proyecto\manage.py migrate

# Debe tener las configuraciones bien, y la base de datos configurada.

```

## Se debe de crear un super-usuario por lo menos.

```python

> python Api_proyecto\manage.py createsuperuser

# Debe tener las configuraciones bien, y la base de datos configurada he ingresar los datos que solicita, como: user, correo, y password.

```


## Se debe de activar un ambiente para que se pueda luego correr el servidor.

```python

> .\env\Scripts\activate

# aparecerá algo similar a esto =>: (env) PS C:\

```

## ahora se puede correr el servidor.

```python

> python Api_proyecto\manage.py runserver

# Con el usuario puede ingresar para crear """"un registro por lo menos"""" de cada modelo: http://127.0.0.1:8000/admin

```

## Por ultimo el resultado del comando anterior, mostrara algo similar (se debe de tener como variable global en windows "python"):

```python

#pone en ejecución la aplicación, mostrara un error, pero si se ingresa a: http://127.0.0.1:8000/admin/ se podrá ver la aplicación en ejecución.

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 15, 2023 - 21:25:26
Django version 4.2.5, using settings 'Api_proyecto.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


```

## ahora ya se puede usar el manual que esta en api.blexzy.com

=======
### Extras del framework utilizado.

## Mas información

Join the #django channel on irc.libera.chat. Lots of helpful people hang out there. Webchat is available.
Join the django-users mailing list, or read the archives, at https://groups.google.com/group/django-users.
Join the Django Discord community.
Join the community on the Django Forum.

=======


## Autor

| [<img src="https://avatars.githubusercontent.com/u/8519258?v=4" width=115><br><sub>Jorge Ramos</sub>](https://github.com/sonic-alex2) |
| :---: |
