# 📖 Guide d'Utilisation - MonGâteau

Guide complet pour utiliser l'application MonGâteau.

## 👥 Pour les clients

### Comment commander un gâteau

#### Étape 1 : Page d'accueil
- Accédez à l'application sur http://localhost:3000
- Cliquez sur le bouton **"Commander un gâteau"**

#### Étape 2 : Choisir un gâteau
- Parcourez les 5 types de gâteaux disponibles :
  - 🎂 Gâteau d'anniversaire
  - 🎉 Gâteau pour événements
  - 🎁 Gâteau surprise
  - ✨ Gâteau personnalisé
  - 💍 Gâteau de mariage
- Cliquez sur **"Commander"** pour le gâteau souhaité

#### Étape 3 : Remplir le formulaire
Complétez les informations suivantes :
- **Nom complet** : Votre nom et prénom
- **Numéro de téléphone** : Pour vous contacter (min. 8 chiffres)
- **Date de livraison** : Minimum 2 jours à l'avance
- **Adresse de livraison** : Adresse complète
- **Message personnalisé** (optionnel) : Instructions spéciales, texte sur le gâteau, etc.

#### Étape 4 : Valider la commande
- Vérifiez vos informations
- Cliquez sur **"Valider la commande"**

#### Étape 5 : Confirmation et ticket
- Votre commande est confirmée ! ✅
- Notez votre **numéro de commande** (format: MG-XXXXXXXX)
- Téléchargez votre **ticket PDF** en cliquant sur le bouton
- **Important** : Conservez ce ticket pour la livraison

### Paiement

💵 **Le paiement s'effectue uniquement à la livraison**

Aucun paiement en ligne n'est requis. Vous règlerez le montant lors de la réception de votre gâteau.

### Suivi de commande

Votre numéro de commande vous permet de suivre l'état de votre commande.
Conservez-le précieusement !

---

## 👨‍💼 Pour l'administrateur (NAOMIE MOUSSAVOU)

### Accès à l'interface d'administration

1. Accédez à http://localhost:8000/admin
2. Connectez-vous avec vos identifiants administrateur

### Gestion des types de gâteaux

#### Voir tous les gâteaux
- Menu **Gâteaux** → **Types de gâteaux**
- Liste de tous les types disponibles

#### Ajouter un nouveau type de gâteau
1. Cliquez sur **"Ajouter Type de gâteau"**
2. Remplissez :
   - **Nom** : Ex: "Gâteau d'anniversaire"
   - **Type** : Choisir dans la liste
   - **Description** : Description détaillée
   - **Prix de base** : Prix en FCFA
   - **URL de l'image** : Lien vers une image (optionnel)
   - **Disponible** : Cochez pour rendre visible aux clients
3. Cliquez sur **"Enregistrer"**

#### Modifier un type de gâteau
1. Cliquez sur le gâteau à modifier
2. Modifiez les informations
3. Cliquez sur **"Enregistrer"**

#### Désactiver un gâteau temporairement
1. Cliquez sur le gâteau
2. Décochez **"Disponible"**
3. Enregistrez

Le gâteau ne sera plus visible aux clients mais les données sont conservées.

### Gestion des commandes

#### Voir toutes les commandes
- Menu **Commandes** → **Commandes**
- Liste de toutes les commandes

#### Filtrer les commandes
Utilisez les filtres à droite :
- Par **statut** (En attente, Confirmée, etc.)
- Par **date de livraison**
- Par **date de création**
- Par **type de gâteau**

#### Rechercher une commande
Utilisez la barre de recherche pour trouver par :
- Numéro de commande
- Nom du client
- Numéro de téléphone

#### Voir les détails d'une commande
Cliquez sur une commande pour voir :
- Informations client
- Détails du gâteau
- Date et adresse de livraison
- Message personnalisé
- Prix total
- Chemin du ticket PDF

#### Changer le statut d'une commande

Les statuts disponibles :
- **En attente** : Commande reçue, non traitée
- **Confirmée** : Commande acceptée
- **En préparation** : Gâteau en cours de fabrication
- **Prête** : Gâteau terminé, prêt pour livraison
- **Livrée** : Commande livrée et payée
- **Annulée** : Commande annulée

Pour changer le statut :
1. Ouvrez la commande
2. Sélectionnez le nouveau statut
3. Cliquez sur **"Enregistrer"**

### Workflow recommandé

1. **Nouvelle commande** → Statut : En attente
   - Vérifier les informations
   - Confirmer la faisabilité

2. **Accepter la commande** → Statut : Confirmée
   - Contacter le client si nécessaire

3. **Commencer la fabrication** → Statut : En préparation
   - Préparer le gâteau selon les spécifications

4. **Gâteau terminé** → Statut : Prête
   - Organiser la livraison

5. **Livrer et encaisser** → Statut : Livrée
   - Livrer le gâteau
   - Récupérer le paiement
   - Marquer comme livrée

### Tickets PDF

Chaque commande génère automatiquement un ticket PDF qui contient :
- Numéro de commande
- Informations client
- Détails du gâteau
- Date et adresse de livraison
- Prix total
- Mention "Paiement à la livraison"

Le ticket est stocké dans `backend/tickets/`.

---

## 📊 Statistiques et rapports

### Commandes du jour
Filtrez par date de création = aujourd'hui

### Livraisons à venir
Filtrez par date de livraison future + statut = "Prête"

### Commandes par type de gâteau
Utilisez le filtre "Type de gâteau"

### Chiffre d'affaires
Additionnez les commandes avec statut = "Livrée"

---

## 🔒 Sécurité

### Recommandations
- Changez le **SECRET_KEY** dans `settings.py` en production
- Créez un mot de passe fort pour le compte admin
- Activez HTTPS en production
- Sauvegardez régulièrement la base de données

### Sauvegarder la base de données

```bash
# Sauvegarder
python manage.py dumpdata > backup.json

# Restaurer
python manage.py loaddata backup.json
```

---

## 📞 Contact client

Lorsqu'un client passe commande :
- Utilisez le numéro de téléphone fourni pour le contacter
- Référencez toujours le numéro de commande
- Confirmez les détails si nécessaire

---

## 💡 Conseils

### Pour les clients
- Commandez au minimum 2 jours à l'avance
- Soyez précis dans votre adresse de livraison
- Ajoutez un message personnalisé pour des instructions spéciales
- Conservez votre ticket PDF

### Pour l'administrateur
- Traitez les commandes rapidement
- Mettez à jour les statuts régulièrement
- Contactez les clients en cas de problème
- Gardez les types de gâteaux à jour avec de belles photos

---

## 🎨 Personnalisation

### Changer les images des gâteaux
1. Trouvez une image de qualité (recommandé : 800x600px minimum)
2. Uploadez l'image sur un service d'hébergement (Imgur, Cloudinary, etc.)
3. Copiez l'URL de l'image
4. Dans l'admin, éditez le type de gâteau et collez l'URL

### Modifier les prix
Les prix sont en FCFA. Modifiez le "Prix de base" dans l'admin.

---

**Propriétaire : NAOMIE MOUSSAVOU**

Pour toute question : consultez ce guide ou contactez le support technique. 🍰
