from django.urls import path
from .views import CreateBrandAPIView, ListBrandAPIView

urlpatterns = [
    path("", ListBrandAPIView.as_view(), name="brand_list"),
    path("create/", CreateBrandAPIView.as_view(), name="brand_create"),
]