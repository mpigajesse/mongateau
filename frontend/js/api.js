/**
 * MonGâteau - API Service
 * Handles all API calls to the backend
 */

const API_BASE = 'http://localhost:3000/api';

const api = {
  /**
   * Fetch all cakes with optional filters
   */
  async getCakes(filters = {}) {
    const params = new URLSearchParams();
    if (filters.category && filters.category !== 'all') {
      params.append('category', filters.category);
    }
    if (filters.available !== undefined) {
      params.append('available', filters.available);
    }
    if (filters.featured !== undefined) {
      params.append('featured', filters.featured);
    }
    
    const url = `${API_BASE}/cakes${params.toString() ? '?' + params : ''}`;
    const response = await fetch(url);
    if (!response.ok) throw new Error('Erreur lors du chargement des gâteaux');
    return response.json();
  },
  
  /**
   * Fetch featured cakes
   */
  async getFeaturedCakes() {
    const response = await fetch(`${API_BASE}/cakes/featured`);
    if (!response.ok) throw new Error('Erreur lors du chargement');
    return response.json();
  },
  
  /**
   * Fetch single cake by ID
   */
  async getCake(id) {
    const response = await fetch(`${API_BASE}/cakes/${id}`);
    if (!response.ok) throw new Error('Gâteau non trouvé');
    return response.json();
  },
  
  /**
   * Fetch available categories
   */
  async getCategories() {
    const response = await fetch(`${API_BASE}/cakes/categories`);
    if (!response.ok) throw new Error('Erreur lors du chargement');
    return response.json();
  },
  
  /**
   * Create a new order
   */
  async createOrder(orderData) {
    const response = await fetch(`${API_BASE}/orders`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(orderData)
    });
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.error || 'Erreur lors de la commande');
    }
    return response.json();
  },
  
  /**
   * Track order by number
   */
  async trackOrder(orderNumber) {
    const response = await fetch(`${API_BASE}/orders/track/${orderNumber}`);
    if (!response.ok) throw new Error('Commande non trouvée');
    return response.json();
  },
  
  /**
   * Health check
   */
  async health() {
    try {
      const response = await fetch(`${API_BASE}/health`);
      return response.ok;
    } catch {
      return false;
    }
  }
};

// Sample data for when API is not available (demo mode)
const sampleCakes = [
  {
    id: 1,
    name: 'Délice Chocolat Noir',
    description: 'Un gâteau intense au chocolat noir 70%, ganache onctueuse et copeaux de chocolat.',
    category: 'classique',
    basePrice: 35.00,
    image: 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=600&h=400&fit=crop',
    ingredients: ['Chocolat noir 70%', 'Crème fraîche', 'Beurre'],
    available: true,
    featured: true,
    sizes: [
      { size: '6 parts', price: 35.00 },
      { size: '8 parts', price: 45.00 },
      { size: '12 parts', price: 60.00 }
    ]
  },
  {
    id: 2,
    name: 'Fraisier Royal',
    description: 'Génoise légère, crème mousseline à la vanille et fraises fraîches de saison.',
    category: 'classique',
    basePrice: 40.00,
    image: 'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600&h=400&fit=crop',
    available: true,
    featured: true,
    sizes: [
      { size: '6 parts', price: 40.00 },
      { size: '8 parts', price: 52.00 }
    ]
  },
  {
    id: 3,
    name: 'Étoile d\'Anniversaire',
    description: 'Gâteau festif personnalisable avec votre message. Génoise vanille et crème au beurre.',
    category: 'anniversaire',
    basePrice: 45.00,
    image: 'https://images.unsplash.com/photo-1558636508-e0db3814bd1d?w=600&h=400&fit=crop',
    available: true,
    featured: true,
    sizes: [
      { size: '8 parts', price: 45.00 },
      { size: '12 parts', price: 65.00 }
    ]
  },
  {
    id: 4,
    name: 'Wedding Cake Élégance',
    description: 'Pièce montée sur mesure pour votre mariage. Trois étages, décoration florale.',
    category: 'mariage',
    basePrice: 250.00,
    image: 'https://images.unsplash.com/photo-1535254973040-607b474cb50d?w=600&h=400&fit=crop',
    available: true,
    featured: false,
    sizes: [
      { size: '30 parts', price: 250.00 },
      { size: '50 parts', price: 380.00 }
    ]
  },
  {
    id: 5,
    name: 'Licorne Magique',
    description: 'Gâteau féerique pour les enfants ! Arc-en-ciel de couleurs et paillettes comestibles.',
    category: 'enfants',
    basePrice: 55.00,
    image: 'https://images.unsplash.com/photo-1621303837174-89787a7d4729?w=600&h=400&fit=crop',
    available: true,
    featured: true,
    sizes: [
      { size: '10 parts', price: 55.00 },
      { size: '15 parts', price: 75.00 }
    ]
  },
  {
    id: 6,
    name: 'Number Cake Personnalisé',
    description: 'Gâteau en forme de chiffre, garni de crème, fruits frais et macarons.',
    category: 'personnalise',
    basePrice: 65.00,
    image: 'https://images.unsplash.com/photo-1562440499-64c9a111f713?w=600&h=400&fit=crop',
    available: true,
    featured: true,
    sizes: [
      { size: '1 chiffre', price: 65.00 },
      { size: '2 chiffres', price: 120.00 }
    ]
  }
];

// Demo mode API wrapper
const demoApi = {
  async getCakes(filters = {}) {
    await new Promise(r => setTimeout(r, 300)); // Simulate loading
    let cakes = [...sampleCakes];
    if (filters.category && filters.category !== 'all') {
      cakes = cakes.filter(c => c.category === filters.category);
    }
    if (filters.featured) {
      cakes = cakes.filter(c => c.featured);
    }
    return cakes;
  },
  
  async getFeaturedCakes() {
    return this.getCakes({ featured: true });
  },
  
  async getCake(id) {
    await new Promise(r => setTimeout(r, 200));
    return sampleCakes.find(c => c.id === parseInt(id));
  }
};

// Check if API is available, fallback to demo
let useDemo = false;

async function initApi() {
  const apiAvailable = await api.health();
  useDemo = !apiAvailable;
  if (useDemo) {
    console.log('🎂 MonGâteau - Mode Démo (Backend non connecté)');
  } else {
    console.log('🎂 MonGâteau - API connectée');
  }
}

function getApi() {
  return useDemo ? demoApi : api;
}

// Initialize on load
initApi();
