#!/usr/bin/env python
"""
Script pour initialiser la base de données MonGâteau
"""
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongateau.settings')
django.setup()

from django.core.management import call_command

def setup_database():
    """
    Initialise la base de données avec les données de base
    """
    print("🍰 Configuration de la base de données MonGâteau...\n")
    
    # Créer les migrations
    print("📝 Création des migrations...")
    call_command('makemigrations')
    
    # Appliquer les migrations
    print("\n📦 Application des migrations...")
    call_command('migrate')
    
    # Charger les données initiales
    print("\n🎂 Chargement des types de gâteaux...")
    call_command('loaddata', 'initial_cakes.json')
    
    # Créer un superutilisateur (optionnel)
    print("\n👤 Création du compte administrateur...")
    print("Vous pouvez créer un superutilisateur maintenant ou plus tard avec:")
    print("python manage.py createsuperuser")
    
    print("\n✅ Base de données configurée avec succès !")
    print("\n🚀 Vous pouvez maintenant lancer le serveur avec:")
    print("python manage.py runserver")

if __name__ == '__main__':
    setup_database()
