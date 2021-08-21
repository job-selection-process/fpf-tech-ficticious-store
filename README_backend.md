## Backend

- Requirements
1. Linux
2. Python 3.9
3. virtualenv

- Creating the virtual environment
- Activate the virtual environment
- Install requirements

```bash
virtualenv -p /usr/bin/python3.9 venv-fpf_tech_ficticious_store
source venv-fpf_tech_ficticious_store/bin/activate
pip install -r requirements.txt
```

- creating the django project
- creating the django application

```bash
django-admin startproject ficticious_store
cd ficticious_store/
django-admin startapp product
```

### Configuring product application
1. INSTALLED_APPS
- open 'ficticious_store/settinggs.py'
- add <'product',> in INSTALLED_APPS

2. TEMPLATES
- open 'ficticious_store/settinggs.py'
- add 'template' in DIRS list

### Run server
```bash
cd ficticious_store/
python manage.py runserver
```
