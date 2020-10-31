from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'Register/home.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'Register/register.html', {'warning': 'Username already taken.'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'Register/register.html', {'warning': 'Email already taken'})

        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        login(request, new_user)

        return redirect('/')


    else:
        return render(request, 'Register/register.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'Register/login.html', {'warning': 'Username or Password didn\'t matched.'})



    else:
        return render(request, 'Register/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')
    
