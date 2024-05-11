from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def home(request):
    return render(request, 'reservation/form.html')


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def superuser_check(user):
    if user.is_authenticated and user.is_superuser:
        return True
    raise PermissionDenied


@user_passes_test(superuser_check)
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
