from rest_framework import serializers
from .models import Order, CustomCakeRequest
from cakes.serializers import CakeTypeSerializer


class CustomCakeRequestSerializer(serializers.ModelSerializer):
    """
    Serializer pour les demandes de gâteau sur mesure
    """
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = CustomCakeRequest
        fields = [
            'id',
            'request_number',
            'customer_name',
            'customer_phone',
            'delivery_date',
            'custom_message',
            'estimated_budget',
            'status',
            'status_display',
            'created_at',
        ]
        read_only_fields = ['id', 'request_number', 'status', 'created_at']


class CustomCakeRequestCreateSerializer(serializers.ModelSerializer):
    """
    Serializer pour la création des demandes de gâteau sur mesure
    """
    class Meta:
        model = CustomCakeRequest
        fields = [
            'customer_name',
            'customer_phone',
            'delivery_date',
            'custom_message',
            'estimated_budget',
        ]

    def validate_customer_phone(self, value):
        value = value.replace(' ', '')
        if len(value) < 8:
            raise serializers.ValidationError(
                "Le numéro de téléphone doit contenir au moins 8 chiffres."
            )
        return value

    def validate_delivery_date(self, value):
        from datetime import date, timedelta
        min_date = date.today() + timedelta(days=2)
        if value < min_date:
            raise serializers.ValidationError(
                f"La date souhaitée doit être au minimum le {min_date.strftime('%d/%m/%Y')} "
                "(2 jours à l'avance)."
            )
        return value


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer pour les commandes
    """
    cake_type_details = CakeTypeSerializer(source='cake_type', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'customer_name',
            'customer_phone',
            'cake_type',
            'cake_type_details',
            'custom_message',
            'delivery_date',
            'delivery_address',
            'total_price',
            'status',
            'status_display',
            'ticket_path',
            'created_at',
        ]
        read_only_fields = ['id', 'order_number', 'ticket_path', 'created_at']


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    Serializer pour la création de commandes
    """
    class Meta:
        model = Order
        fields = [
            'customer_name',
            'customer_phone',
            'cake_type',
            'custom_message',
            'delivery_date',
            'delivery_address',
        ]
    
    def validate_customer_phone(self, value):
        """
        Validation du numéro de téléphone
        """
        # Retirer les espaces
        value = value.replace(' ', '')
        
        if len(value) < 8:
            raise serializers.ValidationError(
                "Le numéro de téléphone doit contenir au moins 8 chiffres."
            )
        
        return value
    
    def validate_delivery_date(self, value):
        """
        Validation de la date de livraison
        """
        from datetime import date, timedelta
        
        # La date de livraison doit être au minimum dans 2 jours
        min_date = date.today() + timedelta(days=2)
        
        if value < min_date:
            raise serializers.ValidationError(
                f"La date de livraison doit être au minimum le {min_date.strftime('%d/%m/%Y')} "
                "(2 jours à l'avance)."
            )
        
        return value
