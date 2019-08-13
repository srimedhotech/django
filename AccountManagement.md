# Registartion and Login

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
5. Now let us add the Login, Registration buttons in base.html, we will add the logout button later.

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
	    <label for="first_name">First Name: </label><input type="text" name="first_name" placeholder="First Name"><br>
            <label for="last_name">Last Name: </label><input type="text" name="last_name" placeholder="Last Name"><br>
	    <label for="email">E-mail:</label><input type="email" name="email" placeholder="Email"><br>
	    <label for="username">User Name:</label><input type="text" name="username" placeholder="User Name"><br>
	    <label for="password">Password: </label><input type="password" name="password" placeholder="Password"><br>
	    <label for="cpassword">Password(again):</label> <input type="password" name="cpassword" placeholder="Confirm Password"><br>
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
            <label for="username">User Name:</label><input type="text" name="username" placeholder="User Name"><br>
	    <label for="password">Password: </label><input type="password" name="password" placeholder="Password"><br>
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
11.
