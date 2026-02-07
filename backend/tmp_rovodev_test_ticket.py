"""
Script de test pour générer un exemple de ticket JPG
"""
import os
import sys
import django

# Configurer Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongateau.settings')
django.setup()

from orders.models import Order
from orders.ticket_generator import generate_order_ticket

# Récupérer la dernière commande ou en créer une pour le test
try:
    order = Order.objects.latest('created_at')
    print(f"✅ Commande trouvée: {order.order_number}")
    print(f"   Client: {order.customer_name}")
    print(f"   Gâteau: {order.cake_type.name}")
    print(f"   Prix: {order.total_price} FCFA")
    print(f"   Livraison: {order.delivery_date}")
    
    # Générer le ticket
    print("\n🎨 Génération du ticket JPG premium...")
    ticket_path = generate_order_ticket(order)
    
    print(f"\n✅ Ticket généré avec succès!")
    print(f"   Chemin: {ticket_path}")
    print(f"\n💡 Ouvrez le fichier pour voir le design premium avec QR code!")
    
    # Mettre à jour le chemin du ticket dans la commande
    order.ticket_path = ticket_path
    order.save()
    print(f"   Ticket path sauvegardé dans la base de données")
    
except Order.DoesNotExist:
    print("❌ Aucune commande trouvée dans la base de données.")
    print("   Créez d'abord une commande via l'interface web.")
except Exception as e:
    print(f"❌ Erreur: {e}")
    import traceback
    traceback.print_exc()
