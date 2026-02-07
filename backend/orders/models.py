from django.db import models
from cakes.models import CakeType
import uuid


class CustomCakeRequest(models.Model):
    """
    Demande de gâteau sur mesure (pré-commande)
    """
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('contacted', 'Contacté'),
        ('quoted', 'Devis envoyé'),
        ('approved', 'Validé'),
        ('cancelled', 'Annulé'),
    ]

    request_number = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
        verbose_name="Numéro de demande"
    )

    customer_name = models.CharField(
        max_length=200,
        verbose_name="Nom du client"
    )
    customer_phone = models.CharField(
        max_length=20,
        verbose_name="Téléphone"
    )
    delivery_date = models.DateField(
        verbose_name="Date souhaitée"
    )
    custom_message = models.TextField(
        blank=True,
        verbose_name="Message ou détails"
    )
    estimated_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Budget estimé (FCFA)"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Statut"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Date de modification"
    )

    class Meta:
        verbose_name = "Demande gâteau sur mesure"
        verbose_name_plural = "Demandes gâteaux sur mesure"
        ordering = ['-created_at']

    def __str__(self):
        return f"Demande {self.request_number} - {self.customer_name}"

    def save(self, *args, **kwargs):
        if not self.request_number:
            self.request_number = f"MGC-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)


class Order(models.Model):
    """
    Modèle représentant une commande de gâteau
    """
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('in_progress', 'En préparation'),
        ('ready', 'Prête'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]
    
    # Identifiant unique de commande
    order_number = models.CharField(
        max_length=50,
        unique=True,
        editable=False,
        verbose_name="Numéro de commande"
    )
    
    # Informations client
    customer_name = models.CharField(
        max_length=200,
        verbose_name="Nom du client"
    )
    customer_phone = models.CharField(
        max_length=20,
        verbose_name="Téléphone"
    )
    
    # Détails de la commande
    cake_type = models.ForeignKey(
        CakeType,
        on_delete=models.PROTECT,
        verbose_name="Type de gâteau"
    )
    custom_message = models.TextField(
        blank=True,
        verbose_name="Message personnalisé"
    )
    
    # Livraison
    delivery_date = models.DateField(
        verbose_name="Date de livraison"
    )
    delivery_address = models.TextField(
        verbose_name="Adresse de livraison"
    )
    
    # Prix et paiement
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prix total (FCFA)"
    )
    
    # Statut
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="Statut"
    )
    
    # Ticket JPG
    ticket_path = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Chemin du ticket JPG"
    )
    
    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Date de modification"
    )
    
    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Commande {self.order_number} - {self.customer_name}"
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            # Génération du numéro de commande unique
            self.order_number = f"MG-{uuid.uuid4().hex[:8].upper()}"
        
        if not self.total_price:
            # Utiliser le prix de base du type de gâteau si non spécifié
            self.total_price = self.cake_type.base_price
        
        super().save(*args, **kwargs)
