# 🍰 MonGâteau - Application Web de Commande de Gâteaux

Application web moderne pour la commande de gâteaux artisanaux en ligne.

**Propriétaire & Créatrice :** NAOMIE MOUSSAVOU

## 🚀 Fonctionnalités

- ✨ Commande rapide sans création de compte
- 🎂 5 types de gâteaux disponibles
- 📄 Génération automatique de ticket PDF
- 💵 Paiement à la livraison
- 📱 Interface responsive (mobile & desktop)

## 🛠️ Technologies

**Backend:**
- Django 4.2+
- Django REST Framework
- **PostgreSQL** (base de données)
- ReportLab (génération PDF)
- psycopg2 (adaptateur PostgreSQL)

**Frontend:**
- React 18+
- TypeScript
- Axios
- CSS moderne

## 📦 Installation

### Backend (Django)

**Prérequis** : PostgreSQL installé avec la base de données `mongateau` créée.

```bash
cd backend

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances (inclut psycopg2 pour PostgreSQL)
pip install -r requirements.txt

# Configuration automatique de la base de données PostgreSQL
python setup_postgres.py

# OU manuellement :
python manage.py migrate
python manage.py loaddata cakes/fixtures/initial_cakes.json
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

📘 **Guide PostgreSQL complet** : Voir [CONFIGURATION_POSTGRESQL.md](CONFIGURATION_POSTGRESQL.md)

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

L'application sera accessible sur:
- Backend API: http://localhost:8000
- Frontend: http://localhost:3000

## 📖 Structure du projet

```
mongateau/
├── backend/                      # Django Backend
│   ├── mongateau/               # Configuration principale
│   │   ├── settings.py          # Configuration Django
│   │   ├── urls.py              # Routes principales
│   │   └── wsgi.py
│   ├── cakes/                   # App gestion gâteaux
│   │   ├── models.py            # Modèle CakeType
│   │   ├── serializers.py       # Serializers API
│   │   ├── views.py             # ViewSets
│   │   ├── admin.py             # Interface admin
│   │   └── fixtures/            # Données initiales
│   ├── orders/                  # App gestion commandes
│   │   ├── models.py            # Modèle Order
│   │   ├── serializers.py       # Serializers API
│   │   ├── views.py             # ViewSets
│   │   ├── pdf_generator.py     # Génération PDF
│   │   └── admin.py             # Interface admin
│   ├── tickets/                 # PDFs générés
│   ├── requirements.txt         # Dépendances Python
│   ├── manage.py                # Script Django
│   └── start_backend.bat/sh     # Scripts de démarrage
│
├── frontend/                    # React Frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/          # Composants React
│   │   │   ├── HomePage.tsx
│   │   │   ├── CakeList.tsx
│   │   │   ├── OrderForm.tsx
│   │   │   └── OrderConfirmation.tsx
│   │   ├── services/
│   │   │   └── api.ts           # Services API
│   │   ├── types/
│   │   │   └── index.ts         # Types TypeScript
│   │   ├── App.tsx              # Composant principal
│   │   └── index.tsx            # Point d'entrée
│   ├── package.json             # Dépendances npm
│   ├── tsconfig.json            # Config TypeScript
│   └── start_frontend.bat/sh    # Scripts de démarrage
│
├── README.md                    # Documentation principale
├── INSTALLATION.md              # Guide d'installation
├── GUIDE_UTILISATION.md         # Guide utilisateur
├── QUICKSTART.md                # Démarrage rapide
└── .gitignore                   # Fichiers ignorés
```

## 🎯 Utilisation

1. Le client consulte les gâteaux disponibles
2. Remplit le formulaire de commande
3. Valide et télécharge son ticket PDF
4. Paie à la livraison

## 📝 License

Propriété de NAOMIE MOUSSAVOU - Tous droits réservés
