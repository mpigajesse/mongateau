"""
Admin-specific URL configuration for orders
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_admin import AdminOrderViewSet, AdminCustomRequestViewSet
from .admin_profile_views import AdminProfileViewSet
from .admin_settings_views import AdminSettingsViewSet

router = DefaultRouter()
router.register(r'orders', AdminOrderViewSet, basename='admin-orders')
router.register(r'custom-requests', AdminCustomRequestViewSet, basename='admin-custom-requests')
router.register(r'profile', AdminProfileViewSet, basename='admin-profile')
router.register(r'settings', AdminSettingsViewSet, basename='admin-settings')

urlpatterns = [
    path('', include(router.urls)),
]
