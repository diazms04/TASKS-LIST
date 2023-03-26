# BLOG
This to do list website was built with python, django and PostgreSQL as database. The frontend with HTML and CSS.
Allows you to create and delete tasks, which are stored in a database created in postgreSQL.

![](https://github.com/diazms04/TASKS-LIST/blob/main/Screenshot%202023-03-26%20161204.png)

# To run the app on your computer, follow the steps below:

1. Clone the repository
```
git clone https://github.com/diazms04/TASKS-LIST.git
```

2. Create a virtual environment
```
python3 -m venv virtual_environment_name
#Linux
Source virtual_environment_name/bin/activate
#Windows
virtual_environment_name\Scripts\activate
```

3. Install requirements
```
pip install -r requirements.txt
```
4. Create a database and modify database configuration, in settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'tasksdb',
        'USER': 'postgres',
        'PASSWORD':'password',
        'HOST': 'localhost',
        'PORT': '5432',
            }
         }
```

5. Run the app
```
python manage.py runserver
```
