"""
Script pour peupler la base de données avec des données initiales de gâteaux.
Télécharge des images depuis Unsplash et crée les entrées dans la base de données.
"""

import os
import sys
import django
import requests
from pathlib import Path

# Configuration Django
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mongateau.settings')
django.setup()

from cakes.models import CakeType

def download_image(url, filename):
    """Télécharge une image depuis une URL et la sauvegarde localement."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Créer le dossier media/cakes s'il n'existe pas
        media_dir = BASE_DIR / 'media' / 'cakes'
        media_dir.mkdir(parents=True, exist_ok=True)
        
        # Sauvegarder l'image
        filepath = media_dir / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        return f'/media/cakes/{filename}'
    except Exception as e:
        print(f"Erreur lors du téléchargement de {url}: {e}")
        return None

def populate_cakes():
    """Peuple la base de données avec des gâteaux."""
    
    # URLs d'images de gâteaux depuis Unsplash (images libres de droits)
    # Chaque gâteau aura une image unique
    cake_images_urls = {
        'birthday': [
            'https://images.unsplash.com/photo-1558636508-e0db3814bd1d?w=800',  # Gâteau chocolat classique
            'https://images.unsplash.com/photo-1587241321921-91a834d82209?w=800',  # Gâteau rainbow
            'https://images.unsplash.com/photo-1535141192574-5d4897c12636?w=800',  # Gâteau premium
            'https://images.unsplash.com/photo-1586985289688-ca3cf47d3e6e?w=800',  # Gâteau caramel
            'https://images.unsplash.com/photo-1578775887804-699de7086ff9?w=800',  # Forêt noire
        ],
        'event': [
            'https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=800',  # Corporate
            'https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?w=800',  # Baptême
            'https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=800',  # Diplôme
            'https://images.unsplash.com/photo-1602351447937-745cb720612f?w=800',  # Fiançailles
            'https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?w=800',  # Fin d'année
        ],
        'surprise': [
            'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800',  # Pinata
            'https://images.unsplash.com/photo-1557925923-cd4648e211a0?w=800',  # Photo
            'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=800',  # Explosion
            'https://images.unsplash.com/photo-1578775887804-699de7086ff9?w=800',  # Trésor
            'https://images.unsplash.com/photo-1571115177098-24ec42ed204d?w=800',  # Géant
        ],
        'custom': [
            'https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=800',  # Sculpture 3D
            'https://images.unsplash.com/photo-1535141192574-5d4897c12636?w=800',  # Thématique enfant
            'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=800',  # Design moderne
            'https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=800',  # Vintage
            'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800',  # Art abstrait
        ],
        'wedding': [
            'https://images.unsplash.com/photo-1519225421980-715cb0215aed?w=800',  # Classique 3 étages
            'https://images.unsplash.com/photo-1594744803329-e58b31de8bf5?w=800',  # Royal
            'https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=800',  # Bohème
            'https://images.unsplash.com/photo-1579372786545-d24232daf58c?w=800',  # Moderne
            'https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?w=800',  # Luxe 5 étages
        ],
    }
    
    cakes_data = [
        {
            'cake_type': 'birthday',
            'name': 'Gâteau d\'Anniversaire Classique',
            'description': 'Un délicieux gâteau au chocolat avec ganache crémeuse, parfait pour célébrer votre anniversaire. Décoré avec élégance et personnalisable selon vos goûts.',
            'base_price': '15000',
        },
        {
            'cake_type': 'birthday',
            'name': 'Gâteau d\'Anniversaire Rainbow',
            'description': 'Gâteau coloré et festif avec plusieurs couches arc-en-ciel. Idéal pour les enfants et les fêtes joyeuses. Garniture vanille légère.',
            'base_price': '18000',
        },
        {
            'cake_type': 'birthday',
            'name': 'Gâteau d\'Anniversaire Premium',
            'description': 'Notre gâteau signature avec couches de génoise, crème pâtissière et fruits frais. Décorations personnalisées incluses.',
            'base_price': '25000',
        },
        {
            'cake_type': 'birthday',
            'name': 'Gâteau d\'Anniversaire au Caramel',
            'description': 'Gâteau moelleux au caramel beurre salé avec glaçage onctueux. Une explosion de saveurs pour les amateurs de douceurs.',
            'base_price': '20000',
        },
        {
            'cake_type': 'birthday',
            'name': 'Gâteau d\'Anniversaire Forêt Noire',
            'description': 'Classique revisité avec génoise au chocolat, cerises et chantilly. Un intemporel qui fait toujours plaisir.',
            'base_price': '22000',
        },
        
        # Gâteaux pour événements
        {
            'cake_type': 'event',
            'name': 'Gâteau Corporate Élégant',
            'description': 'Gâteau professionnel parfait pour les événements d\'entreprise, inaugurations et célébrations corporatives. Design sobre et raffiné.',
            'base_price': '30000',
        },
        {
            'cake_type': 'event',
            'name': 'Gâteau de Baptême',
            'description': 'Gâteau délicat et léger pour célébrer le baptême. Décorations personnalisables avec le prénom de l\'enfant.',
            'base_price': '25000',
        },
        {
            'cake_type': 'event',
            'name': 'Gâteau de Remise de Diplôme',
            'description': 'Célébrez la réussite avec style ! Gâteau thématique avec décorations académiques et couleurs personnalisables.',
            'base_price': '28000',
        },
        {
            'cake_type': 'event',
            'name': 'Gâteau de Fiançailles',
            'description': 'Gâteau romantique pour célébrer vos fiançailles. Décoré avec élégance et touches dorées.',
            'base_price': '35000',
        },
        {
            'cake_type': 'event',
            'name': 'Gâteau de Fête de Fin d\'Année',
            'description': 'Gâteau festif pour célébrer la nouvelle année ou Noël. Saveurs épicées et décorations saisonnières.',
            'base_price': '32000',
        },
        
        # Gâteaux surprise
        {
            'cake_type': 'surprise',
            'name': 'Gâteau Surprise Pinata',
            'description': 'Gâteau surprise avec centre rempli de bonbons et confettis. Moment magique garanti lors de la découpe !',
            'base_price': '22000',
        },
        {
            'cake_type': 'surprise',
            'name': 'Gâteau Surprise Photo',
            'description': 'Gâteau personnalisé avec impression photo comestible. Surprenez vos proches avec leur photo préférée.',
            'base_price': '25000',
        },
        {
            'cake_type': 'surprise',
            'name': 'Gâteau Surprise Explosion',
            'description': 'Gâteau avec effet "explosion" de pépites de chocolat et crème. Un moment spectaculaire !',
            'base_price': '28000',
        },
        {
            'cake_type': 'surprise',
            'name': 'Gâteau Surprise Trésor',
            'description': 'Gâteau cachant une surprise à l\'intérieur (bijou, message, etc.). Livré avec discrétion absolue.',
            'base_price': '30000',
        },
        {
            'cake_type': 'surprise',
            'name': 'Gâteau Surprise Géant',
            'description': 'Grand gâteau surprise pour événements importants. Portions généreuses et effet wow assuré.',
            'base_price': '40000',
        },
        
        # Gâteaux personnalisés
        {
            'cake_type': 'custom',
            'name': 'Gâteau Sculpture 3D',
            'description': 'Gâteau sculpté en forme d\'objet ou personnage de votre choix. Art comestible sur mesure.',
            'base_price': '45000',
        },
        {
            'cake_type': 'custom',
            'name': 'Gâteau Thématique Enfant',
            'description': 'Gâteau personnalisé selon le thème préféré de votre enfant (super-héros, princesse, etc.).',
            'base_price': '35000',
        },
        {
            'cake_type': 'custom',
            'name': 'Gâteau Design Moderne',
            'description': 'Design contemporain et minimaliste. Parfait pour les amateurs d\'esthétique épurée.',
            'base_price': '40000',
        },
        {
            'cake_type': 'custom',
            'name': 'Gâteau Vintage Romantique',
            'description': 'Style rétro avec dentelle comestible et roses en sucre. Élégance intemporelle.',
            'base_price': '42000',
        },
        {
            'cake_type': 'custom',
            'name': 'Gâteau Art Abstrait',
            'description': 'Création artistique unique inspirée de vos couleurs et formes préférées.',
            'base_price': '50000',
        },
        
        # Gâteaux de mariage
        {
            'cake_type': 'wedding',
            'name': 'Gâteau de Mariage Classique 3 Étages',
            'description': 'Élégant gâteau blanc à 3 niveaux avec décorations florales. Jusqu\'à 100 parts.',
            'base_price': '75000',
        },
        {
            'cake_type': 'wedding',
            'name': 'Gâteau de Mariage Royal',
            'description': 'Gâteau majestueux à 4 étages avec détails dorés et perles comestibles. Pour les grandes occasions.',
            'base_price': '120000',
        },
        {
            'cake_type': 'wedding',
            'name': 'Gâteau de Mariage Bohème',
            'description': 'Style naturel et champêtre avec fleurs fraîches et glaçage rustique. Romantique et authentique.',
            'base_price': '85000',
        },
        {
            'cake_type': 'wedding',
            'name': 'Gâteau de Mariage Moderne',
            'description': 'Design contemporain géométrique avec finitions marbre. Chic et sophistiqué.',
            'base_price': '95000',
        },
        {
            'cake_type': 'wedding',
            'name': 'Gâteau de Mariage Luxe 5 Étages',
            'description': 'Notre création la plus prestigieuse. 5 étages ornés de détails exquis. Jusqu\'à 200 parts.',
            'base_price': '150000',
        },
    ]
    
    print("🎂 Début du peuplement de la base de données...")
    print("=" * 60)
    
    # Supprimer les anciennes données
    deleted_count = CakeType.objects.all().delete()[0]
    print(f"✓ {deleted_count} anciennes entrées supprimées")
    
    created_count = 0
    cake_type_counters = {}  # Compteur pour chaque type de gâteau
    
    for cake_data in cakes_data:
        cake_type = cake_data['cake_type']
        
        # Incrémenter le compteur pour ce type
        if cake_type not in cake_type_counters:
            cake_type_counters[cake_type] = 0
        else:
            cake_type_counters[cake_type] += 1
        
        type_index = cake_type_counters[cake_type]
        
        # Télécharger l'image si elle n'existe pas déjà
        image_filename = f'{cake_type}_{type_index + 1}.jpg'
        image_path = BASE_DIR / 'media' / 'cakes' / image_filename
        
        if not image_path.exists() and cake_type in cake_images_urls:
            print(f"📥 Téléchargement de l'image pour {cake_data['name']}...")
            # Utiliser l'URL correspondante à l'index du gâteau dans sa catégorie
            image_url_source = cake_images_urls[cake_type][type_index]
            download_image(image_url_source, image_filename)
        
        # Construire l'URL complète
        if image_path.exists():
            image_url = f'http://localhost:8000/media/cakes/{image_filename}'
        else:
            image_url = None
        
        # Créer l'entrée dans la base de données
        cake = CakeType.objects.create(
            cake_type=cake_data['cake_type'],
            name=cake_data['name'],
            description=cake_data['description'],
            base_price=cake_data['base_price'],
            image_url=image_url,
            is_available=True
        )
        
        created_count += 1
        print(f"✓ Créé: {cake.name} ({cake.get_cake_type_display()}) - {cake.base_price} FCFA")
    
    print("=" * 60)
    print(f"✅ {created_count} gâteaux créés avec succès!")
    print("\n💡 Vous pouvez maintenant:")
    print("   - Démarrer le serveur: python manage.py runserver")
    print("   - Accéder à l'admin: http://localhost:8000/admin")
    print("   - Tester l'API: http://localhost:8000/api/cakes/types/")

if __name__ == '__main__':
    populate_cakes()
