from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import FileResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Order, CustomCakeRequest
from .serializers import (
    OrderSerializer,
    OrderCreateSerializer,
    CustomCakeRequestSerializer,
    CustomCakeRequestCreateSerializer,
)
from .ticket_generator import generate_order_ticket
import os


class CustomCakeRequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour la gestion des demandes de gâteaux sur mesure
    """
    queryset = CustomCakeRequest.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomCakeRequestCreateSerializer
        return CustomCakeRequestSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour la gestion des commandes
    """
    queryset = Order.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer
    
    def create(self, request, *args, **kwargs):
        """
        Créer une nouvelle commande et générer le ticket PDF
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Créer la commande
        order = serializer.save()
        
        # Générer le ticket PDF
        try:
            ticket_path = generate_order_ticket(order)
            order.ticket_path = ticket_path
            order.save()
        except Exception as e:
            # En cas d'erreur, la commande est quand même créée
            print(f"Erreur lors de la génération du PDF: {e}")
        
        # Retourner la commande avec tous les détails
        output_serializer = OrderSerializer(order)
        return Response(
            output_serializer.data,
            status=status.HTTP_201_CREATED
        )
    
    @action(detail=True, methods=['get'], url_path='download-ticket')
    def download_ticket(self, request, pk=None):
        """
        Télécharger le ticket JPG d'une commande
        """
        order = self.get_object()
        
        if not order.ticket_path or not os.path.exists(order.ticket_path):
            return Response(
                {'error': 'Ticket non disponible'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Retourner le fichier JPG
        return FileResponse(
            open(order.ticket_path, 'rb'),
            as_attachment=True,
            filename=f'ticket_{order.order_number}.jpg',
            content_type='image/jpeg'
        )
    
    @action(detail=False, methods=['get'], url_path='verify/(?P<order_number>[^/.]+)')
    def verify(self, request, order_number=None):
        """
        Vérifier une commande via son numéro (pour le QR code)
        Retourne JSON pour API ou HTML pour navigateur
        """
        try:
            order = Order.objects.get(order_number=order_number)
            
            # Si c'est une requête API (Accept: application/json), retourner JSON
            if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                return Response({
                    'valid': True,
                    'order_number': order.order_number,
                    'customer_name': order.customer_name,
                    'cake_type': order.cake_type.name,
                    'delivery_date': order.delivery_date,
                    'total_price': order.total_price,
                    'status': order.status,
                    'status_display': order.get_status_display(),
                    'message': 'Commande valide ✓'
                })
            
            # Sinon, retourner une page HTML (pour QR code scanné depuis mobile)
            context = {
                'valid': True,
                'order_number': order.order_number,
                'customer_name': order.customer_name,
                'cake_type': order.cake_type.name,
                'delivery_date': order.delivery_date.strftime('%d/%m/%Y'),
                'total_price': order.total_price,
                'status': order.status,
                'status_display': order.get_status_display(),
            }
            return render(request, 'orders/verify_order.html', context)
            
        except Order.DoesNotExist:
            # Si c'est une requête API, retourner JSON
            if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
                return Response({
                    'valid': False,
                    'message': 'Commande introuvable ✗'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Sinon, retourner page HTML d'erreur
            context = {
                'valid': False,
                'message': 'Commande introuvable'
            }
            return render(request, 'orders/verify_order.html', context)
    
    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        """
        Consulter le statut d'une commande
        """
        order = self.get_object()
        return Response({
            'order_number': order.order_number,
            'status': order.status,
            'status_display': order.get_status_display(),
            'delivery_date': order.delivery_date,
        })
