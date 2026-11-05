# 📌 Aide-Mémoire MonGâteau

Guide rapide des commandes essentielles pour MonGâteau.

---

## 🎯 Configuration PostgreSQL

### Vos Credentials
```
Base de données : mongateau
Utilisateur     : postgres
Mot de passe    : admin
Host            : localhost
Port            : 5432
```

### Vérifier PostgreSQL
1. Ouvrir **pgAdmin 4**
2. Se connecter au serveur PostgreSQL
3. Vérifier que la base **mongateau** existe
4. Si elle n'existe pas : Clic droit sur **Databases** → **Create** → **Database** → Nom : `mongateau`

---

## ⚡ Démarrage Rapide

### Première Fois (Configuration Initiale)

**Terminal 1 - Backend :**
```bash
cd backend
python -m venv venv
venv\Scripts\activate                # Windows
pip install -r requirements.txt
python setup_postgres.py             # Configure tout automatiquement
python manage.py runserver
```

**Terminal 2 - Frontend :**
```bash
cd frontend
npm install
npm start
```

### Fois Suivantes (Démarrage Normal)

**Méthode 1 - Scripts Automatiques (Windows) :**
```bash
# Terminal 1
cd backend
start_backend.bat

# Terminal 2
cd frontend
start_frontend.bat
```

**Méthode 2 - Manuelle :**
```bash
# Terminal 1 - Backend
cd backend
venv\Scripts\activate
python manage.py runserver

# Terminal 2 - Frontend
cd frontend
npm start
```

---

## 🌐 URLs Importantes

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend** | http://localhost:3000 | Interface client |
| **Backend API** | http://localhost:8000 | API REST |
| **Admin Django** | http://localhost:8000/admin | Interface admin |
| **API Gâteaux** | http://localhost:8000/api/cakes/types/ | Liste des gâteaux |
| **API Commandes** | http://localhost:8000/api/orders/ | Commandes |

---

## 💻 Commandes Backend (Django)

### Gestion Environnement
```bash
# Activer l'environnement virtuel
cd backend
venv\Scripts\activate              # Windows
source venv/bin/activate           # macOS/Linux

# Désactiver
deactivate
```

### Base de Données
```bash
# Configuration complète auto
python setup_postgres.py

# Créer des migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Charger les gâteaux
python manage.py loaddata cakes/fixtures/initial_cakes.json

# Réinitialiser la BDD (ATTENTION: supprime tout!)
python manage.py flush
```

### Administration
```bash
# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver

# Lancer sur un autre port
python manage.py runserver 8080

# Shell Django
python manage.py shell

# Shell PostgreSQL
python manage.py dbshell
```

### Vérifications
```bash
# Voir les migrations appliquées
python manage.py showmigrations

# Tester la connexion PostgreSQL
python -c "import django; django.setup(); from django.db import connection; connection.ensure_connection(); print('OK')"
```

---

## 🎨 Commandes Frontend (React)

### Installation
```bash
cd frontend
npm install                   # Installer les dépendances
```

### Développement
```bash
npm start                     # Lancer en mode dev (localhost:3000)
npm run build                 # Build de production
npm test                      # Lancer les tests
```

### Nettoyage
```bash
# Réinstaller les dépendances
rm -rf node_modules
npm install

# Windows
rmdir /s /q node_modules
npm install
```

---

## 🗄️ Gestion PostgreSQL

### Via pgAdmin
```
1. Sauvegarder : Clic droit sur 'mongateau' → Backup
2. Restaurer   : Clic droit sur 'mongateau' → Restore
3. Requêtes    : Clic droit sur 'mongateau' → Query Tool
```

### Via Django
```bash
# Sauvegarder toutes les données
python manage.py dumpdata > backup.json

# Sauvegarder uniquement les commandes
python manage.py dumpdata orders > backup_orders.json

# Restaurer
python manage.py loaddata backup.json
```

### Requêtes Utiles (pgAdmin Query Tool)
```sql
-- Voir toutes les commandes
SELECT * FROM orders_order;

-- Voir tous les gâteaux
SELECT * FROM cakes_caketype;

-- Compter les commandes par statut
SELECT status, COUNT(*) FROM orders_order GROUP BY status;

-- Commandes du jour
SELECT * FROM orders_order WHERE DATE(created_at) = CURRENT_DATE;

-- Chiffre d'affaires total (commandes livrées)
SELECT SUM(total_price) FROM orders_order WHERE status = 'delivered';
```

---

## 🎂 Gestion des Gâteaux (Admin)

### Ajouter un nouveau gâteau
1. http://localhost:8000/admin
2. Connexion
3. **Gâteaux** → **Types de gâteaux** → **Ajouter**
4. Remplir : nom, type, description, prix, URL image
5. Cocher **Disponible**
6. **Enregistrer**

### Modifier un gâteau
1. **Gâteaux** → **Types de gâteaux**
2. Cliquer sur le gâteau
3. Modifier
4. **Enregistrer**

### Désactiver temporairement
1. Cliquer sur le gâteau
2. Décocher **Disponible**
3. **Enregistrer**

---

## 📦 Gestion des Commandes (Admin)

### Voir les commandes
http://localhost:8000/admin → **Commandes** → **Commandes**

### Filtrer
- Par **statut** (colonne droite)
- Par **date de livraison**
- Par **type de gâteau**

### Rechercher
Barre de recherche : numéro de commande, nom client, téléphone

### Changer le statut
1. Ouvrir la commande
2. Changer **Statut**
3. **Enregistrer**

### Workflow recommandé
```
En attente → Confirmée → En préparation → Prête → Livrée
```

---

## 🐛 Résolution Problèmes Courants

### Backend ne démarre pas

**Erreur PostgreSQL :**
```bash
# Vérifier que PostgreSQL est démarré
# Windows : Services → PostgreSQL → Démarrer

# Tester la connexion
python setup_postgres.py
```

**Erreur "No module named..." :**
```bash
# Réinstaller les dépendances
pip install -r requirements.txt
```

**Erreur migrations :**
```bash
python manage.py migrate
```

### Frontend ne démarre pas

**Port 3000 occupé :**
```bash
# Le frontend proposera automatiquement le port 3001
# OU modifier API_BASE_URL dans src/services/api.ts
```

**Erreur CORS :**
```
Vérifier que le backend est lancé sur localhost:8000
Vérifier CORS_ALLOWED_ORIGINS dans backend/mongateau/settings.py
```

**Modules manquants :**
```bash
npm install
```

### Ticket PDF ne se génère pas

```bash
# Vérifier ReportLab
pip install reportlab

# Vérifier le dossier tickets existe
# Il se crée automatiquement au démarrage du serveur
```

### Base de données vide

```bash
# Charger les gâteaux
python manage.py loaddata cakes/fixtures/initial_cakes.json
```

---

## 📊 Statistiques Rapides (pgAdmin)

### Nombre de commandes
```sql
SELECT COUNT(*) FROM orders_order;
```

### Commandes par type de gâteau
```sql
SELECT c.name, COUNT(o.id) as total
FROM cakes_caketype c
LEFT JOIN orders_order o ON o.cake_type_id = c.id
GROUP BY c.name;
```

### Revenu total
```sql
SELECT SUM(total_price) as revenu_total
FROM orders_order
WHERE status = 'delivered';
```

### Commandes à livrer aujourd'hui
```sql
SELECT * FROM orders_order
WHERE delivery_date = CURRENT_DATE
AND status != 'delivered';
```

---

## 🔑 Credentials par Défaut

### PostgreSQL
```
User     : postgres
Password : admin
```

### Django Admin
À créer avec :
```bash
python manage.py createsuperuser
```

---

## 📁 Fichiers Importants

### Configuration
- `backend/mongateau/settings.py` - Configuration Django
- `backend/requirements.txt` - Dépendances Python
- `frontend/package.json` - Dépendances npm
- `frontend/src/services/api.ts` - Configuration API

### Données
- `backend/cakes/fixtures/initial_cakes.json` - 5 types de gâteaux
- `backend/tickets/` - Tickets PDF générés

### Scripts
- `backend/setup_postgres.py` - Configuration auto PostgreSQL
- `backend/start_backend.bat` - Démarrage Windows
- `frontend/start_frontend.bat` - Démarrage Windows

---

## 📚 Documentation

| Fichier | Contenu |
|---------|---------|
| **START_HERE.md** | 👉 **COMMENCEZ ICI** |
| **QUICKSTART.md** | Démarrage rapide 5 min |
| **INSTALLATION.md** | Installation complète |
| **CONFIGURATION_POSTGRESQL.md** | Guide PostgreSQL |
| **GUIDE_UTILISATION.md** | Guide utilisateur |
| **FONCTIONNALITES.md** | Fonctionnalités détaillées |
| **RESUME_PROJET.md** | Résumé complet |
| **AIDE_MEMOIRE.md** | ⭐ Ce fichier |

---

## 🎯 Checklist Démarrage Quotidien

- [ ] PostgreSQL démarré (vérifier pgAdmin)
- [ ] Terminal 1 : Backend lancé (port 8000)
- [ ] Terminal 2 : Frontend lancé (port 3000)
- [ ] Tester : http://localhost:3000
- [ ] Vérifier admin : http://localhost:8000/admin

---

## 💡 Astuces

### Backend
- Gardez le terminal backend ouvert pour voir les requêtes API
- Utilisez l'admin Django pour gérer facilement les données
- Les tickets PDF sont dans `backend/tickets/`

### Frontend
- Rechargement automatique à chaque modification
- Console navigateur (F12) pour voir les erreurs
- React DevTools pour debugger

### PostgreSQL
- pgAdmin pour visualiser les données
- Faites des backups réguliers
- Utilisez Query Tool pour des requêtes rapides

---

## 🆘 En Cas de Problème

1. **Vérifier PostgreSQL** : Ouvert et base `mongateau` existe
2. **Vérifier backend** : Lancé sur port 8000
3. **Vérifier frontend** : Lancé sur port 3000
4. **Consulter logs** : Dans les terminaux
5. **Relancer setup** : `python setup_postgres.py`
6. **Consulter docs** : START_HERE.md, CONFIGURATION_POSTGRESQL.md

---

**MonGâteau**

🍰 **MonGâteau** - Gardez ce fichier à portée de main !
