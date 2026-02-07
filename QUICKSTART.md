# ⚡ Démarrage Rapide - MonGâteau

Guide ultra-rapide pour lancer l'application en 5 minutes !

## 🎯 En bref

**MonGâteau** est une application complète de commande de gâteaux :
- **Backend** : Django + Django REST Framework
- **Frontend** : React + TypeScript
- **Fonctionnalités** : Commande sans compte, génération de ticket PDF, paiement à la livraison

---

## 🚀 Installation en 4 étapes

### 1️⃣ Backend Django

**Important** : Assurez-vous que PostgreSQL est démarré et que la base `mongateau` existe.

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

# Configuration PostgreSQL automatique
python setup_postgres.py

# Lancer le serveur
python manage.py runserver
```

✅ Backend lancé sur **http://localhost:8000**

**Base de données PostgreSQL** :
- Nom : `mongateau`
- User : `postgres`
- Password : `admin`
- Host : `localhost`
- Port : `5432`

### 2️⃣ Frontend React (nouveau terminal)

```bash
cd frontend
npm install
npm start
```

✅ Frontend lancé sur **http://localhost:3000**

---

## 🎮 Scripts de démarrage rapide

### Windows

**Backend :**
```bash
cd backend
start_backend.bat
```

**Frontend :**
```bash
cd frontend
start_frontend.bat
```

### macOS/Linux

**Backend :**
```bash
cd backend
chmod +x start_backend.sh
./start_backend.sh
```

**Frontend :**
```bash
cd frontend
chmod +x start_frontend.sh
./start_frontend.sh
```

---

## 🧪 Tester l'application

1. **Page d'accueil** : http://localhost:3000
2. **API Gâteaux** : http://localhost:8000/api/cakes/types/
3. **Admin Django** : http://localhost:8000/admin

### Parcours test complet

1. Ouvrir http://localhost:3000
2. Cliquer sur "Commander un gâteau"
3. Choisir un type de gâteau
4. Remplir le formulaire :
   - Nom : Test Client
   - Téléphone : 06 12 34 56 78
   - Date : (dans 3 jours)
   - Adresse : 123 Rue Test, Libreville
   - Message : Gâteau de test
5. Valider la commande
6. Télécharger le ticket PDF
7. Vérifier la commande dans l'admin Django

---

## 📁 Structure du projet

```
mongateau/
├── backend/              # Django (API + Admin)
│   ├── cakes/           # Gestion des types de gâteaux
│   ├── orders/          # Gestion des commandes
│   └── tickets/         # PDFs générés
├── frontend/            # React (Interface client)
│   └── src/
│       ├── components/  # Composants UI
│       └── services/    # API services
└── docs/                # Documentation
```

---

## 🔑 Points clés

### API Endpoints

**Gâteaux :**
- `GET /api/cakes/types/` - Liste des gâteaux
- `GET /api/cakes/types/{id}/` - Détails d'un gâteau

**Commandes :**
- `POST /api/orders/` - Créer une commande
- `GET /api/orders/{id}/` - Détails d'une commande
- `GET /api/orders/{id}/download-ticket/` - Télécharger le ticket PDF
- `GET /api/orders/{id}/status/` - Statut d'une commande

### Données initiales

5 types de gâteaux sont pré-configurés :
1. 🎂 Gâteau d'anniversaire - 15 000 FCFA
2. 🎉 Gâteau pour événements - 20 000 FCFA
3. 🎁 Gâteau surprise - 18 000 FCFA
4. ✨ Gâteau personnalisé - 25 000 FCFA
5. 💍 Gâteau de mariage - 50 000 FCFA

---

## 🛠️ Commandes utiles

### Django

```bash
# Créer un admin
python manage.py createsuperuser

# Reset la base de données
python manage.py flush

# Recharger les données initiales
python manage.py loaddata cakes/fixtures/initial_cakes.json

# Shell Django
python manage.py shell
```

### React

```bash
# Build de production
npm run build

# Tests
npm test

# Nettoyer et réinstaller
rm -rf node_modules && npm install
```

---

## 🐛 Problèmes fréquents

### Port 8000 déjà utilisé
```bash
python manage.py runserver 8080
```
Puis modifiez `API_BASE_URL` dans `frontend/src/services/api.ts`.

### Erreur CORS
Vérifiez que le backend est lancé et que `CORS_ALLOWED_ORIGINS` dans `settings.py` inclut `http://localhost:3000`.

### Ticket PDF ne se génère pas
- Vérifiez que ReportLab est installé : `pip install reportlab`
- Créez le dossier manuellement : `mkdir backend/tickets`

---

## 📚 Documentation complète

- **Installation détaillée** : [INSTALLATION.md](INSTALLATION.md)
- **Guide utilisateur** : [GUIDE_UTILISATION.md](GUIDE_UTILISATION.md)
- **README principal** : [README.md](README.md)

---

## 🎨 Personnalisation rapide

### Changer les couleurs

**Frontend** : Modifiez les gradients dans les fichiers CSS
- Rose principal : `#FF6B9D`
- Violet : `#667eea` et `#764ba2`

### Ajouter un type de gâteau

1. Accédez à http://localhost:8000/admin
2. Gâteaux → Types de gâteaux → Ajouter
3. Remplissez le formulaire et enregistrez

### Modifier les prix

Dans l'admin Django, éditez le "Prix de base" de chaque type de gâteau.

---

## ✨ Fonctionnalités principales

### Côté Client
- ✅ Navigation simple (accueil → gâteaux → commande → confirmation)
- ✅ Pas de compte requis
- ✅ Formulaire de commande avec validation
- ✅ Génération de ticket PDF
- ✅ Interface responsive (mobile + desktop)

### Côté Admin
- ✅ Interface Django Admin
- ✅ Gestion des types de gâteaux
- ✅ Gestion des commandes
- ✅ Changement de statut
- ✅ Filtres et recherche
- ✅ Tickets PDF stockés

---

## 🚢 Déploiement

Pour déployer en production, consultez :
- Backend : Heroku, DigitalOcean, AWS
- Frontend : Vercel, Netlify, GitHub Pages
- Base de données : PostgreSQL recommandé

---

## 💡 Aide

**Besoin d'aide ?**
- Consultez [INSTALLATION.md](INSTALLATION.md) pour plus de détails
- Vérifiez les logs du serveur Django
- Ouvrez la console du navigateur (F12)

---

**Propriétaire : NAOMIE MOUSSAVOU**

🍰 **MonGâteau** - Commander un gâteau devient un plaisir simple, rapide et gourmand !
