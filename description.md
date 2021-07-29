# AVS Sustainability process

## Code of all the process

### check the python environment, make sure the python version is higher than 3.6

### Create an virtual environment
```
python -m venv avs-sustain-web/venv
```

### Start the virtual env
```
source avs-sustain-web/venv/bin/activate
```
### upgrade pip 
```
pip install --upgrade pip
```

### install django 
```
pip install Django
```

### init the project
```
cd avs-sustain-web 
django-admin startproject avs_web 
```

### check the django project
```
python -m django --version
python manage.py runserver
```

### start app 
```
python manage.py startapp avsapp
```


