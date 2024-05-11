from django.urls import path
from .views import BrandViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
