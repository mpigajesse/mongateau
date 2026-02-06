/**
 * Seed script - Populate database with sample cakes
 * Run: npm run db:seed
 */

require('dotenv').config({ path: require('path').join(__dirname, '../../.env') });
const { sequelize, Cake, CakeSize } = require('../models');

const sampleCakes = [
  {
    name: 'Délice Chocolat Noir',
    description: 'Un gâteau intense au chocolat noir 70%, ganache onctueuse et copeaux de chocolat. Pour les vrais amateurs de cacao.',
    category: 'classique',
    basePrice: 35.00,
    image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600&h=400&fit=crop',
    ingredients: ['Chocolat noir 70%', 'Crème fraîche', 'Beurre', 'Œufs', 'Farine'],
    allergens: ['Gluten', 'Œufs', 'Lait'],
    available: true,
    featured: true,
    preparationDays: 2,
    sizes: [
      { size: '6 parts', price: 35.00, servings: 6 },
      { size: '8 parts', price: 45.00, servings: 8 },
      { size: '12 parts', price: 60.00, servings: 12 }
    ]
  },
  {
    name: 'Fraisier Royal',
    description: 'Génoise légère, crème mousseline à la vanille de Madagascar et fraises fraîches de saison. Un classique indémodable.',
    category: 'classique',
    basePrice: 40.00,
    image: 'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600&h=400&fit=crop',
    ingredients: ['Fraises fraîches', 'Crème pâtissière', 'Génoise', 'Vanille Madagascar'],
    allergens: ['Gluten', 'Œufs', 'Lait'],
    available: true,
    featured: true,
    preparationDays: 1,
    sizes: [
      { size: '6 parts', price: 40.00, servings: 6 },
      { size: '8 parts', price: 52.00, servings: 8 },
      { size: '12 parts', price: 70.00, servings: 12 }
    ]
  },
  {
    name: 'Étoile d\'Anniversaire',
    description: 'Gâteau festif personnalisable avec votre message. Génoise vanille, crème au beurre et décoration colorée.',
    category: 'anniversaire',
    basePrice: 45.00,
    image: 'https://images.unsplash.com/photo-1558636508-e0db3814bd1d?w=600&h=400&fit=crop',
    ingredients: ['Génoise vanille', 'Crème au beurre', 'Fondant', 'Décorations comestibles'],
    allergens: ['Gluten', 'Œufs', 'Lait'],
    available: true,
    featured: true,
    preparationDays: 2,
    sizes: [
      { size: '8 parts', price: 45.00, servings: 8 },
      { size: '12 parts', price: 65.00, servings: 12 },
      { size: '20 parts', price: 95.00, servings: 20 }
    ]
  },
  {
    name: 'Wedding Cake Élégance',
    description: 'Pièce montée sur mesure pour votre mariage. Trois étages, décoration florale en sucre, saveur au choix.',
    category: 'mariage',
    basePrice: 250.00,
    image: 'https://images.unsplash.com/photo-1535254973040-607b474cb50d?w=600&h=400&fit=crop',
    ingredients: ['Génoise', 'Crème', 'Pâte à sucre', 'Fleurs en sucre'],
    allergens: ['Gluten', 'Œufs', 'Lait'],
    available: true,
    featured: false,
    preparationDays: 5,
    sizes: [
      { size: '30 parts', price: 250.00, servings: 30 },
      { size: '50 parts', price: 380.00, servings: 50 },
      { size: '80 parts', price: 550.00, servings: 80 }
    ]
  },
  {
    name: 'Licorne Magique',
    description: 'Gâteau féerique pour les enfants ! Arc-en-ciel de couleurs, licorne en pâte à sucre et paillettes comestibles.',
    category: 'enfants',
    basePrice: 55.00,
    image: 'https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=600&h=400&fit=crop',
    ingredients: ['Génoise vanille', 'Crème colorée', 'Pâte à sucre', 'Paillettes comestibles'],
    allergens: ['Gluten', 'Œufs', 'Lait'],
    available: true,
    featured: true,
    preparationDays: 3,
    sizes: [
      { size: '10 parts', price: 55.00, servings: 10 },
      { size: '15 parts', price: 75.00, servings: 15 },
      { size: '20 parts', price: 95.00, servings: 20 }
    ]
  },
  {
    name: 'Tarte Citron Meringuée',
    description: 'Pâte sablée croustillante, crème citron acidulée et meringue italienne caramélisée au chalumeau.',
    category: 'classique',
    basePrice: 30.00,
    image: 'https://images.unsplash.com/photo-1519915028121-7d3463d20b13?w=600&h=400&fit=crop',
    ingredients: ['Citrons frais', 'Meringue', 'Pâte sablée', 'Beurre'],
    allergens: ['Gluten', 'Œufs', 'Lait'],
    available: true,
    featured: false,
    preparationDays: 1,
    sizes: [
      { size: '6 parts', price: 30.00, servings: 6 },
      { size: '8 parts', price: 38.00, servings: 8 }
    ]
  },
  {
    name: 'Number Cake Personnalisé',
    description: 'Gâteau en forme de chiffre ou lettre, garni de crème, fruits frais et macarons. Parfait pour les anniversaires !',
    category: 'personnalise',
    basePrice: 65.00,
    image: 'https://images.unsplash.com/photo-1562440499-64c9a111f713?w=600&h=400&fit=crop',
    ingredients: ['Pâte sablée', 'Crème mascarpone', 'Fruits frais', 'Macarons', 'Fleurs comestibles'],
    allergens: ['Gluten', 'Œufs', 'Lait', 'Fruits à coque'],
    available: true,
    featured: true,
    preparationDays: 2,
    sizes: [
      { size: '1 chiffre (10 parts)', price: 65.00, servings: 10 },
      { size: '2 chiffres (20 parts)', price: 120.00, servings: 20 }
    ]
  },
  {
    name: 'Forêt Noire Traditionnelle',
    description: 'Le grand classique ! Génoise au cacao, cerises griottes, chantilly et copeaux de chocolat.',
    category: 'classique',
    basePrice: 38.00,
    image: 'https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?w=600&h=400&fit=crop',
    ingredients: ['Cacao', 'Cerises griottes', 'Chantilly', 'Kirsch', 'Chocolat'],
    allergens: ['Gluten', 'Œufs', 'Lait', 'Alcool'],
    available: true,
    featured: false,
    preparationDays: 2,
    sizes: [
      { size: '6 parts', price: 38.00, servings: 6 },
      { size: '8 parts', price: 48.00, servings: 8 },
      { size: '12 parts', price: 65.00, servings: 12 }
    ]
  }
];

async function seed() {
  try {
    await sequelize.authenticate();
    console.log('✅ Connecté à PostgreSQL');
    
    await sequelize.sync({ force: true });
    console.log('✅ Tables créées');
    
    for (const cakeData of sampleCakes) {
      const { sizes, ...cake } = cakeData;
      const createdCake = await Cake.create(cake);
      
      if (sizes && sizes.length > 0) {
        const sizeRecords = sizes.map(s => ({ ...s, cakeId: createdCake.id }));
        await CakeSize.bulkCreate(sizeRecords);
      }
      console.log(`   🎂 ${cake.name} créé`);
    }
    
    console.log('\n✅ Base de données initialisée avec', sampleCakes.length, 'gâteaux !');
    process.exit(0);
  } catch (error) {
    console.error('❌ Erreur:', error.message);
    process.exit(1);
  }
}

seed();
