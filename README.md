# Polls application: 

## I. Notes:
### I.1. .gitignore:
* [Reference](https://github.com/github/gitignore/blob/master/Python.gitignore) about the Python .gitignore

### I.2. .idea:
* Definition: The .idea directory contains a set of configuration files for the project.
* [Reference](https://intellij-support.jetbrains.com/hc/en-us/articles/206544839-How-to-manage-projects-under-Version-Control-Systems) about How to manage projects under Version Control Systems.
* Check status of the .idea folder: 
```commandline
git status .idea/
```

### I.3. Webserver vs. Application server:
* Most of the web frameworks usually contain a lightweight web server for agile development and testing (e.g., Django, ExpressJS, NestJS). However, if you want to run your application on a production site, you must use a robust web server, such as Apache or Nginx.
* Apache is a collection of projects that include a web server (Apache HTTP) and application server (Tomcat), in addition to lots of other middleware libraries and systems.
* [Reference](https://www.educative.io/edpresso/web-server-vs-application-server?utm_source=Google%20AdWords&aid=5082902844932096&utm_medium=cpc&utm_campaign=kb-dynamic-edpresso&gclid=CjwKCAiA17P9BRB2EiwAMvwNyP_uHFhWnD34DERlPxayNvFzEn2bomypbGFVJjGJ-Py9BmMnsqiXxBoCcMgQAvD_BwE).

### I.4. Production deployment: 
* [Reference](https://docs.djangoproject.com/en/3.1/topics/install/).

### I.5. LAN deployment:
* [Reference](https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-runserver) 

### I.6. SQLite:
* [Windows SQLite installation](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
> After installing and adding SQLite shell to the environment variables, you must restart all Pycharm processes to load it.

* To interact with the SQLite DB created by Django:
```commandline
python manage.py dbshell
```
The SQLite client, created by the above command, automatically connect to the SQLite DB of this project. 

## II. Errors: 

## III. Commands:
* The **migrate** command looks at the INSTALLED_APPS  settings and
creates any necessary database tables according to the database settings in the **website/settings.py** file and
the database migrations shipped with the app.
```commandline
python manage.py migrate
```

