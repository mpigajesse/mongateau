from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCakeRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(editable=False, max_length=50, unique=True, verbose_name='Numéro de demande')),
                ('customer_name', models.CharField(max_length=200, verbose_name='Nom du client')),
                ('customer_phone', models.CharField(max_length=20, verbose_name='Téléphone')),
                ('delivery_date', models.DateField(verbose_name='Date souhaitée')),
                ('custom_message', models.TextField(blank=True, verbose_name='Message ou détails')),
                ('estimated_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Budget estimé (FCFA)')),
                ('status', models.CharField(choices=[('pending', 'En attente'), ('contacted', 'Contacté'), ('quoted', 'Devis envoyé'), ('approved', 'Validé'), ('cancelled', 'Annulé')], default='pending', max_length=20, verbose_name='Statut')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'verbose_name': 'Demande gâteau sur mesure',
                'verbose_name_plural': 'Demandes gâteaux sur mesure',
                'ordering': ['-created_at'],
            },
        ),
    ]
