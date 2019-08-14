# Registration and Login

- Please see the previous notes on Todo App
-  This is continuation to that 

- We want the provide todo list to be avaiable to users based on their login  i.e. respective users will have their own todo list

## Create new App 'accounts'
Let us create a new app called 'accounts' in our todo project

First let us switch to our environment with command
```
	workon <environment_name>,
```
i.e. now it could be workon todoenv

- Next, create the app using command ***python manage.py startapp account***

#### NOTE:
* There is an in-built support for user and auth models from django.contrib.auth.models (which are part of django.contrib.auth package - used to manage users and their authentication) 
* We can check this module in INSTALLED_APPS section of settings.py, ***Have you checked it?***

### Adding the Navigations
1. First Go to accounts folder and create a new file called urls.py
2. Add the below code for Registration, login and logout

    ```
    from django.urls import path
    from . import views
    urlpatterns = [
	    path('register', views.register, name = 'register'),
        path('login', views.login, name='login'),
        path('logout', views.logout, name='logout')
    ]
    ```
3. Goto todo_site/urls.py and add the below line
    ```
    path('accounts/', include('accounts.urls'))
    ```
4. Let us add dummy functions for now in views.py
    ```
    def login(request):
        pass
    def logout(request):
        pass
    def register(request):
        pass
    ```
5. Now let us add the Login, Registration buttons in base.html, we will add the logout button later. This has to be added immediately after the body tag.

    ```
	In the style tags add the below css

	.menu {
		  background-color: #ccc;
		  overflow: hidden;
		}
	.menu a{
		float: right;
		display: block;
		color: #f2f2f2;
		text-align: center;
		padding: 14px 16px;
		text-decoration: none;
		font-size: 17px;
		margin-right: 60px;
		font-family: Arial;
		font-size: 20px;
	}

	<!-- In the body section add the below code-->

	<p>Welcome </p>

	<div class="menu">
		<a href="/">Home</a>
		<a href="/accounts/register">Registration</a>
		<a href="/accounts/login">Login</a>
	</div>
	
	<h1>My Todo List</h1>
	...

    ```
Please note that we have add the registration link as /accounts/register -- not just /register, because register is part of the accounts app. Similarly for login, we will add /accounts/login

6. views.py 
	
	```
	def register(request):
            return render(request, 'register.html', {})
    ```
7. Let us create a new folder Templates inside the accounts App and also create a new file with name 'register.html' 
8. Open register.html and add the code below
   - As you know the registration form will have fields like  First Name, Last Name, Email, User Name, Password, Confirm Password and Submit button. The same is done below with label and input type(s). As you now for every form we need to add csrf_token tags to prevent the CSRF attack.
9. Also you might have observed that we have added a for loop with messages. The message object is used for displaying the message

    ```
    {% extends 'base.html' %}

    {% block content %}

    <div id='registerid'>
        <form action="register" method="post">
	{% csrf_token%}
	    First Name: <input type="text" name="first_name" placeholder="First Name"><br>
	    Last Name: <input type="text" name="last_name" placeholder="Last Name"><br>
	    E-mail:<input type="email" name="email" placeholder="Email"><br>
	    User Name:><input type="text" name="username" placeholder="User Name"><br>
	    Password: <input type="password" name="password" placeholder="Password"><br>
	    Password(again): <input type="password" name="cpassword" placeholder="Confirm Password"><br>
	    <input type="Submit">
	</form>
	<div>
	    {% for message in messages %}
	        <h3>{{ message }}</h3>
	    {% endfor %}
	</div>
    </div>
    {% endblock %}
    ```
10. Similarly create a file called login.html inside the templates of accounts app and add the content given below. Similar to the registration form, Login form has User name and Password along with submit button. Any messages are printed below the form in the messages for loop

    ```
    {% extends 'base.html' %}
    {% block content %}
    <div id='loginid'>
        <form action="login" method="post">
            {% csrf_token%}
            User Name: <input type="text" name="username" placeholder="User Name"><br>
	    Password: <input type="password" name="password" placeholder="Password"><br>
	    <input type="Submit">
        </form>
        <div>
            {% for message in messages %}
            <h3>{{ message }}</h3>
            {% endfor %}
        </div>
    </div>
    {% endblock %}
    ```
11. Now Let us add the code for register function in views.py 

    ```
    #Let us import the User and auth models from django.contrib.auth.models
    from django.shortcuts import render, redirect
    from django.contrib import messages
    from django.contrib.auth.models import User, auth

    def register(request):
        if request.method == 'POST':
	    first_name = request.POST['first_name']
	    last_name = request.POST['last_name']
	    username = request.POST['username']
            email = request.POST['email']
	    password = request.POST['password']
	    cpassword = request.POST['cpassword']
		
	    #First check if both password match
	    if password == cpassword:
		if User.objects.filter(username=username)).exists():
		    messages.info(request, 'Username is already exists ')
		elif User.objects.filter(email=email).exists():
		    messages.info(request, 'Email already exists')
		else:
		    user = User.objects.create_user(username=username, password=password, 
		    email=email, first_name=first_name, last_name=last_name)
    		    user.save()
		return redirect('login')
	    else:
		messages.info(request, "Passwords does not match")
		return redirect('/register/')
    ```
12. In the above we have used in built method of User (create_user) by calling User.objects.create_user(...)
13. We need to do multiple checks here, First check is to verify if passwords are matching. Next step is to check if the username is already existing in the database and also verify if the email is already in the database, in all the 3 scnearios above we need to show a message using ***message*** object
15. We can use ***message*** object to show the messages as info, error, warning etc.,
16. Now refresh the browser, click on register link and fill the form and submit. You can also verify if the user is successfully created or not in the database using SQLiteDatabaseBrowser tool.(You can download this from https://sqlitebrowser.org/dl/)
17. Similarly now let us handle login in views.py
    ```
    def login(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
	    if user is not None:
	        auth.login(request, user)
	        return redirect("/")
	    else:
	        messages.info(request, "Invalid Credentials")
	        return redirect('/login/')
	else:
	    return render(request, 'login.html', {})

    ```
18. To verify if the user can login, we can use auth.authenticate method by passing the username and password and it will return a user object. If user is not present, it will return None, otherwise it will return the user. We will now login the user by calling ***user.login*** method by passing the user object that we got from auth.authenticate. If the user is None, then we need to show message "Invalid Credentials" and redirect the user to the login page.
19. You can test this by going to http://127.0.0.1 and clicking on login link 
20. Here, finally we need to make slight changes, if the user is registered/logged in, then we need to show logout button only and hide the login and registration button.
21. To achieve this, let us modify the body in base.html
    ```
    <h1>Welcome to My Todo List</h1>
    {% if user.is_authenticated %}
    <p>Welcome, {{user.first_name}}</p>
    {% endif %}
    <div class="menu">
	<a href="/">Home</a>
	{% if user.is_authenticated %}
	    <a href="/accounts/logout">Logout</a>
	{% else %}
            <a href="/accounts/register">Registration</a>
	    <a href="/accounts/login">Login</a>
	{% endif %}
	</div>
    ```
22. First we have added a new anchor tags with log out i.e. /accounts/logout. Next, we are checking if the user is authenticated and based on that we are showing the respective buttons. In this, if the user is authenticated, we are showing only logout and not displaying the Registration and Login buttons
23. Also, we will show the welcome message with user name so we have added welcome, {{user.first_name}}
24. Now test all scenarios and see if the proper error messages are shown to the user in both registration and login
25. Last, we need to handle the logout, if the user clicks on logout, we need to logout the user and take him back to login page
26. We will achieve the same by adding the below code in views.py
    ```
    def logout(request):
	auth.logout(request)
	return redirect('/login/')
    ```
    To explain the above, we need to call auth.logout method and pass the request. Then we need to redirec the user to login page using redirect method
27. That's it, Your Todo App is now having the Registration and Login functionality.
