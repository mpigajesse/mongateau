from rest_framework import serializers
from .models import CakeType


class CakeTypeSerializer(serializers.ModelSerializer):
    """
    Serializer pour les types de gâteaux
    """
    cake_type_display = serializers.CharField(source='get_cake_type_display', read_only=True)
    
    class Meta:
        model = CakeType
        fields = [
            'id',
            'name',
            'cake_type',
            'cake_type_display',
            'description',
            'base_price',
            'image_url',
            'is_available',
            'is_deleted',
            'deleted_at',
        ]
        read_only_fields = ['id', 'is_deleted', 'deleted_at']
