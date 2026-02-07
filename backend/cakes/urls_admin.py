"""
Admin-specific URL configuration for cakes
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_admin import AdminCakeTypeViewSet

router = DefaultRouter()
router.register(r'', AdminCakeTypeViewSet, basename='admin-cakes')

urlpatterns = [
    path('', include(router.urls)),
]
