from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from .models import CakeType
from .serializers import CakeTypeSerializer


class CakeTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet pour la consultation des types de gâteaux.
    Les clients peuvent uniquement consulter, pas créer/modifier.
    """
    queryset = CakeType.objects.filter(is_available=True)
    serializer_class = CakeTypeSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
