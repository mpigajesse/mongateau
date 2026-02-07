# 🎨 Design System - MonGâteau

Documentation complète du système de design moderne et professionnel.

---

## 📋 Vue d'ensemble

Le design system de MonGâteau est un ensemble cohérent de composants réutilisables, de styles et de guidelines qui garantissent une expérience utilisateur consistante et professionnelle.

### Principes

1. **Réutilisabilité** - Chaque composant est conçu pour être utilisé dans différents contextes
2. **Cohérence** - Utilisation de variables CSS pour garantir l'uniformité
3. **Accessibilité** - Focus states, contraste, ARIA labels
4. **Performance** - Composants optimisés avec Framer Motion
5. **Maintenabilité** - Code propre, organisé et documenté

---

## 🎨 Variables CSS

### Fichier : `src/styles/variables.css`

Toutes les variables de design sont centralisées dans un seul fichier.

#### Couleurs

```css
--primary-500: #D4996C    /* Couleur principale */
--primary-600: #C08858    /* Hover states */
--text-primary: #2C2C2C   /* Texte principal */
--text-secondary: #616161 /* Texte secondaire */
--bg-primary: #FFFFFF     /* Fond principal */
--bg-secondary: #F4F1EC   /* Fond alternatif */
```

#### Typographie

```css
--font-heading: 'Playfair Display', Georgia, serif
--font-body: 'Inter', sans-serif
--text-xs: 0.75rem   /* 12px */
--text-base: 1rem    /* 16px */
--text-6xl: 3.75rem  /* 60px */
```

#### Espacements

```css
--spacing-4: 1rem      /* 16px */
--spacing-8: 2rem      /* 32px */
--spacing-12: 3rem     /* 48px */
--spacing-20: 5rem     /* 80px */
```

#### Autres

- Border radius : `--radius-sm` à `--radius-full`
- Shadows : `--shadow-sm` à `--shadow-primary-lg`
- Transitions : `--transition-fast`, `--transition-base`
- Z-index : `--z-base` à `--z-tooltip`

---

## 🧩 Composants UI

### Button

**Fichier :** `src/components/ui/Button.tsx`

#### Variantes
- `primary` - Bouton principal (fond beige/or)
- `secondary` - Bouton secondaire (fond gris foncé)
- `outline` - Bouton avec bordure
- `ghost` - Bouton transparent
- `danger` - Bouton d'erreur

#### Tailles
- `sm` - Petit (36px hauteur)
- `md` - Moyen (44px hauteur)
- `lg` - Grand (52px hauteur)

#### Props
```typescript
variant?: 'primary' | 'secondary' | 'outline' | 'ghost' | 'danger'
size?: 'sm' | 'md' | 'lg'
fullWidth?: boolean
loading?: boolean
icon?: React.ReactNode
iconPosition?: 'left' | 'right'
```

#### Utilisation
```tsx
import { Button } from '../ui';
import { FiShoppingBag } from 'react-icons/fi';

<Button 
  variant="primary" 
  size="lg"
  icon={<FiShoppingBag />}
  iconPosition="right"
>
  Commander
</Button>
```

---

### Card

**Fichier :** `src/components/ui/Card.tsx`

#### Variantes
- `default` - Carte standard
- `elevated` - Avec plus d'ombre
- `outlined` - Avec bordure visible

#### Props
```typescript
variant?: 'default' | 'elevated' | 'outlined'
padding?: 'none' | 'sm' | 'md' | 'lg'
hoverable?: boolean  // Animation hover
onClick?: () => void
```

---

### Input

**Fichier :** `src/components/ui/Input.tsx`

#### Fonctionnalités
- Label automatique
- Messages d'erreur
- Helper text
- Icônes (gauche/droite)
- États : normal, focus, error, disabled

#### Utilisation
```tsx
import { Input } from '../ui';
import { FiMail } from 'react-icons/fi';

<Input
  label="Email"
  placeholder="votre@email.com"
  icon={<FiMail />}
  error={errors.email}
  required
/>
```

---

### Textarea

**Fichier :** `src/components/ui/Textarea.tsx`

Similaire à Input mais pour texte multiligne.

---

### Badge

**Fichier :** `src/components/ui/Badge.tsx`

#### Variantes
- `primary`, `success`, `warning`, `error`, `info`, `neutral`

#### Utilisation
```tsx
import { Badge } from '../ui';

<Badge variant="success">Nouveau</Badge>
```

---

### Spinner

**Fichier :** `src/components/ui/Spinner.tsx`

#### Tailles
- `sm` (16px), `md` (24px), `lg` (40px)

#### Couleurs
- `primary`, `white`

---

## 🏗️ Composants Layout

### Container

**Fichier :** `src/components/layout/Container.tsx`

Centre le contenu avec largeur max.

#### Tailles
- `sm` (640px), `md` (768px), `lg` (1024px), `xl` (1280px), `full`

```tsx
<Container size="xl">
  {/* Contenu */}
</Container>
```

---

### Section

**Fichier :** `src/components/layout/Section.tsx`

Wrapper pour sections de page.

#### Variantes
- `default` - Fond blanc
- `primary` - Fond beige clair
- `secondary` - Fond tertiaire

#### Padding
- `none`, `sm`, `md`, `lg`

```tsx
<Section variant="primary" padding="lg">
  <Container>
    {/* Contenu */}
  </Container>
</Section>
```

---

### PageHeader

**Fichier :** `src/components/common/PageHeader.tsx`

Header de page avec titre, sous-titre et bouton retour.

```tsx
<PageHeader
  title="Nos Gâteaux"
  subtitle="Choisissez le gâteau parfait"
  onBack={() => navigate('/')}
/>
```

---

## 🎯 Composants Métier

### CakeCard

**Fichier :** `src/components/common/CakeCard.tsx`

Carte pour afficher un gâteau.

#### Fonctionnalités
- Image avec placeholder
- Badge de catégorie
- Description
- Prix formaté
- Bouton commander
- Animations hover

```tsx
<CakeCard 
  cake={cakeData} 
  onOrder={(cake) => handleOrder(cake)} 
/>
```

---

## 🎬 Animations

### Framer Motion

Toutes les animations utilisent Framer Motion.

#### Exemples

**Fade In Up**
```tsx
<motion.div
  initial={{ opacity: 0, y: 30 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.6 }}
>
  {/* Contenu */}
</motion.div>
```

**Hover Scale**
```tsx
<motion.div
  whileHover={{ scale: 1.02 }}
  whileTap={{ scale: 0.98 }}
>
  {/* Contenu */}
</motion.div>
```

**Scroll Reveal**
```tsx
<motion.div
  initial={{ opacity: 0 }}
  whileInView={{ opacity: 1 }}
  viewport={{ once: true }}
  transition={{ duration: 0.6 }}
>
  {/* Contenu */}
</motion.div>
```

---

## 🎨 Icônes

### React Icons

Utilise `react-icons` avec différentes bibliothèques :

- **Fi** (Feather Icons) - Interface générale
- **Gi** (Game Icons) - Icônes spécifiques (gâteaux)

```tsx
import { FiShoppingBag, FiHeart, FiCheck } from 'react-icons/fi';
import { GiCakeSlice } from 'react-icons/gi';

<FiShoppingBag size={24} />
<GiCakeSlice color="var(--primary-500)" />
```

---

## 📱 Responsive

### Breakpoints

```css
@media (max-width: 768px) {
  /* Mobile */
}

@media (max-width: 1024px) {
  /* Tablette */
}
```

### Grid Responsive

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: var(--spacing-8);
}
```

---

## 🎨 Polices

### Playfair Display (Titres)

```css
font-family: var(--font-heading);
```

Élégant, serif, parfait pour les titres.

### Inter (Corps)

```css
font-family: var(--font-body);
```

Moderne, lisible, parfait pour le texte.

### Chargement

Les polices sont chargées depuis Google Fonts dans `global.css`.

---

## 🎯 Best Practices

### 1. Toujours utiliser les variables CSS

❌ **Mauvais**
```css
.my-component {
  color: #D4996C;
  padding: 16px;
}
```

✅ **Bon**
```css
.my-component {
  color: var(--primary-500);
  padding: var(--spacing-4);
}
```

### 2. Utiliser les composants UI

❌ **Mauvais**
```tsx
<button className="my-button">
  Cliquer
</button>
```

✅ **Bon**
```tsx
<Button variant="primary">
  Cliquer
</Button>
```

### 3. Wrapper avec Container

❌ **Mauvais**
```tsx
<div style={{ maxWidth: '1280px', margin: '0 auto' }}>
  {/* Contenu */}
</div>
```

✅ **Bon**
```tsx
<Container size="xl">
  {/* Contenu */}
</Container>
```

### 4. Utiliser Section pour les sections

❌ **Mauvais**
```tsx
<div style={{ padding: '80px 0', background: '#F4F1EC' }}>
  {/* Contenu */}
</div>
```

✅ **Bon**
```tsx
<Section variant="primary" padding="lg">
  {/* Contenu */}
</Section>
```

---

## 📦 Import des Composants

### Composants UI (index.ts)

```tsx
import { Button, Card, Input, Badge, Spinner } from '../ui';
```

### Composants individuels

```tsx
import Button from '../ui/Button';
import Container from '../layout/Container';
import PageHeader from '../common/PageHeader';
```

---

## 🎨 Thème Sombre (Futur)

Les variables sont prêtes pour un thème sombre :

```css
[data-theme="dark"] {
  --bg-primary: #1A1A1A;
  --text-primary: #FAFAFA;
  /* ... */
}
```

---

## 📝 Checklist Nouveau Composant

- [ ] Créer le fichier `.tsx` et `.css`
- [ ] Utiliser les variables CSS
- [ ] Ajouter les props TypeScript
- [ ] Implémenter les variantes
- [ ] Ajouter les animations Framer Motion
- [ ] Rendre responsive
- [ ] Exporter depuis `index.ts`
- [ ] Documenter l'utilisation

---

## 🚀 Performances

### Optimisations

1. **Lazy loading** des composants lourds
2. **Memoization** avec React.memo si nécessaire
3. **Animations GPU** (transform, opacity)
4. **Variables CSS** au lieu de JS pour les styles
5. **Tree shaking** automatique avec imports nommés

---

## 📚 Ressources

- [Framer Motion Docs](https://www.framer.com/motion/)
- [React Icons](https://react-icons.github.io/react-icons/)
- [CSS Variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)

---

**Design System créé pour MonGâteau - NAOMIE MOUSSAVOU**

🍰 Architecture moderne, professionnelle et scalable
