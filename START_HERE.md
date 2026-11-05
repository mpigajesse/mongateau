# 🚀 COMMENCER ICI - MonGâteau

**Guide de démarrage ultra-rapide pour MonGâteau**

---

## ⚡ Démarrage en 5 minutes

### 📋 Avant de commencer

Vérifiez que vous avez :
- ✅ Python 3.8+ installé
- ✅ Node.js 16+ installé
- ✅ PostgreSQL installé et démarré
- ✅ Base de données `mongateau` créée dans pgAdmin

---

## 🎯 Étape 1 : Backend Django (2 minutes)

Ouvrez un terminal :

```bash
cd backend

# Créer et activer l'environnement virtuel
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# Installer les dépendances
pip install -r requirements.txt

# Configurer PostgreSQL (automatique)
python setup_postgres.py
```

Le script va :
1. ✅ Tester la connexion à PostgreSQL
2. ✅ Créer les tables dans la base de données
3. ✅ Charger les 5 types de gâteaux
4. ✅ Proposer de créer un compte admin

**Puis lancez le serveur :**

```bash
python manage.py runserver
```

✅ **Backend prêt sur http://localhost:8000**

---

## 🎨 Étape 2 : Frontend React (2 minutes)

Ouvrez un **NOUVEAU terminal** :

```bash
cd frontend

# Installer les dépendances
npm install

# Lancer l'application
npm start
```

✅ **Frontend prêt sur http://localhost:3000**

L'application s'ouvre automatiquement dans votre navigateur !

---

## ✅ Étape 3 : Tester l'application (1 minute)

### Test rapide :

1. **Page d'accueil** : http://localhost:3000
   - Cliquez sur "Commander un gâteau"

2. **Choisir un gâteau** : 
   - Sélectionnez n'importe quel gâteau

3. **Remplir le formulaire** :
   - Nom : Test Client
   - Téléphone : 0612345678
   - Date : (choisissez dans 3 jours)
   - Adresse : 123 Rue Test, Libreville
   - Message : Test de commande

4. **Valider** :
   - Téléchargez le ticket PDF
   - Vérifiez le numéro de commande

### Vérifier dans l'admin Django :

1. Ouvrez http://localhost:8000/admin
2. Connectez-vous avec le compte créé
3. Allez dans **Commandes** → voir votre test

---

## 🎉 C'est fait !

Votre application MonGâteau est maintenant **opérationnelle** !

---

## 📚 Documentation détaillée

- **Guide d'installation complet** : [INSTALLATION.md](INSTALLATION.md)
- **Configuration PostgreSQL** : [CONFIGURATION_POSTGRESQL.md](CONFIGURATION_POSTGRESQL.md)
- **Guide d'utilisation** : [GUIDE_UTILISATION.md](GUIDE_UTILISATION.md)
- **Fonctionnalités complètes** : [FONCTIONNALITES.md](FONCTIONNALITES.md)

---

## 🐛 Problèmes ?

### Le backend ne démarre pas

```bash
# Vérifiez que PostgreSQL est démarré
# Dans pgAdmin, vérifiez que la base 'mongateau' existe
# Relancez le script de configuration
python setup_postgres.py
```

### Erreur de connexion PostgreSQL

Vérifiez les credentials dans `backend/mongateau/settings.py` ligne 75 :
- NAME : `mongateau`
- USER : `postgres`
- PASSWORD : `admin`

### Le frontend ne se connecte pas au backend

Vérifiez que le backend est lancé sur http://localhost:8000

---

## 🗂️ Configuration actuelle

### Base de données PostgreSQL
- **Nom** : mongateau
- **User** : postgres
- **Password** : admin
- **Host** : localhost
- **Port** : 5432

### 5 Types de gâteaux pré-chargés
1. 🎂 Gâteau d'anniversaire - 15 000 FCFA
2. 🎉 Gâteau pour événements - 20 000 FCFA
3. 🎁 Gâteau surprise - 18 000 FCFA
4. ✨ Gâteau personnalisé - 25 000 FCFA
5. 💍 Gâteau de mariage - 50 000 FCFA

---

## 💡 Prochaines étapes

1. **Personnalisez les gâteaux** dans l'admin
2. **Ajoutez de belles images** (URLs)
3. **Testez le parcours complet** client
4. **Vérifiez les tickets PDF** générés

---

## 🛠️ Scripts de démarrage rapide

Une fois configuré, utilisez les scripts :

### Windows
```bash
# Backend
cd backend
start_backend.bat

# Frontend (nouveau terminal)
cd frontend
start_frontend.bat
```

### macOS/Linux
```bash
# Backend
cd backend
chmod +x start_backend.sh
./start_backend.sh

# Frontend (nouveau terminal)
cd frontend
chmod +x start_frontend.sh
./start_frontend.sh
```

---

## 🎓 Apprendre l'application

### Pour les clients
Consultez le [GUIDE_UTILISATION.md](GUIDE_UTILISATION.md) section "Pour les clients"

### Pour l'administratrice ou l'administrateur
Consultez le [GUIDE_UTILISATION.md](GUIDE_UTILISATION.md) section "Pour l'administrateur"

---

**MonGâteau**

🍰 **MonGâteau** - Votre application de commande de gâteaux est prête !

**Bon développement ! 🚀**
