"""
Admin-specific views for cakes management
"""
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.utils import timezone
from .models import CakeType
from .serializers import CakeTypeSerializer


class AdminCakeTypeViewSet(viewsets.ModelViewSet):
    """
    Admin ViewSet for managing cake types with full CRUD operations
    """
    queryset = CakeType.objects.filter(is_deleted=False)
    serializer_class = CakeTypeSerializer
    permission_classes = [AllowAny]  # TODO: Add admin authentication
    
    def get_queryset(self):
        """
        Admin can see all cakes, including unpublished ones
        """
        return CakeType.objects.filter(is_deleted=False).order_by('-created_at')

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.deleted_at = timezone.now()
        instance.save()
