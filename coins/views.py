from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import simplejson as json


# Old code
# def home(request):
#    return render(request, 'coins/home.html')

def home(request):
    if request.method == 'POST' and 'login' in request.POST:
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                name = str(request.user.username)
                return render(request, 'coins/home.html', {'message' : 'Welcome ' + name})
            else:
                return render(request, 'coins/home.html', {'error' : 'Username or Password is incorrect.'} )


    elif request.method == 'POST' and 'create' in request.POST:
            #User has info and wants an account now!
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'accounts/signup.html', {'error' : 'Username already exists'} )
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                    auth.login(request,user)
                    return redirect('home')
            else:
                return render(request, 'coins/home.html', {'error' : 'Passswords must match'} )

    else:
            return render(request, 'coins/home.html')

def logout(request):
    request.method == 'POST'
    auth.logout(request)
    return redirect('home')
