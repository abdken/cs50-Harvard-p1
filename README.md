
<img src="https://upload.wikimedia.org/wikipedia/commons/c/cd/EdX_newer_logo.svg" alt="Edx Icone" width="200"/>

## Wiki
## Project(1)
## Get Started!

### Package Req
- Python3
- pip3

### Install
```
pip3 install virtualenv
python3 -m venv wikienv
source wikienv/bin/activate
```
### Install Django modules
```
pip3 install Django
pip3 install markdown2
```
### Open wiki Project folder
```
cd ./wiki 
```

### Run Migrations
```
python manage.py migrate
```
### Start the App
```
python3 manage.py runserver
```
##### Note
You can run Django server on custom port, deaflt port on 8000.
'''
python3 manage.py runserver
'''

### Ref
[youtube project review](https://youtu.be/DCiKW-hDGvw) :sunglasses:

Markdown2 [Docs](https://daringfireball.net/projects/markdown/basics)