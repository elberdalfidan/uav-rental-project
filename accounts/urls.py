from django.urls import path, include
from . import views
app_name = "accounts"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('api/users/', include('accounts.api.urls'), name='user_api'),
]