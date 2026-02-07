from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CakeTypeViewSet

router = DefaultRouter()
router.register(r'types', CakeTypeViewSet, basename='cake-type')

urlpatterns = [
    path('', include(router.urls)),
]
