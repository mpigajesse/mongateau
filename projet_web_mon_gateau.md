# 🍰 MonGâteau – Application Web de Commande de Gâteaux

## 1. Présentation générale

**MonGâteau** est une application web moderne, simple et rapide permettant aux clients de commander des gâteaux en ligne sans création de compte ni authentification.

L’objectif principal est de faciliter la réservation de gâteaux artisanaux pour différents événements, avec un processus **fluide, rapide et sans complexité inutile**.

La fabrication et la gestion des commandes sont assurées par **NAOMIE MOUSSAVOU**, propriétaire de l’application et créatrice des gâteaux.

---

## 2. Objectifs de l’application

- Permettre aux clients de **commander un gâteau en ligne facilement et rapidement**
- Éviter toute complexité (pas de compte, pas de mot de passe, pas d’étapes inutiles)
- Offrir une **expérience utilisateur jolie, moderne et intuitive**
- Générer automatiquement un **ticket de réservation téléchargeable** après commande
- **Paiement uniquement à la livraison**

---

## 3. Types de gâteaux proposés

L’application propose plusieurs catégories de gâteaux :

1. 🎂 **Gâteau d’anniversaire**  
2. 🎉 **Gâteau pour événements**  
3. 🎁 **Gâteau surprise**  
4. ✨ **Gâteau personnalisé**  
5. 💍 **Gâteau de mariage**

Chaque type de gâteau peut inclure :
- Une description
- Des options de personnalisation
- Un prix estimatif
- Une image illustrative

---

## 4. Fonctionnalités principales

### Côté client

- Consultation des types de gâteaux
- Formulaire de commande simple :
  - Nom du client
  - Numéro de téléphone
  - Type de gâteau
  - Message personnalisé (optionnel)
  - Date de livraison
  - Adresse de livraison
- Validation de la commande en **moins d’étapes possibles**
- Génération et **téléchargement d’un ticket de réservation (PDF)**
- Message de confirmation après commande

### Paiement

- 💵 **Paiement uniquement à la livraison**
- Mention claire sur le ticket et l’interface

---

## 5. Architecture technique

### Backend

- **Django** (API REST)
- Django REST Framework
- Base de données : SQLite (début) → PostgreSQL (évolution possible)
- Génération de ticket PDF côté serveur

### Frontend

- **React avec TypeScript**
- Interface responsive (mobile & desktop)
- Design moderne et épuré
- Communication avec l’API Django via HTTP (Axios / Fetch)
- Priorité à la **rapidité et simplicité**

---

## 6. Parcours utilisateur

1. Le client arrive sur la page d’accueil
2. Il choisit un type de gâteau
3. Il remplit le formulaire de commande rapidement
4. Il valide la commande
5. Un message de confirmation s’affiche
6. Il télécharge son **ticket de réservation**
7. Il paie le gâteau à la livraison

---

## 7. Identité & Propriété

- **Nom de l’application :** MonGâteau
- **Propriétaire & créatrice :** NAOMIE MOUSSAVOU
- **Activité :** Fabrication artisanale de gâteaux & gestion des commandes

---

## 8. Évolutions futures possibles

- Paiement en ligne (Mobile Money / Carte bancaire)
- Tableau de bord administrateur
- Notifications WhatsApp / SMS
- Suivi de commande
- Galerie photo des réalisations

---

✨ *MonGâteau : commander un gâteau devient un plaisir simple, rapide et gourmand.*