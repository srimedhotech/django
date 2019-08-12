# django

## Instructions for Todo App

### Create Virtual Environment

#### Open command prompt, select a folder say c:\projects.
1. Create a folder ***todos***.
1. Create a virtual environment with name 'todosenv' by using command ***mkvirtualenv todosenv***.

### Create Project
1. Install django with the command ***pip install django***
1. Once the django is installed, create a project using command ***django-admin startproject todo_site***.
1. You will see todo_site/todo_site/files..., rename the top folder ***todo_site*** as ***todo_root***, so your structure will now look like ***todo_root/todo_site***.
1. Verify if everything is fine by running development server with command ***python manage.py runserver***.
1. Type http://127.0.0.1:8000/ on your browser and check if the django page is loaded properly.
### Create App
1. Let us create an app with name todo_app now with the command ***python manage.py startapp todo_app***. This will create the folder with name as todo_app and few files inside that.
1. We need to update the ***settings.py*** now, open ***settings.py*** and add the following line in ***INSTALLED_APPS***.
    ```
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #add here the app name
      'todo_app.apps.Todo_appConfig',
    ]
  
    ```
1. You need to know how to create this string, for this, we need to use the structure appname.apps.name_in_apps.py, so in this case it will be ***todo_app.apps.todo_appConfig*** (app folder name / apps.py without .py and the name in apps.py)

### Create database tables
1. Whenver we create app, we need to create the database tables for the apps in INSTALLED_APPS.
2. First prepare the statements by running command ***python manage.py makemigrations***
3. After that, use the command ***python manage.py migrate***, this will actually create the tables inside the database
4. The database we are going to use for this project is sqlite3 which is inbuilt provided along with django

### Preparing the Navigation with urls.py
1. Open todo_site/urls.py
2. Add the below entries so that any navigation to home is going to the urls.py in the todo_app
    ```
    #todo_site/urls.py
    #change from django.urls import path to from django.urls import path, include
    In the URLPatterns add a new entry 
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        
        #new entry
        path('', include('todo_app.urls'))
    ]
    
    ```
 3. Now go to ***todo_app*** and create a new file called ***urls.py***
 4. Add the below lines in the urls.py of todo_app
     ```
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name = 'index'),
    ]
     ```
 ### Creating Views
 
 
 
 
 
 
 
 
 
 
 
 
