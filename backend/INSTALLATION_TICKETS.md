# 🎨 Installation du Nouveau Système de Tickets JPG Premium

## 📋 Modifications Effectuées

Le système de tickets a été transformé de **PDF basique** vers des **cartes JPG premium avec QR code de vérification**.

### ✨ Nouvelles Fonctionnalités

1. **Design Premium Style Envato** 🎨
   - Dégradé rose élégant (#FF6B9D)
   - Carte blanche avec ombres portées
   - Typographie professionnelle
   - Formes décoratives

2. **QR Code de Vérification** 🔐
   - Code QR unique par commande
   - URL: `http://localhost:8000/api/orders/verify/{order_number}/`
   - Endpoint API pour validation
   - Sécurité renforcée

3. **Format JPG Haute Qualité** 📸
   - Dimensions: 1200x1600 pixels
   - Qualité: 95%
   - Compatible mobile et impression

## 🔧 Installation

### 1. Installer les dépendances

```bash
cd backend

# Activer l'environnement virtuel
python -m venv venv
.\venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

# Installer les nouvelles dépendances
pip install -r requirements.txt
```

**Nouvelle dépendance ajoutée:**
- `qrcode==7.4.2` - Génération de QR codes

### 2. Appliquer les migrations (optionnel)

Le champ `ticket_path` existe déjà mais sa description a été mise à jour:

```bash
python manage.py migrate
```

### 3. Tester la génération de tickets

```bash
# Lancer le serveur Django
python manage.py runserver

# Dans un autre terminal, tester la génération:
python tmp_rovodev_test_ticket.py
```

## 📁 Fichiers Modifiés

### Backend

1. **`requirements.txt`**
   - Ajout: `qrcode==7.4.2`

2. **`orders/ticket_generator.py`** ✨ NOUVEAU
   - Remplace `pdf_generator.py`
   - Génère des cartes JPG premium
   - Intègre le QR code
   - Design style Envato

3. **`orders/views.py`**
   - Import: `ticket_generator` au lieu de `pdf_generator`
   - `download_ticket()`: Retourne JPG au lieu de PDF
   - `verify()`: ✨ NOUVEAU - Endpoint de vérification QR code

4. **`orders/models.py`**
   - `ticket_path`: Description mise à jour (JPG au lieu de PDF)

### Frontend

1. **`pages/ConfirmationPage.tsx`**
   - `handleDownloadTicket()`: Télécharge JPG au lieu de PDF
   - Texte bouton: "Télécharger le Ticket (JPG)"

## 🎯 API Endpoints

### Nouveau Endpoint: Vérification QR Code

```
GET /api/orders/verify/<order_number>/
```

**Réponse succès (200):**
```json
{
  "valid": true,
  "order_number": "MG-ABC12345",
  "customer_name": "Jean Dupont",
  "cake_type": "Gâteau d'anniversaire",
  "delivery_date": "2024-12-25",
  "total_price": "15000.00",
  "status": "pending",
  "status_display": "En attente",
  "message": "Commande valide ✓"
}
```

**Réponse échec (404):**
```json
{
  "valid": false,
  "message": "Commande introuvable ✗"
}
```

### Endpoint Modifié: Téléchargement

```
GET /api/orders/<id>/download-ticket/
```

- Retourne maintenant: `image/jpeg` (au lieu de `application/pdf`)
- Nom fichier: `ticket_<order_number>.jpg`

## 🎨 Détails du Design

### Palette de Couleurs

- **Rose principal**: `#FF6B9D`
- **Rose foncé**: `#C94277`
- **Or/Crème**: `#FFF8DC` et `#FFD700`
- **Texte**: `#333333`, `#666666`, `#999999`
- **Blanc**: `#FFFFFF`

### Dimensions

- **Largeur**: 1200px
- **Hauteur**: 1600px
- **Format**: Portrait (ratio ~3:4)

### Éléments

1. **Header** (0-150px)
   - Logo "🍰 MonGâteau" centré
   - Fond dégradé rose

2. **Carte principale** (150-1450px)
   - Rectangle blanc arrondi
   - Ombre portée
   - Informations de commande
   - QR code centré

3. **Footer** (1450-1600px)
   - Informations créatrice
   - Fond dégradé rose

## 🧪 Tests

### Test Manuel

1. Créer une commande via l'interface web
2. Aller sur la page de confirmation
3. Cliquer sur "Télécharger le Ticket (JPG)"
4. Vérifier que le JPG est téléchargé
5. Ouvrir le JPG et vérifier le design
6. Scanner le QR code avec votre téléphone
7. Vérifier que l'URL renvoie les détails de la commande

### Test avec Script

```bash
python tmp_rovodev_test_ticket.py
```

Le script:
1. Trouve la dernière commande
2. Génère le ticket JPG
3. Affiche le chemin du fichier
4. Met à jour la base de données

## 📱 Utilisation Mobile

Les tickets JPG peuvent être:
- 📱 Enregistrés dans la galerie du téléphone
- 📧 Envoyés par email
- 💬 Partagés via WhatsApp/Telegram
- 🖨️ Imprimés en haute qualité
- 📲 Scannés pour vérification

## 🔄 Migration depuis PDF

Si vous avez des anciennes commandes avec tickets PDF:

```python
# Script de migration (optionnel)
from orders.models import Order
from orders.ticket_generator import generate_order_ticket

# Régénérer tous les tickets en JPG
for order in Order.objects.all():
    try:
        ticket_path = generate_order_ticket(order)
        order.ticket_path = ticket_path
        order.save()
        print(f"✅ {order.order_number}: Ticket JPG généré")
    except Exception as e:
        print(f"❌ {order.order_number}: Erreur - {e}")
```

## ⚠️ Notes Importantes

1. **Polices système**: Le générateur utilise des polices système (DejaVu sur Linux, Arial sur Windows)
2. **Répertoire tickets**: Les JPG sont sauvegardés dans `backend/tickets/`
3. **Qualité**: JPG sauvegardé à 95% de qualité pour un bon équilibre taille/qualité
4. **QR Code**: L'URL de vérification utilise localhost - à modifier pour la production

## 🚀 Prochaines Étapes

Pour la production:

1. Mettre à jour l'URL du QR code dans `ticket_generator.py`:
   ```python
   verification_url = f"https://votre-domaine.com/api/orders/verify/{order.order_number}/"
   ```

2. Configurer HTTPS pour la sécurité

3. Ajouter une page web de vérification conviviale

4. Optionnel: Envoyer le ticket par email automatiquement

## 📞 Support

Pour toute question concernant le nouveau système de tickets, référez-vous à:
- `backend/orders/ticket_generator.py` - Code de génération
- Ce fichier (INSTALLATION_TICKETS.md) - Documentation

---

**Projet :** MonGâteau  
**Date:** 2026-02-07  
**Version:** 1.0.0
