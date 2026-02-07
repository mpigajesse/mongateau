from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from .models import AdminSettings
from .admin_settings_serializers import AdminSettingsSerializer


class AdminSettingsViewSet(ViewSet):
    permission_classes = [AllowAny]  # TODO: add auth

    def _get_settings(self):
        settings, _ = AdminSettings.objects.get_or_create(
            id=1,
            defaults={
                'store_name': 'MonGâteau',
                'store_phone': '+241 07 40 13 02',
                'store_email': 'mpigajesse23@gmail.com',
                'store_address': 'Libreville, Gabon',
                'email_notifications': True,
                'sms_notifications': True,
                'order_notifications': True,
                'min_order_days': 2,
                'delivery_fee': 0,
                'tax_rate': 0,
                'items_per_page': 10,
                'default_currency': 'FCFA',
                'language': 'fr',
            }
        )
        return settings

    def list(self, request):
        settings = self._get_settings()
        serializer = AdminSettingsSerializer(settings)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        settings = self._get_settings()
        serializer = AdminSettingsSerializer(settings, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
