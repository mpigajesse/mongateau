from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CustomCakeRequestViewSet

router = DefaultRouter()
router.register(r'custom-requests', CustomCakeRequestViewSet, basename='custom-cake-request')
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
