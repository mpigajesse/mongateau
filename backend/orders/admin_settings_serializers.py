from rest_framework import serializers
from .models import AdminSettings


class AdminSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminSettings
        fields = [
            'id',
            'store_name',
            'store_phone',
            'store_email',
            'store_address',
            'email_notifications',
            'sms_notifications',
            'order_notifications',
            'min_order_days',
            'delivery_fee',
            'tax_rate',
            'items_per_page',
            'default_currency',
            'language',
            'updated_at',
        ]
        read_only_fields = ['id', 'updated_at']
