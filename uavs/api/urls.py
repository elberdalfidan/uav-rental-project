from django.urls import path
from .views import BrandViewSet, CategoryViewSet, UavViewSet, ReservationViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'uav', UavViewSet, basename='uav')
router.register(r'reservation', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
]
