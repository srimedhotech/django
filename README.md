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
      'todo_app.apps.TodoAppConfig',
    ]
  
    ```
1. You need to know how to create this string, for this, we need to use the structure appname.apps.name_in_apps.py, so in this case it will be ***todo_app.apps.TodoAppConfig*** (app folder name / apps.py without .py and the name in apps.py)

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
 5. Now goto views.py file and add the following lines
     ```
     #add this at the top
     from django.http import HttpResponse
     	...
     	...
     
     def index(request):
         return HttpResponse('<h1>Hello World</h1>')
     
     ```
    Now if you navigate to http://127.0.0.1:8000 you will see the Hello World
    
### Creating Models
1. Let us create a model class named ***Todo*** derived from *models.Model*
2. We need to have two fields, one for the task text and other for the status of the task, if it is completed or not
3. Open ***todo_app/models.py*** and add the below code
    ```
    from django.db import models
    
    class Todo(models.Model):
        text = models.CharField(max_length=80)
        completed = models.BooleanField(default=False)
    
        def __str__(self):
            return self.text
    ```
 4. Now we need to add this to database, use commands one by one
 	* python manage.py makemigrations
 	* python manage.py migrate
 
### Creating Form
 1. In the todo_app, create new file called forms.py and add the below code
     ````
     #todo_app/forms.py
     from django import forms

    class TodoForm(forms.Form):
        text = forms.CharField(max_length=40,widget=forms.TextInput())
     ````
 
### Creating Views
1. Open ***todo_app/views.py*** and replace the entire code with the below.
2. In this we are going to interact with a template called ***todo.html*** and send all this data to that template from view

    ```
    #todo_app/views.py
    from django.shortcuts import render, redirect
    from .models import TodoModel
    from .forms import TodoForm
    
    def index(request):
    
        #get the list of objects using below command objects.all()
        todo_list = Todo.objects.all()
        
        #create the form
        form = TodoForm()
        
        #pass the data and form to the template
        context = {'tasks' : todo_list, 'form' : form}
        
        return render(request, 'todo.html', context)
     ```

### Creating Templates
1. Create a folder called Templates in todo_site/ and also in todo_app/
2. Register this path in the TEMPLATES section in settings.app so that Django knows where to look for the html templates
    ```
	TEMPLATES = [
		{
		   ....
		   
			'DIRS': [ os.path.join(BASE_DIR, 'todo_site/templates')],
			'APP_DIRS': True,
		   
		   ...
		},
	]
    ```
3. Let us create a base template called base.html in todo_site/ folder
4. Add the following content in base.html
    ```
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title>Welcome to My todo List</title>
	</head>
	<body>
		<h1>My Todo List</h1>
		{% block content %}

		{% endblock %}

	</body>
	</html>
    ```
5. Now let us create a new file called todo.html in todo_app/Templates/ directory
6. Add the below code in the todo.html
    ```
	{% extends 'base.html' %}

	{% block content %}
	    <div id="todoform">
		<h4>Enter your Task:</h4>
		<form action="{% url 'add' %}" method="POST">
		    {% csrf_token %}
		    {{ form.text }}
		    <button type="submit">ADD</button>

		</form>
	    </div>
	    <hr>

	    <div id='tasklist'>
		<h4>Your tasks</h4>
		<ul>
		    {% for task in tasks %}
			<li>{{ task.text }} - {{ task.completed }} </li>
		    {% endfor %}
		</ul>
	    </div>
	{% endblock %}
	
	```
7. We are now displaying the form on the top and also the list of the tasks below

### Adding the task
1. Go to todo_app/urls.py add the below entry
   * *path('add', views.addTodo, name='add')* in the urlpatterns
2. Go to todo_app/views.py and add the function for addTodo
    ```
    from django.shortcuts import render, redirect
    from django.views.decorators.http import require_POST
    from .models import Todo
    from .forms import TodoForm
    
    def index(requst):
        .....
    
    @require_POST
    def addTodo(request):
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = Todo(text=request.POST['text'])
            new_todo.save()
        return redirect('/')    
    ```
 
3. ***@require_POST*** decorator to the ***addTodo*** function in views mentions that the addTodo will accept only POST requests
4. We are creating the form and check if it is valid, if so, we are reading the data from the post and storing it in dataase using ***save()*** command.
5. return ***redirect("/")*** indicates that we are taking the user to home page
