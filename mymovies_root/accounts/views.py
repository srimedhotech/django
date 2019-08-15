from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def logout(request):
	auth.logout(request)
	return redirect("/")

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

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']

		canregister = can_register(username, password, cpassword, email)

		if canregister == 1:
			user = User.objects.create_user(username=username, password=password, 
				email=email, first_name=first_name, last_name=last_name)
			user.save()
			#messages.success(request, "user {} is registered successfully".format(username))
			return redirect('login')
		elif canregister == 0:
			messages.info(request, "passwords does not match")
			return redirect('/register/')
		elif canregister == -1:
			messages.info(request, "Username already exists")
			return redirect('/register/')
		elif canregister == -2:
			messages.info(request, "Email already exists")
			return redirect('/register/')
		return redirect("/")
	else:
		return render(request, 'register.html', {})

def can_register(username, password, cpassword, email):
	if(password != cpassword):
		return 0
	elif(User.objects.filter(username=username)).exists():
		return -1
	elif User.objects.filter(email=email).exists():
		return -2
	else:
		return 1