from django.db import models


class CakeType(models.Model):
    """
    Modèle représentant les différents types de gâteaux disponibles
    """
    CAKE_TYPES = [
        ('birthday', '🎂 Gâteau d\'anniversaire'),
        ('event', '🎉 Gâteau pour événements'),
        ('surprise', '🎁 Gâteau surprise'),
        ('custom', '✨ Gâteau personnalisé'),
        ('wedding', '💍 Gâteau de mariage'),
    ]
    
    name = models.CharField(
        max_length=100,
        verbose_name="Nom du gâteau"
    )
    cake_type = models.CharField(
        max_length=20,
        choices=CAKE_TYPES,
        verbose_name="Type"
    )
    description = models.TextField(
        verbose_name="Description"
    )
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prix de base (FCFA)",
        help_text="Prix indicatif"
    )
    image_url = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="URL de l'image",
        help_text="URL complète de l'image (ex: http://localhost:8000/media/cakes/image.jpg)"
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Disponible"
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
        verbose_name = "Type de gâteau"
        verbose_name_plural = "Types de gâteaux"
        ordering = ['cake_type']
    
    def __str__(self):
        return self.name
