from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def superuser_check(user):
    if user.is_authenticated and user.is_superuser:
        return True
    raise PermissionDenied


@user_passes_test(superuser_check)
def brand_form(request):
    return render(request, 'dashboard/brand/form.html')


@user_passes_test(superuser_check)
def brand_list(request):
    return render(request, 'dashboard/brand/list.html')


def category_form(request):
    return render(request, 'dashboard/category/form.html')


def category_list(request):
    return render(request, 'dashboard/category/list.html')


def uav_form(request):
    return render(request, 'dashboard/uav/form.html')


def uav_list(request):
    return render(request, 'dashboard/uav/list.html')


def reservation_form(request):
    return render(request, 'reservation/form.html')


def reservation_list(request):
    return render(request, 'dashboard/reservation/list.html')


def account_reservation_list(request):
    return render(request, 'accounts/reservations.html')
