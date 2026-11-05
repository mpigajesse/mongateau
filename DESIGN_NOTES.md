# 🎨 Notes de Design - MonGâteau

## Inspiration

Design inspiré des thèmes modernes de pâtisserie professionnelle, avec une esthétique épurée et élégante.

## Palette de Couleurs

### Couleurs Principales
- **Primaire** : `#D4996C` - Beige/Or (couleur signature)
- **Primaire Foncé** : `#C08858` - Or foncé (hover states)
- **Texte Foncé** : `#2C2C2C` - Gris très foncé
- **Texte Clair** : `#666666` - Gris moyen
- **Fond Clair** : `#F4F1EC` - Beige très clair
- **Blanc** : `#FFFFFF`

### Utilisation des Couleurs
- Boutons primaires : Beige/Or avec dégradé
- Textes importants : Gris foncé
- Backgrounds alternatifs : Beige très clair
- Accents et highlights : Beige/Or

## Typographie

### Polices
- **Titres** : Georgia (serif) - Élégant et classique
- **Corps** : Helvetica Neue, système fonts - Moderne et lisible

### Hiérarchie
- H1 : 4.5rem (Hero) / 3rem (Pages)
- H2 : 2.5rem
- H3 : 1.5rem
- Body : 1rem
- Small : 0.95rem

## Composants

### Boutons

**Style Principal**
```css
background: #D4996C
color: white
padding: 16px 40px
border-radius: 4px
text-transform: uppercase
letter-spacing: 0.5px
```

**Hover Effect**
```css
background: #C08858
transform: translateY(-2px)
box-shadow: 0 4px 15px rgba(212, 153, 108, 0.3)
```

### Cartes

**Style**
```css
background: white
border-radius: 8px
box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08)
border: 1px solid #f0f0f0
```

**Hover Effect**
```css
transform: translateY(-5px)
box-shadow: 0 8px 25px rgba(212, 153, 108, 0.15)
```

### Formulaires

**Inputs**
```css
border: 1px solid #e0e0e0
border-radius: 4px
padding: 14px 16px
```

**Focus State**
```css
border-color: #D4996C
box-shadow: 0 0 0 3px rgba(212, 153, 108, 0.1)
```

## Pages

### HomePage

#### Structure
1. **Header** - Sticky avec logo
2. **Hero Section** 
   - Badge "Pâtisserie Artisanale"
   - Titre principal avec accent coloré
   - 2 boutons CTA
3. **About Section**
   - Image/emoji à gauche
   - Texte descriptif à droite
   - Signature de la créatrice
4. **Features** - Grid de 4 cartes
5. **CTA Section** - Dark background
6. **Footer** - Fond clair

### CakeList

#### Structure
1. **Header** - Fond beige clair
2. **Grille de cartes** - 3 colonnes max
   - Image du gâteau
   - Nom et description
   - Prix et bouton

### OrderForm

#### Structure
1. **Résumé du gâteau** - Carte avec dégradé
2. **Formulaire** - Fond blanc
   - Labels clairs
   - Inputs élégants
   - Section paiement mise en valeur

### OrderConfirmation

#### Structure
1. **Icône de succès**
2. **Message de confirmation**
3. **Récapitulatif** - Fond beige clair
4. **Section ticket** - Dégradé beige/or
5. **Prochaines étapes**
6. **Bouton retour**

## Responsive Design

### Breakpoints
- Mobile : < 768px
- Desktop : > 768px

### Adaptations Mobile
- Grid 1 colonne
- Padding réduits
- Font sizes ajustées
- Hero title : 3rem
- About section : 1 colonne

## Animations

### Transitions Globales
```css
transition: all 0.3s ease
```

### Animations Spécifiques
- **fadeIn** : Entrée des pages
- **scaleIn** : Icône de succès
- **Hover effects** : translateY(-2px à -5px)

## Accessibilité

- Contraste suffisant pour tous les textes
- Focus states visibles
- Tailles de boutons adaptées au touch
- Labels explicites sur les formulaires

## Design System

### Espacement
- Base : 20px
- Sections : 80px padding vertical
- Cards : 30-40px padding

### Border Radius
- Standard : 8px
- Boutons : 4px
- Badges : 20px

### Shadows
- Subtile : `0 2px 10px rgba(0, 0, 0, 0.08)`
- Hover : `0 8px 25px rgba(212, 153, 108, 0.15)`

## Améliorations Futures

### Images
- Remplacer les emojis par de vraies photos professionnelles
- Ajouter des images de fond subtiles
- Galerie de réalisations

### Animations
- Parallax scrolling subtil
- Animations au scroll
- Micro-interactions

### Fonctionnalités
- Mode sombre (optionnel)
- Animations de chargement personnalisées
- Skeleton loaders

---

**Design de MonGâteau**
🍰 MonGâteau - Pâtisserie Artisanale
