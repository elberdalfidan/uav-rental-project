from django.urls import path, include
from .views import brand_form, brand_list

app_name = "uavs"

urlpatterns = [
    path('api/', include('uavs.api.urls'), name='brand_api'),
    path('dashboard/brand/create/', brand_form, name='brand_form'),
    path('dashboard/brand/list/', brand_list, name='brand_list'),
]
