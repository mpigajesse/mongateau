# 🎂 MonGâteau

Application web de commande de gâteaux en ligne — élégante, moderne et gourmande.

## 📁 Structure

```
mongateau/
├── frontend/           # Interface utilisateur
│   ├── css/           # Styles
│   ├── js/            # Scripts
│   ├── images/        # Assets
│   └── *.html         # Pages
├── backend/           # API Node.js/Express
│   └── src/
│       ├── routes/    # Endpoints API
│       ├── models/    # Modèles Mongoose
│       ├── controllers/
│       └── middleware/
└── README.md
```

## 🚀 Installation

### Backend
```bash
cd backend
npm install
cp .env.example .env
# Configurer MongoDB dans .env
npm run dev
```

### Frontend
```bash
cd frontend
# Ouvrir index.html ou utiliser Live Server
```

## 🎨 Features

- ✅ Catalogue de gâteaux filtrable
- ✅ Panier persistant (localStorage)
- ✅ Formulaire de commande complet
- ✅ API REST complète
- ✅ Design responsive mobile-first
- ✅ Animations fluides

## 🛠 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Backend**: Node.js, Express.js
- **Database**: MongoDB + Mongoose
- **Design**: Mobile-first, tons chauds gourmands

## 📄 License

MIT
