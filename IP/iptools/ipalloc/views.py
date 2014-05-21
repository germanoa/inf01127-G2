from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth

@login_required(login_url='/')
def index(request):
    return render(request,'index.html')
