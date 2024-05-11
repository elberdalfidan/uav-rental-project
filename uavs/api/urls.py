from django.urls import path
from .views import BrandViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'brand', BrandViewSet, basename='brand')

urlpatterns = [
    # path("brand/list/", BrandViewSet.as_view({'get': 'list', 'delete': 'destroy'}), name="brand_list"),
    path('', include(router.urls)),
]
