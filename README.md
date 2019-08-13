# django

## What are we going to do in this?
We will create a todo app which will 
* Allow to "Add Tasks"
* Display the Tasks Added along with the Status
* The completed tasks are striked off
* The pending tasks are shown as URLs
* If a pending task is clicked, then it will be converted as completed task (striked off)

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
    from .models import Todo
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

### Mark the Tasks as Completed
We are going to show the pending tasks as URLs
1. Go to base.html and add style tag in the head
    ```
    <head>
     ...
    <style>
        .todo-completed {
            text-decoration: line-through;
            background: rgba(149, 165, 166, .3);
        }
    </style>
    </head>
    ```
2. Now goto todo.html and modify the code below the hr tag as

    ```
        <div id='tasklist'>
        <h4>Your tasks</h4>
        <ul>
            {% for task in tasks %}
                {% if task.completed %}
                    <li class="todo-completed">{{ task.text }} </li>
                {% else %}
                    <a href="{% url 'complete' task.id %}"><li>{{ task.text }}</li></a>
                {% endif %}
            {% endfor %}
        </ul>
    </div>
    ```
3. If you understand the changes, we are checking if the task is completed, if so, we are showing as striked off using the style todo-completed.
4. If the Task is not completed, then we are displaying text of the task as a URL, but the URL will be url/complete/<id>.
5. Now we need to add this path in the urls.py of todo_app
6. Goto todo_app/urls.py and add the entry in urlpatterns as
	path('complete/<todo_id>', views.completeTodo, name='complete'),
	
7. Next open todo_app/views.py add the ***completeTodo*** function
	
    ```
	def completeTodo(request, todo_id):
	    todo = Todo.objects.get(pk=todo_id)
	    todo.completed = True
	    todo.save()

	    return redirect('/')
    ```
8. Now refresh your browser with CTRL + SHIFT + R
9. Add task and check if it is added as hyper link
10. Click on the link, it will be marked as completed and striked through

### Deleting the completed task
1. Add a button in the todo.html below the form tag to show the button "Delete Completed"
    ```
        <div>
            <a href="{% url 'deletecomplete' %}"><button type="button">DELETE COMPLETED</button></a>
        </div>
    ```
2. In the todo_app/urls.py add the entry in urlpatterns as
    ```
	path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    ```
3.  Next open todo_app/views.py add the ***deleteCompleted*** function
    ```
	def deleteCompleted(request):
    	    TodoModel.objects.filter(completed__exact=True).delete()    
    	    return redirect('/')
	    
    #completed__exact - This will get the records whose status is completed. The name before _exact is derived from the model field 'completed' in Todo model
    
    ```
4. That's it, now force refresh your browser with CTRL + SHIFT + R
5. You should be able to see all tasks (pending and completed), mark some of the tasks as completed 
6. Click on the DeleteCompleted Button, your completed tasks will be cleared. Also you can check the same in the database

### Deleting all tasks (items)

1. Add a button in the todo.html below the deleteCompleted button to show the button "Delete All"
    ```
 	<div>
            <a href="{% url 'deletecomplete' %}"><button type="button">DELETE COMPLETED</button></a>
        </div>   
        <div>
            <a href="{% url 'deleteall' %}"><button type="button">DELETE ALL</button></a>
        </div>
    ```
2. In the todo_app/urls.py add the entry in urlpatterns as
    ```
	path('deleteall', views.deleteAll, name='deleteall'),
    ```
3.  Next open todo_app/views.py add the ***deleteAll*** function
    ```
	def deleteAll(request):
    	    TodoModel.objects.all().delete()    
    	    return redirect('/')
    ```
4. That's it, now force refresh your browser with CTRL + SHIFT + R
5. You should be able to see all tasks (pending and completed), mark some of the tasks as completed 
6. Click on the DeleteAll Button, your all tasks will be removed. Also you can check the same in the database

## Handling the Todo from the Backend i.e. Admin
1. Open admin.py in the todo_app/admin.py
2. Now we need to register our Model ***Todo*** here
3. Add the below entry
    ```
    from .models import Todo
    
    #Register your models here
    admin.site.register(Todo)
    ```
4. If  you have not created super user, Goto command prompt and issue the command
- python manage.py createsuperuser and provide username, email, password, repeat password.
5. Now navigate to http://127.0.0.1/admin
6. Login with the credentials you have used in step 4 above (while creating the super user)
7. You should be able to see the "Todo" in the Todo App
8. You can add / edit / delete the Tasks here.
9. The same can be seen reflected in the frontend as well


