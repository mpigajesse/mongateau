"""
URL configuration for MonGâteau project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from orders.views import OrderViewSet

from cakes.views_demo import vitrine_demo, commande_demo

# En démo publique, l'administration Django est retirée et « / » sert une
# vitrine qui consomme les mêmes modèles et le même générateur de ticket que l'API.
urlpatterns = [] if settings.DEMO_PUBLIQUE else [path('admin/', admin.site.urls)]
if settings.DEMO_PUBLIQUE:
    urlpatterns += [
        path('', vitrine_demo, name='vitrine-demo'),
        path('commande/', commande_demo, name='commande-demo'),
    ]

urlpatterns += [
    path('api/cakes/', include('cakes.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/admin/', include('orders.urls_admin')),
    path('api/admin/cakes/', include('cakes.urls_admin')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
