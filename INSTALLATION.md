# 📦 Guide d'Installation - MonGâteau

Ce guide vous explique comment installer et lancer l'application MonGâteau sur votre machine.

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.8+** : [Télécharger Python](https://www.python.org/downloads/)
- **Node.js 16+** et **npm** : [Télécharger Node.js](https://nodejs.org/)
- **Git** (optionnel) : [Télécharger Git](https://git-scm.com/)

Pour vérifier les versions installées :

```bash
python --version
node --version
npm --version
```

## 🚀 Installation

### Étape 1 : Cloner ou télécharger le projet

```bash
git clone <url-du-repo>
cd mongateau
```

Ou téléchargez et extrayez le dossier ZIP.

### Étape 2 : Configuration du Backend Django

#### 2.1 Créer un environnement virtuel Python

**Sur Windows :**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

**Sur macOS/Linux :**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

Vous devriez voir `(venv)` apparaître dans votre terminal.

#### 2.2 Installer les dépendances Python

```bash
pip install -r requirements.txt
```

#### 2.3 Configurer la base de données PostgreSQL

**Important** : Assurez-vous que PostgreSQL est installé et que la base `mongateau` existe.

**Configuration actuelle** :
- Base de données : `mongateau`
- Utilisateur : `postgres`
- Mot de passe : `admin`
- Host : `localhost`
- Port : `5432`

**Méthode automatique (recommandée)** :

```bash
python setup_postgres.py
```

Ce script va :
- Tester la connexion à PostgreSQL
- Créer et appliquer les migrations
- Charger les 5 types de gâteaux
- Proposer de créer un superutilisateur

**Méthode manuelle** :

```bash
# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Charger les données initiales (types de gâteaux)
python manage.py loaddata cakes/fixtures/initial_cakes.json
```

📘 **Guide complet PostgreSQL** : Voir [CONFIGURATION_POSTGRESQL.md](../CONFIGURATION_POSTGRESQL.md)

#### 2.4 Créer un compte administrateur (optionnel)

```bash
python manage.py createsuperuser
```

Suivez les instructions pour créer un compte admin.

#### 2.5 Lancer le serveur Django

```bash
python manage.py runserver
```

Le backend sera accessible sur **http://localhost:8000**

✅ **Backend prêt !** Laissez ce terminal ouvert.

---

### Étape 3 : Configuration du Frontend React

Ouvrez un **nouveau terminal** et naviguez vers le dossier frontend :

```bash
cd frontend
```

#### 3.1 Installer les dépendances npm

```bash
npm install
```

Cette étape peut prendre quelques minutes.

#### 3.2 Lancer l'application React

```bash
npm start
```

Le frontend sera accessible sur **http://localhost:3000**

✅ **Frontend prêt !** L'application devrait s'ouvrir automatiquement dans votre navigateur.

---

## 🎯 Vérification de l'installation

1. **Backend API** : Ouvrez http://localhost:8000/api/cakes/types/ dans votre navigateur
   - Vous devriez voir la liste des 5 types de gâteaux en JSON

2. **Frontend** : Ouvrez http://localhost:3000
   - Vous devriez voir la page d'accueil de MonGâteau

3. **Admin Django** : Ouvrez http://localhost:8000/admin
   - Connectez-vous avec le compte superuser créé

---

## 🛠️ Commandes utiles

### Backend

```bash
# Activer l'environnement virtuel
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Lancer le serveur
python manage.py runserver

# Créer des migrations après modification des modèles
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Ouvrir le shell Django
python manage.py shell
```

### Frontend

```bash
# Installer les dépendances
npm install

# Lancer en mode développement
npm start

# Créer une version de production
npm run build

# Lancer les tests
npm test
```

---

## 📂 Structure des dossiers

```
mongateau/
├── backend/                    # Application Django
│   ├── mongateau/             # Configuration principale
│   ├── cakes/                 # App gestion des gâteaux
│   ├── orders/                # App gestion des commandes
│   ├── tickets/               # Tickets PDF générés
│   ├── manage.py              # Script de gestion Django
│   └── requirements.txt       # Dépendances Python
│
├── frontend/                   # Application React
│   ├── public/                # Fichiers publics
│   ├── src/                   # Code source
│   │   ├── components/        # Composants React
│   │   ├── services/          # Services API
│   │   └── types/             # Types TypeScript
│   ├── package.json           # Dépendances npm
│   └── tsconfig.json          # Configuration TypeScript
│
├── README.md                   # Documentation principale
└── INSTALLATION.md            # Ce fichier
```

---

## 🐛 Résolution de problèmes

### Le serveur Django ne démarre pas

- Vérifiez que l'environnement virtuel est activé
- Vérifiez que toutes les dépendances sont installées : `pip install -r requirements.txt`
- Vérifiez les migrations : `python manage.py migrate`

### Le frontend React affiche des erreurs

- Supprimez `node_modules` et réinstallez : `rm -rf node_modules && npm install`
- Vérifiez que le backend est lancé sur le port 8000
- Vérifiez la console du navigateur pour les erreurs CORS

### Erreur CORS (Cross-Origin)

Le backend est configuré pour accepter les requêtes depuis `http://localhost:3000`.
Si vous utilisez un autre port, modifiez `CORS_ALLOWED_ORIGINS` dans `backend/mongateau/settings.py`.

### Les tickets PDF ne se génèrent pas

- Vérifiez que ReportLab est installé : `pip install reportlab`
- Vérifiez que le dossier `backend/tickets/` existe
- Consultez les logs du serveur Django pour les erreurs

---

## 🔧 Configuration avancée

### Changer le port du backend

```bash
python manage.py runserver 8080
```

N'oubliez pas de mettre à jour `API_BASE_URL` dans `frontend/src/services/api.ts`.

### Variables d'environnement

Créez un fichier `.env` dans le dossier `backend/` :

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 📝 Prochaines étapes

Une fois l'installation réussie :

1. Explorez l'interface admin Django : http://localhost:8000/admin
2. Testez la création d'une commande sur le frontend
3. Vérifiez la génération du ticket PDF
4. Personnalisez les types de gâteaux dans l'admin

---

## 💡 Support

Pour toute question ou problème :
- Consultez la documentation : `README.md`
- Vérifiez les logs du serveur Django et de React
- Contactez le support technique

---

**Propriétaire : NAOMIE MOUSSAVOU**

Bon développement ! 🍰
