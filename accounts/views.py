from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)

        if password1 and password2 and password1 == password2:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password2'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
       user=auth.authenticate(username = request.POST.get('username', None),password = request.POST.get('password', None))
       if user is not None:
           auth.login(request,user)
           return redirect('home')

       else:
           return render(request, 'accounts/login.html',{'error': 'Username and Passwords must match!'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('logout')



