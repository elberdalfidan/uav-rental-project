from django.urls import path
from .views import UserCreateAPIView, UserListAPIView, UserDetailAPIView, UserLoginAPIView, UserLogoutAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_detail"),
    path("register/", UserCreateAPIView.as_view(), name="user_create"),
    path("login/", UserLoginAPIView.as_view(), name="user_login"),
    path("logout/", UserLogoutAPIView.as_view(), name="user_logout"),
    path("<int:id>/", UserDetailAPIView.as_view(), name="user_detail"),
]
