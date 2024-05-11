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
