from rest_framework import serializers
from .models import AdminProfile


class AdminProfileSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = AdminProfile
        fields = [
            'id',
            'full_name',
            'email',
            'phone',
            'address',
            'new_password',
            'updated_at'
        ]
        read_only_fields = ['id', 'updated_at']

    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password', '')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if new_password:
            instance.set_password(new_password)
        instance.save()
        return instance
