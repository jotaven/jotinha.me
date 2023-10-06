
# https://jotinha.me

Site simples criado para apresentar minhas habilidades utilizando Django e Tailwind


## Instalação

Crie o ambiente virtual:
```
$ cd jotinha.me/
$ python3 -m venv env
$ source env/bin/activate
```

Instale as dependencias do Django:

```
$ pip3 install -r requirements.txt
```
    
Instale as dependencias do Tailwind:

```
$ npm install -D tailwindcss
$ cd theme/static_src/
$ npm start
$ cd ../..
```

Crie um arquivo .env e configure a DJANGO_SECRET_KEY e altere para o falor da sua chave

```
DJANGO_SECRET_KEY=<YOUR-KEY>
```

Para criar uma Secret Key entre no shell do django e execute as seguintes linhas de código (pode usar a já gerada abaixo se quiser):

```
$ python3 manage.py shell
```


```
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())

kkwh4=n(&a&a1-m^o=t^$k&4&yknf+shp0c2jl53--$x#rcc15
```

Migre o banco de dados e colete os arquivos estáticos:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py collectstatic
```

Rode o servidor na sua maquina ou na rede local:


```
$ python3 manage.py runserver
```
ou
```
$ python3 manage.py runserver 0.0.0.0:8000
```