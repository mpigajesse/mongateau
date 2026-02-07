# 🔐 Guide QR Code - Système de Vérification MonGâteau

## 📱 Comment ça marche ?

### 1. Génération du Ticket
Lorsqu'une commande est créée, un ticket JPG ultra-premium est généré avec:
- Design style ThemeForest/Envato Premium
- QR Code de vérification unique
- Informations complètes de la commande

### 2. QR Code Généré
Chaque QR code contient une URL unique:
```
http://localhost:8000/verify/{NUMERO_COMMANDE}/
```

Exemple: `http://localhost:8000/verify/MG-ABC12345/`

### 3. Vérification par Scan

#### 📱 Depuis un Mobile
1. Client scanne le QR code avec son téléphone
2. Le navigateur s'ouvre automatiquement
3. Une belle page web s'affiche avec:
   - ✅ Badge "COMMANDE VALIDE"
   - 📋 **Numéro de commande** (en gros et en évidence)
   - 👤 **Nom du client** (bien visible)
   - 🎂 Type de gâteau
   - 📅 Date de livraison
   - 💰 Prix total
   - 📊 Statut de la commande

#### 💻 Via API
Pour les applications, l'endpoint retourne du JSON:
```bash
curl -H "Accept: application/json" http://localhost:8000/verify/MG-ABC12345/
```

Réponse:
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

## 🎨 Design de la Page de Vérification

### Caractéristiques Premium
- ✨ **Glassmorphism** - Effet verre moderne
- 🌈 **Gradients** - Dégradés sophistiqués (rose → violet → orange)
- 💫 **Animations** - Apparition fluide des éléments
- 📱 **Responsive** - Parfait sur mobile et desktop
- 🎯 **Focus visuel** - Numéro de commande et nom du client en évidence

### Palette de Couleurs
- **Primary Gradient**: `#8A2387 → #E94057 → #F27121`
- **Accent Gold**: `#FFD700`
- **Success**: `#10b981`
- **Error**: `#ef4444`

### Éléments Visuels
1. **Header animé** avec logo MonGâteau 🍰
2. **Badge de statut** (vert pour valide, rouge pour invalide)
3. **Cartes d'information** avec hover effects
4. **Prix total** en grand avec fond dégradé
5. **Footer** avec informations créatrice

## 🔧 Configuration

### URLs
Le système utilise 2 routes:

1. **Route API** (pour ViewSet):
   ```
   GET /api/orders/verify/{order_number}/
   ```

2. **Route directe** (pour QR code):
   ```
   GET /verify/{order_number}/
   ```
   → Plus court et facile à scanner

### Templates
Le template HTML se trouve dans:
```
backend/orders/templates/orders/verify_order.html
```

### Vue (Logic)
La logique de vérification est dans:
```python
# backend/orders/views.py
class OrderViewSet:
    @action(detail=False, methods=['get'])
    def verify(self, request, order_number=None):
        # Détecte si c'est JSON ou HTML
        # Retourne la bonne réponse
```

## 📋 Cas d'Usage

### ✅ Commande Valide
**Scénario**: Client scanne le QR code d'un ticket valide

**Affichage**:
- ✅ Badge vert "COMMANDE VALIDE"
- Toutes les informations de la commande
- Prix total en évidence
- Statut actuel

**Données affichées en priorité**:
1. 📋 Numéro de commande (très grand)
2. 👤 Nom du client (grand)
3. 🎂 Type de gâteau
4. 📅 Date de livraison
5. 💰 Prix total

### ❌ Commande Invalide
**Scénario**: QR code falsifié ou numéro inexistant

**Affichage**:
- ❌ Badge rouge "COMMANDE INVALIDE"
- Message d'erreur explicatif
- Pas d'information sensible révélée

## 🧪 Tests

### Test Manuel

1. **Créer une commande**:
   ```bash
   # Via l'interface web ou API
   POST http://localhost:8000/api/orders/
   ```

2. **Télécharger le ticket JPG**:
   ```bash
   GET http://localhost:8000/api/orders/{id}/download-ticket/
   ```

3. **Scanner le QR code**:
   - Utiliser l'appareil photo du téléphone
   - Ou une app de scan QR code
   - Vérifier que la page s'ouvre

4. **Vérifier les informations affichées**:
   - ✅ Numéro de commande visible
   - ✅ Nom du client visible
   - ✅ Toutes les infos correctes

### Test avec URL Directe

```bash
# Navigateur
http://localhost:8000/verify/MG-ABC12345/

# API (JSON)
curl -H "Accept: application/json" http://localhost:8000/verify/MG-ABC12345/
```

## 🚀 Déploiement en Production

### 1. Mettre à jour l'URL du QR code

Éditer `backend/orders/ticket_generator.py`:

```python
# Ligne ~257
# AVANT (développement):
verification_url = f"http://localhost:8000/verify/{order.order_number}/"

# APRÈS (production):
verification_url = f"https://votre-domaine.com/verify/{order.order_number}/"
```

### 2. Configurer HTTPS
⚠️ **Important**: Utilisez HTTPS en production pour la sécurité

### 3. Mettre à jour ALLOWED_HOSTS

Dans `backend/mongateau/settings.py`:
```python
ALLOWED_HOSTS = ['votre-domaine.com', 'www.votre-domaine.com']
```

### 4. CORS pour la vérification
Ajouter votre domaine dans CORS_ALLOWED_ORIGINS si nécessaire

## 📱 Utilisation Mobile Optimale

### Pour iOS (iPhone/iPad)
- ✅ App Appareil photo native
- ✅ Safari
- ✅ Apps tierces (QR Code Reader)

### Pour Android
- ✅ Google Lens
- ✅ Chrome
- ✅ Apps tierces

### Conseils
1. **Bonne luminosité** - Scanner dans un endroit bien éclairé
2. **Distance** - Tenir le téléphone à 15-20cm du QR code
3. **Stable** - Ne pas bouger pendant le scan
4. **Connexion Internet** - Nécessaire pour charger la page

## 🔐 Sécurité

### Mesures en Place
1. ✅ Numéro de commande unique (UUID)
2. ✅ Vérification côté serveur
3. ✅ Pas d'informations sensibles dans le QR
4. ✅ HTTPS recommandé en production

### Informations Publiques
Le QR code ne contient que:
- URL de vérification
- Numéro de commande

Les détails (nom, prix, etc.) sont récupérés depuis la base de données.

## 💡 Fonctionnalités Futures (Optionnel)

1. **Historique de scans** - Tracer qui/quand le ticket a été vérifié
2. **Notifications** - Alerter le client quand son ticket est vérifié
3. **Authentification** - Réserver la vérification aux livreurs autorisés
4. **Statistiques** - Nombre de vérifications par commande

## 🆘 Dépannage

### Le QR code ne se scanne pas
- Vérifier la qualité de l'image JPG
- Essayer avec une autre app de scan
- Vérifier la luminosité

### La page ne se charge pas
- Vérifier que le serveur Django tourne
- Vérifier la connexion Internet
- Vérifier l'URL dans le navigateur

### Erreur "Commande introuvable"
- Vérifier que la commande existe dans la base
- Vérifier le numéro de commande
- Regarder les logs Django

## 📞 Support

Pour toute question:
- 📧 Contacter NAOMIE MOUSSAVOU
- 📝 Consulter la documentation
- 🐛 Vérifier les logs Django

---

**Version**: 2.0.0  
**Date**: 2026-02-07  
**Auteur**: NAOMIE MOUSSAVOU
