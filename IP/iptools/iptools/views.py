from django.shortcuts import render, redirect
from django.contrib import auth

def index(request):
    if request.user is None or not request.user.is_authenticated():
        return redirect('login')
    else:
        return redirect('dashboard')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_authenticated():
            auth.login(request,user)
            return redirect('dashboard')
        else:
            error_message = "Nome de usuario ou senha invalidos."
            return render(request,'login.html', {"error_message" : error_message})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    return render(request,'dashboard.html')
