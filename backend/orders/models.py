from django.db import models
from cakes.models import CakeType
import uuid


class CustomCakeRequest(models.Model):
    """
    Demande de gâteau sur mesure (pré-commande)
    """
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('reviewed', 'Examinée'),
        ('approved', 'Approuvée'),
        ('rejected', 'Rejetée'),
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

    admin_notes = models.TextField(
        blank=True,
        verbose_name="Notes administratives"
    )

    # Soft delete
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="Supprimée"
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date de suppression"
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
    
    # Soft delete
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="Supprimée"
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date de suppression"
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


class AdminProfile(models.Model):
    """
    Profil administrateur (singleton)
    """
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    password_hash = models.CharField(max_length=128, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profil administrateur"
        verbose_name_plural = "Profil administrateur"

    def set_password(self, raw_password: str):
        from django.contrib.auth.hashers import make_password
        self.password_hash = make_password(raw_password)

    def __str__(self):
        return self.full_name


class AdminSettings(models.Model):
    """
    Paramètres administrateur (singleton)
    """
    store_name = models.CharField(max_length=200, default='MonGâteau')
    store_phone = models.CharField(max_length=50, default='+241 07 40 13 02')
    store_email = models.EmailField(default='mpigajesse23@gmail.com')
    store_address = models.TextField(default='Libreville, Gabon')

    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=True)
    order_notifications = models.BooleanField(default=True)

    min_order_days = models.PositiveIntegerField(default=2)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    items_per_page = models.PositiveIntegerField(default=10)
    default_currency = models.CharField(max_length=20, default='FCFA')
    language = models.CharField(max_length=10, default='fr')

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Paramètres administrateur"
        verbose_name_plural = "Paramètres administrateur"

    def __str__(self):
        return "Paramètres administrateur"
