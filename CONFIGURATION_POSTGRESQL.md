# 🐘 Configuration PostgreSQL - MonGâteau

Guide pour configurer l'application MonGâteau avec PostgreSQL.

## 📋 Prérequis

- **PostgreSQL** installé sur votre PC
- **pgAdmin** pour la gestion (déjà configuré)
- Base de données créée : `mongateau`
- Utilisateur : `postgres`
- Mot de passe : `admin`
- Port : `5432` (par défaut)

---

## ✅ Configuration actuelle

L'application est **déjà configurée** pour utiliser votre base de données PostgreSQL locale :

### Paramètres de connexion

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mongateau',        # Nom de la base de données
        'USER': 'postgres',          # Utilisateur PostgreSQL
        'PASSWORD': 'admin',         # Mot de passe
        'HOST': 'localhost',         # Serveur local
        'PORT': '5432',              # Port par défaut
    }
}
```

Ces paramètres sont déjà configurés dans `backend/mongateau/settings.py`.

---

## 🚀 Installation et Configuration

### Étape 1 : Vérifier PostgreSQL

Assurez-vous que PostgreSQL est démarré :

1. Ouvrez **pgAdmin 4**
2. Connectez-vous à votre serveur PostgreSQL
3. Vérifiez que la base de données **mongateau** existe

### Étape 2 : Créer la base de données (si nécessaire)

Si la base `mongateau` n'existe pas encore dans pgAdmin :

1. Dans pgAdmin, clic droit sur **Databases**
2. **Create** → **Database**
3. **Database name** : `mongateau`
4. **Owner** : `postgres`
5. Cliquez sur **Save**

### Étape 3 : Installer les dépendances Python

```bash
cd backend

# Activer l'environnement virtuel
# Windows :
venv\Scripts\activate

# macOS/Linux :
source venv/bin/activate

# Installer les dépendances (inclut psycopg2)
pip install -r requirements.txt
```

**Note** : `psycopg2-binary` est l'adaptateur PostgreSQL pour Python, déjà ajouté aux requirements.

### Étape 4 : Configurer la base de données

Utilisez le script automatisé :

```bash
python setup_postgres.py
```

Ce script va :
- ✅ Tester la connexion à PostgreSQL
- ✅ Créer les migrations
- ✅ Appliquer les migrations (créer les tables)
- ✅ Charger les 5 types de gâteaux
- ✅ Proposer de créer un superutilisateur

**OU** manuellement :

```bash
# Tester la connexion
python manage.py dbshell

# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Charger les données initiales
python manage.py loaddata cakes/fixtures/initial_cakes.json

# Créer un superutilisateur
python manage.py createsuperuser
```

---

## 🔍 Vérification

### 1. Vérifier les tables dans pgAdmin

1. Ouvrez pgAdmin
2. Naviguez vers : **Servers** → **PostgreSQL** → **Databases** → **mongateau** → **Schemas** → **public** → **Tables**

Vous devriez voir les tables :
- `cakes_caketype` (5 types de gâteaux)
- `orders_order` (commandes)
- `django_migrations`
- `auth_user`
- etc.

### 2. Vérifier les données

Dans pgAdmin, clic droit sur `cakes_caketype` → **View/Edit Data** → **All Rows**

Vous devriez voir les 5 types de gâteaux.

### 3. Tester l'API

Lancez le serveur :
```bash
python manage.py runserver
```

Ouvrez dans votre navigateur :
- http://localhost:8000/api/cakes/types/

Vous devriez voir les gâteaux en JSON.

---

## 🛠️ Commandes utiles PostgreSQL

### Accéder au shell PostgreSQL depuis Django

```bash
python manage.py dbshell
```

### Sauvegarder la base de données

**Via Django :**
```bash
python manage.py dumpdata > backup.json
```

**Via pgAdmin :**
1. Clic droit sur `mongateau`
2. **Backup...**
3. Choisir le format et l'emplacement

### Restaurer la base de données

**Via Django :**
```bash
python manage.py loaddata backup.json
```

**Via pgAdmin :**
1. Clic droit sur `mongateau`
2. **Restore...**
3. Sélectionner le fichier de sauvegarde

### Réinitialiser la base de données

```bash
# Supprimer toutes les données (garde la structure)
python manage.py flush

# Recharger les données initiales
python manage.py loaddata cakes/fixtures/initial_cakes.json
```

### Voir les migrations appliquées

```bash
python manage.py showmigrations
```

---

## 🐛 Résolution de problèmes

### Erreur : "could not connect to server"

**Cause** : PostgreSQL n'est pas démarré

**Solution** :
1. Ouvrez **Services Windows** (Win + R → `services.msc`)
2. Cherchez **PostgreSQL**
3. Clic droit → **Démarrer**

OU dans pgAdmin, vérifiez que le serveur est connecté.

### Erreur : "FATAL: password authentication failed"

**Cause** : Mauvais mot de passe

**Solution** :
Vérifiez le mot de passe dans `backend/mongateau/settings.py` ligne ~90 :
```python
'PASSWORD': 'admin',  # Doit correspondre à votre mot de passe PostgreSQL
```

### Erreur : "database 'mongateau' does not exist"

**Cause** : La base de données n'a pas été créée

**Solution** :
Créez la base dans pgAdmin (voir Étape 2 ci-dessus)

### Erreur : "psycopg2" not found

**Cause** : Le module PostgreSQL n'est pas installé

**Solution** :
```bash
pip install psycopg2-binary
```

### Erreur : "relation does not exist"

**Cause** : Les migrations n'ont pas été appliquées

**Solution** :
```bash
python manage.py migrate
```

---

## 🔒 Sécurité

### Pour le développement

Les credentials actuels sont OK pour le développement local :
- User : `postgres`
- Password : `admin`
- Host : `localhost`

### Pour la production

⚠️ **NE PAS utiliser ces credentials en production !**

Créez :
1. Un utilisateur PostgreSQL dédié (pas `postgres`)
2. Un mot de passe fort
3. Utilisez des variables d'environnement (fichier `.env`)

Exemple `.env` :
```env
DB_NAME=mongateau
DB_USER=mongateau_user
DB_PASSWORD=VotreMdpFortetComplexe123!
DB_HOST=localhost
DB_PORT=5432
```

---

## 📊 Avantages de PostgreSQL vs SQLite

### PostgreSQL (actuel)
✅ Base de données professionnelle
✅ Support de grosses volumétries
✅ Meilleure performance
✅ Concurrent access
✅ Transactions avancées
✅ Prêt pour la production

### SQLite (alternative)
✅ Simple, sans installation
✅ Fichier unique
✅ OK pour développement/test
❌ Non recommandé en production

---

## 📈 Monitoring

### Voir les connexions actives (pgAdmin)

1. **Dashboard** → **Server Activity**
2. Voir les sessions actives

### Analyser les requêtes Django

```python
# Dans Django shell (python manage.py shell)
from django.db import connection
print(connection.queries)
```

---

## 🔧 Configuration avancée

### Changer le port PostgreSQL

Si votre PostgreSQL utilise un autre port :

Dans `settings.py` :
```python
DATABASES = {
    'default': {
        ...
        'PORT': '5433',  # Votre port
    }
}
```

### Utiliser un autre utilisateur

Dans `settings.py` :
```python
DATABASES = {
    'default': {
        ...
        'USER': 'votre_user',
        'PASSWORD': 'votre_password',
    }
}
```

### Connexion distante

Pour une base PostgreSQL sur un autre serveur :
```python
DATABASES = {
    'default': {
        ...
        'HOST': '192.168.1.100',  # IP du serveur
        'PORT': '5432',
    }
}
```

---

## 📝 Checklist de configuration

- [x] PostgreSQL installé et démarré
- [x] Base de données `mongateau` créée dans pgAdmin
- [x] Credentials configurés dans `settings.py`
- [x] `psycopg2-binary` installé
- [ ] Migrations appliquées (`python manage.py migrate`)
- [ ] Données initiales chargées (`loaddata`)
- [ ] Superutilisateur créé (`createsuperuser`)
- [ ] Serveur Django lancé et testé
- [ ] API accessible et fonctionnelle

---

## 💡 Conseils

1. **Sauvegardez régulièrement** votre base de données
2. **Utilisez pgAdmin** pour visualiser les données
3. **Testez les requêtes** dans le shell Django
4. **Surveillez les logs** de PostgreSQL en cas d'erreur
5. **Documentez** vos modifications de schéma

---

## 🆘 Support

Si vous rencontrez des problèmes :

1. Vérifiez que PostgreSQL est démarré
2. Vérifiez les credentials dans pgAdmin
3. Consultez les logs : `backend/logs/` (si configuré)
4. Utilisez `python setup_postgres.py` pour diagnostiquer
5. Vérifiez la connexion : `python manage.py dbshell`

---

**Base de données configurée pour MonGâteau**

🍰 **MonGâteau** est maintenant connecté à PostgreSQL !
