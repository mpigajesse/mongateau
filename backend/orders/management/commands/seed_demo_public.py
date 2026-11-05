"""`seed_demo_public` — données fictives de la démo en ligne (portfolio).

- les 5 gâteaux du catalogue (fixture initial_cakes.json) ;
- un profil et des réglages boutique FICTIFS : les valeurs par défaut du code
  contiennent le vrai téléphone et le vrai e-mail, qu'une démo publique ne doit
  pas exposer via /api/admin/profile/ et /api/admin/settings/ ;
- une dizaine de commandes et deux demandes sur mesure fictives, avec leur ticket.

Idempotente : si des commandes existent déjà, seuls profil et réglages sont
réécrits. Sur Render, la base SQLite est éphémère : la démo revient à cet état
à chaque réveil du service.
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import Any

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from cakes.models import CakeType
from orders.models import AdminProfile, AdminSettings, CustomCakeRequest, Order
from orders.ticket_generator import generate_order_ticket

CLIENTS = [
    ("Client Démo A", "00000001", "Quartier fictif A, Libreville"),
    ("Client Démo B", "00000002", "Quartier fictif B, Libreville"),
    ("Client Démo C", "00000003", "Quartier fictif C, Owendo"),
    ("Client Démo D", "00000004", "Quartier fictif D, Akanda"),
    ("Client Démo E", "00000005", "Quartier fictif E, Libreville"),
]
STATUTS = ["pending", "confirmed", "in_progress", "ready", "delivered", "delivered", "cancelled", "pending", "confirmed", "delivered"]
MESSAGES = ["Joyeux anniversaire !", "Félicitations aux mariés", "", "Bon courage pour la suite", "Bienvenue bébé"]


class Command(BaseCommand):
    help = "Crée les données fictives de la démo publique (idempotent)."

    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> None:
        if not CakeType.objects.exists():
            call_command("loaddata", "initial_cakes", verbosity=0)

        AdminProfile.objects.update_or_create(id=1, defaults={
            "full_name": "Gérante (démo)", "email": "contact@mongateau-demo.example",
            "phone": "00 00 00 00", "address": "Adresse fictive, Libreville",
        })
        AdminSettings.objects.update_or_create(id=1, defaults={
            "store_name": "MonGâteau (démo)", "store_phone": "00 00 00 00",
            "store_email": "contact@mongateau-demo.example", "store_address": "Libreville (adresse fictive)",
        })

        if Order.objects.exists():
            self.stdout.write("Démo déjà en place : profil et réglages remis à jour.")
            return

        gateaux = list(CakeType.objects.order_by("id"))
        aujourd_hui = date.today()
        for i, statut in enumerate(STATUTS):
            nom, tel, adresse = CLIENTS[i % len(CLIENTS)]
            commande = Order.objects.create(
                customer_name=nom, customer_phone=tel, delivery_address=adresse,
                cake_type=gateaux[i % len(gateaux)], custom_message=MESSAGES[i % len(MESSAGES)],
                delivery_date=aujourd_hui + timedelta(days=(i - 4) * 3), status=statut,
            )
            try:
                commande.ticket_path = generate_order_ticket(commande)
                commande.save()
            except Exception as erreur:  # le ticket n'empêche pas la démo de démarrer
                self.stderr.write(f"Ticket non généré pour {commande.order_number} : {erreur}")

        for nom, tel, _ in CLIENTS[:2]:
            CustomCakeRequest.objects.create(
                customer_name=nom, customer_phone=tel,
                delivery_date=aujourd_hui + timedelta(days=10),
                custom_message="Pièce montée trois étages, thème doré (demande fictive)",
                estimated_budget=75000,
            )

        self.stdout.write(self.style.SUCCESS("Démo publique créée : 5 gâteaux, 10 commandes, 2 demandes sur mesure."))
