"""
URL configuration for MonGâteau project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from orders.views import OrderViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cakes/', include('cakes.urls')),
    path('api/orders/', include('orders.urls')),
    # Route directe pour la vérification QR code (sans /api/ pour URLs courtes)
    path('verify/<str:order_number>/', 
         OrderViewSet.as_view({'get': 'verify'}), 
         name='verify_order'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
