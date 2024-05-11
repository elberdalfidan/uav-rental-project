from django.shortcuts import render


def home(request):
    return render(request, 'accounts/home.html')


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')
