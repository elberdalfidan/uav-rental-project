from django.urls import path, include

app_name = "uavs"

urlpatterns = [
    path('', include('uavs.api.urls'), name='brand_api'),
]
