from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from .models import AdminProfile
from .admin_profile_serializers import AdminProfileSerializer


class AdminProfileViewSet(ViewSet):
    permission_classes = [AllowAny]  # TODO: add auth

    def _get_profile(self):
        profile, _ = AdminProfile.objects.get_or_create(
            id=1,
            defaults={
                'full_name': 'Naomie Moussavou',
                'email': 'mpigajesse23@gmail.com',
                'phone': '',
                'address': '',
            }
        )
        return profile

    def list(self, request):
        profile = self._get_profile()
        serializer = AdminProfileSerializer(profile)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        profile = self._get_profile()
        serializer = AdminProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
