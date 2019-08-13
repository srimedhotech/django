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

6.
