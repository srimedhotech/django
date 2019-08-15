11. Now Let us add the code for register function in views.py 

    ```
    #Let us import the User and auth models from django.contrib.auth.models
	
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
		    user = User.objects.create_user(username=username, password=password, 
				email=email, first_name=first_name, last_name=last_name)
			user.save()
			return redirect('login')
			
		else:
			message.info("Passwords does not match")
			return redirect('/register/')


    ```