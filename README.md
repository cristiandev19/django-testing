

Version de python 
- 3.8.10
Version de pip



## Pasos para crear el proyecto

1. Crear un ambiente virtual en python (venv documentation)[https://docs.python.org/3/tutorial/venv.html]

```
python3 -m venv django-testing
```

2. Activar el ambiente virtual

```
source django-testing/bin/activate
```

3. Instalar Django

```
python -m pip install Django
```

4. Creamos un proyecto en Django

```
django-admin startproject djangoTesting
```

5. Entramos en la carpeta del proyecto

```
cd djangoTesting
```

6. Iniciamos el servidor de desarrollo


```
python manage.py runserver
```

7. 

## Pasos para configurar el proyecto

1. Crear un ambiente virtual en python (venv documentation)[https://docs.python.org/3/tutorial/venv.html]

```
python3 -m venv django-testing
```

2. Activar el ambiente virtual

```
source django-testing/bin/activate
```

3. 


## Informacion extra

El usuario admin tienes estas credenciales

Usuario: admin
Email: admin@admin.com
Password: admin

Usuarios:

```
user: cristian
pass: bvH9oAN7UpBjxi
```

```
user: rose
pass: WPDtNeToSWZDA2
```


Para correr tests

```
python manage.py test posts
```


## Rutas


accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
