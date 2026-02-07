#!/usr/bin/env python
"""
Script pour configurer la base de données PostgreSQL MonGâteau
"""
import os
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongateau.settings')
django.setup()

from django.core.management import call_command
from django.db import connection

def test_connection():
    """Test la connexion à PostgreSQL"""
    try:
        connection.ensure_connection()
        print("✅ Connexion à PostgreSQL réussie !")
        print(f"   Base de données : {connection.settings_dict['NAME']}")
        print(f"   Utilisateur : {connection.settings_dict['USER']}")
        print(f"   Hôte : {connection.settings_dict['HOST']}")
        print(f"   Port : {connection.settings_dict['PORT']}")
        return True
    except Exception as e:
        print("❌ Erreur de connexion à PostgreSQL :")
        print(f"   {str(e)}")
        print("\nVérifiez que :")
        print("  1. PostgreSQL est démarré")
        print("  2. La base de données 'mongateau' existe dans pgAdmin")
        print("  3. Les credentials sont corrects (user: postgres, password: admin)")
        return False

def setup_database():
    """
    Initialise la base de données PostgreSQL avec les données de base
    """
    print("=" * 60)
    print("🍰 Configuration de la base de données PostgreSQL - MonGâteau")
    print("=" * 60)
    print()
    
    # Test de connexion
    if not test_connection():
        return
    
    print("\n" + "=" * 60)
    
    # Créer les migrations
    print("\n📝 Création des migrations...")
    try:
        call_command('makemigrations')
        print("✅ Migrations créées avec succès")
    except Exception as e:
        print(f"❌ Erreur lors de la création des migrations : {e}")
        return
    
    # Appliquer les migrations
    print("\n📦 Application des migrations...")
    try:
        call_command('migrate')
        print("✅ Migrations appliquées avec succès")
    except Exception as e:
        print(f"❌ Erreur lors de l'application des migrations : {e}")
        return
    
    # Charger les données initiales
    print("\n🎂 Chargement des types de gâteaux...")
    try:
        call_command('loaddata', 'cakes/fixtures/initial_cakes.json')
        print("✅ 5 types de gâteaux chargés avec succès")
    except Exception as e:
        print(f"❌ Erreur lors du chargement des données : {e}")
        return
    
    # Informations sur le superutilisateur
    print("\n" + "=" * 60)
    print("👤 Création du compte administrateur")
    print("=" * 60)
    print("\nVous pouvez créer un superutilisateur maintenant ou plus tard.")
    print("Commande : python manage.py createsuperuser")
    
    response = input("\nVoulez-vous créer un superutilisateur maintenant ? (o/n) : ")
    if response.lower() in ['o', 'oui', 'y', 'yes']:
        try:
            call_command('createsuperuser')
        except KeyboardInterrupt:
            print("\n⚠️ Création du superutilisateur annulée")
    
    print("\n" + "=" * 60)
    print("✅ Configuration terminée avec succès !")
    print("=" * 60)
    print("\n🚀 Prochaines étapes :")
    print("   1. Lancez le serveur : python manage.py runserver")
    print("   2. Accédez à l'admin : http://localhost:8000/admin")
    print("   3. Testez l'API : http://localhost:8000/api/cakes/types/")
    print("\n🍰 MonGâteau est prêt à être utilisé !")

if __name__ == '__main__':
    try:
        setup_database()
    except KeyboardInterrupt:
        print("\n\n⚠️ Configuration interrompue par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur inattendue : {e}")
