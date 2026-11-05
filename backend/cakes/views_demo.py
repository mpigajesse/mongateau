"""Vitrine de la démo publique (portfolio), servie uniquement si DEMO_PUBLIQUE.

Le frontend React du projet n'est pas versionné dans ce dépôt : sans cette page,
la démo en ligne ne montrerait qu'une API JSON. La vitrine réutilise tels quels
les modèles, le sérialiseur de création de commande et le générateur de ticket :
une commande passée ici suit exactement le même chemin qu'une commande de l'API.
"""

from datetime import date, timedelta

from django.shortcuts import render

from orders.serializers import OrderCreateSerializer
from orders.ticket_generator import generate_order_ticket

from .models import CakeType


def _gateaux():
    return CakeType.objects.filter(is_available=True, is_deleted=False).order_by('base_price')


def vitrine_demo(request):
    return render(request, 'cakes/demo_vitrine.html', {'gateaux': _gateaux()})


def commande_demo(request):
    date_min = date.today() + timedelta(days=2)
    if request.method == 'POST':
        serializer = OrderCreateSerializer(data=request.POST)
        if serializer.is_valid():
            commande = serializer.save()
            try:
                commande.ticket_path = generate_order_ticket(commande)
                commande.save()
            except Exception:  # même tolérance que l'API : la commande reste créée
                pass
            return render(request, 'cakes/demo_confirmation.html', {'commande': commande})
        erreurs = serializer.errors
    else:
        erreurs = {}
    return render(request, 'cakes/demo_commande.html', {
        'gateaux': _gateaux(),
        'erreurs': erreurs,
        'valeurs': request.POST,
        'date_min': date_min.isoformat(),
        'choisi': request.GET.get('gateau', ''),
    })
