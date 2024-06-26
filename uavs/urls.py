from django.urls import path, include
from .views import brand_form, brand_list, category_form, category_list, uav_form, uav_list, reservation_form, \
    reservation_list, account_reservation_list

app_name = "uavs"

urlpatterns = [
    path('api/', include('uavs.api.urls'), name='brand_api'),
    path('dashboard/brand/create/', brand_form, name='brand_form'),
    path('dashboard/brand/list/', brand_list, name='brand_list'),

    path('dashboard/category/create/', category_form, name='category_form'),
    path('dashboard/category/list/', category_list, name='category_list'),

    path('dashboard/uav/create/', uav_form, name='uav_form'),
    path('dashboard/uav/list/', uav_list, name='uav_list'),

    path('reservation/create/', reservation_form, name='reservation_form'),
    path('dashboard/reservation/list/', reservation_list, name='reservation_list'),

    path('accounts/reservation/list/', account_reservation_list, name='account_reservation_list'),
]
