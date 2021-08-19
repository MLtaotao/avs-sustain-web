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

### create superuser
```
python manage.py createsuperuser
```
username = admin
password = 123456

### create client
username = client
password = P@$$w0rd123

### create staff
username = staff
password = P@$$w0rd123

### create staff
username = staff1
password = P@$$w0rd123

### create 3 consultant
username = consultant1
password = P@$$w0rd123

username = consultant2
password = P@$$w0rd123

username = consultant3
password = P@$$w0rd123

username = consultant4
password = P@$$w0rd123

username = consultant5
password = P@$$w0rd123

username = consultant6
password = P@$$w0rd123



### Install geos library
#### linux
```
sudo apt-get install gdal-bin
```
#### mac
```
brew install gdal
```
email authentication
https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef