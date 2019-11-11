creat webTools by command line : 

check the python version : 
python - python3 - 3.7.4
pip - pip3 - pip in python 3.7
easy_install-3.7

>mkdir webTools
>cd webTools
>pip3 install virtualenv
>virtualenv —version
16.7.7

>virtualenv transactionCorrection


Now, activate the virtual environment by typing the following command. Please Make sure you are in the virtual environment directory.
//todo activate virtualenv
>cd trainsactionCorrection
>source bin/activate
So, our virtual environment has been started. Now, this is the time to install the Django Framework.
We recommend using the latest version of Python 3. The last version to support Python 2.7 is Django 1.11 LTS.
The latest official version is 2.2.7 (LTS).
pip3 install Django==2.2.7
Creat project : 
Interpreter : 
Path : ${PROJECT/venv/bin/python
Version : 3.7
>django-admin startproject correction
>cd correction
>python manage.py runserver
This will run a serveur to response http://localhost:8000

Creat app:
a project can include one or more apps. We could creat app with command line : 
>python manage.py startapp correctionApp