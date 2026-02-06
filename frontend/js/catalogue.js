/**
 * MonGâteau - Catalogue Page Script
 */

document.addEventListener('DOMContentLoaded', () => {
  initFilters();
  loadCakes();
  initMobileMenu();
  
  // Check URL params for initial filter
  const params = new URLSearchParams(window.location.search);
  const category = params.get('category');
  if (category) {
    filterCakes(category);
    // Update active filter button
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.classList.remove('active');
      if (btn.dataset.category === category) {
        btn.classList.add('active');
      }
    });
  }
});

let allCakes = [];

/**
 * Initialize filter buttons
 */
function initFilters() {
  const filters = document.getElementById('filters');
  if (!filters) return;
  
  filters.addEventListener('click', (e) => {
    const btn = e.target.closest('.filter-btn');
    if (!btn) return;
    
    // Update active state
    filters.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    
    // Filter cakes
    const category = btn.dataset.category;
    filterCakes(category);
    
    // Update URL
    const url = new URL(window.location);
    if (category === 'all') {
      url.searchParams.delete('category');
    } else {
      url.searchParams.set('category', category);
    }
    window.history.replaceState({}, '', url);
  });
}

/**
 * Load all cakes
 */
async function loadCakes() {
  const grid = document.getElementById('cakesGrid');
  const loading = document.getElementById('loading');
  const emptyState = document.getElementById('emptyState');
  
  if (!grid) return;
  
  try {
    // Wait for API initialization
    await new Promise(r => setTimeout(r, 100));
    
    allCakes = await getApi().getCakes();
    
    loading.style.display = 'none';
    
    if (allCakes.length === 0) {
      emptyState.style.display = 'block';
      return;
    }
    
    renderCakes(allCakes);
    
  } catch (error) {
    console.error('Error loading cakes:', error);
    loading.innerHTML = '<p class="text-center text-muted">Erreur de chargement</p>';
  }
}

/**
 * Filter cakes by category
 */
function filterCakes(category) {
  const filtered = category === 'all' 
    ? allCakes 
    : allCakes.filter(c => c.category === category);
  
  const emptyState = document.getElementById('emptyState');
  
  if (filtered.length === 0) {
    document.getElementById('cakesGrid').innerHTML = '';
    emptyState.style.display = 'block';
  } else {
    emptyState.style.display = 'none';
    renderCakes(filtered);
  }
}

/**
 * Render cakes to grid
 */
function renderCakes(cakes) {
  const grid = document.getElementById('cakesGrid');
  if (!grid) return;
  
  const categoryLabels = {
    'anniversaire': 'Anniversaire',
    'mariage': 'Mariage',
    'enfants': 'Enfants',
    'personnalise': 'Personnalisé',
    'classique': 'Classique',
    'special': 'Spécial'
  };
  
  grid.innerHTML = cakes.map(cake => {
    const price = cake.sizes?.[0]?.price || cake.basePrice;
    return `
      <div class="cake-card" data-cake-id="${cake.id}">
        <div class="cake-card-image">
          <img src="${cake.image}" alt="${cake.name}" loading="lazy">
          ${cake.featured ? '<span class="cake-card-badge">★ Populaire</span>' : ''}
          <button class="cake-card-favorite" title="Ajouter aux favoris">♡</button>
        </div>
        <div class="cake-card-body">
          <div class="cake-card-category">${categoryLabels[cake.category] || cake.category}</div>
          <h3 class="cake-card-title">${cake.name}</h3>
          <p class="cake-card-description">${cake.description}</p>
          <div class="cake-card-footer">
            <div class="cake-card-price">
              ${Cart.formatPrice(price)}
              <span>/ ${cake.sizes?.[0]?.size || 'pièce'}</span>
            </div>
            <button class="cake-card-btn add-to-cart" title="Ajouter au panier">+</button>
          </div>
        </div>
      </div>
    `;
  }).join('');
  
  // Add event listeners
  grid.querySelectorAll('.cake-card').forEach(card => {
    const addBtn = card.querySelector('.add-to-cart');
    const cakeId = card.dataset.cakeId;
    const cake = cakes.find(c => c.id == cakeId);
    
    addBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (cake) {
        const defaultSize = cake.sizes?.[0] || { size: 'Standard', price: cake.basePrice };
        Cart.addItem(cake, defaultSize.size, defaultSize.price);
      }
    });
    
    card.addEventListener('click', () => {
      showCakeModal(cake);
    });
  });
}

/**
 * Mobile menu toggle
 */
function initMobileMenu() {
  const menuBtn = document.getElementById('mobileMenuBtn');
  const nav = document.getElementById('mobileNav');
  const closeBtn = document.getElementById('mobileNavClose');
  
  if (!menuBtn || !nav) return;
  
  menuBtn.addEventListener('click', () => {
    nav.classList.add('active');
    document.body.style.overflow = 'hidden';
  });
  
  closeBtn?.addEventListener('click', () => {
    nav.classList.remove('active');
    document.body.style.overflow = '';
  });
  
  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('active');
      document.body.style.overflow = '';
    });
  });
}

/**
 * Show cake detail modal (copied from app.js for standalone use)
 */
function showCakeModal(cake) {
  if (!cake) return;
  
  const existingModal = document.getElementById('cakeModal');
  if (existingModal) existingModal.remove();
  
  const modal = document.createElement('div');
  modal.id = 'cakeModal';
  modal.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.6);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
  `;
  
  const sizes = cake.sizes || [{ size: 'Standard', price: cake.basePrice }];
  
  modal.innerHTML = `
    <div class="modal-content" style="
      background: white;
      border-radius: 24px;
      max-width: 800px;
      width: 100%;
      max-height: 90vh;
      overflow: auto;
      position: relative;
    ">
      <button id="closeModal" style="
        position: absolute;
        top: 16px;
        right: 16px;
        background: white;
        border: none;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        font-size: 20px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        z-index: 10;
      ">✕</button>
      
      <div style="display: grid; grid-template-columns: 1fr 1fr;">
        <img src="${cake.image}" alt="${cake.name}" style="width: 100%; height: 100%; min-height: 400px; object-fit: cover; border-radius: 24px 0 0 24px;">
        
        <div style="padding: 32px;">
          <span style="
            display: inline-block;
            background: #E8B4B8;
            color: #4A3728;
            font-size: 12px;
            font-weight: 500;
            padding: 4px 12px;
            border-radius: 20px;
            margin-bottom: 12px;
            text-transform: capitalize;
          ">${cake.category}</span>
          
          <h2 style="font-family: 'Playfair Display', serif; font-size: 28px; margin-bottom: 12px; color: #4A3728;">
            ${cake.name}
          </h2>
          
          <p style="color: #666; margin-bottom: 24px; line-height: 1.6;">
            ${cake.description}
          </p>
          
          <div style="margin-bottom: 24px;">
            <label style="display: block; font-weight: 500; margin-bottom: 8px;">Choisir la taille :</label>
            <div id="sizeOptions" style="display: flex; flex-wrap: wrap; gap: 8px;">
              ${sizes.map((s, i) => `
                <label class="size-option" data-index="${i}" style="
                  display: flex;
                  align-items: center;
                  gap: 8px;
                  padding: 12px 16px;
                  border: 2px solid ${i === 0 ? '#C9956C' : '#ddd'};
                  border-radius: 12px;
                  cursor: pointer;
                  transition: all 0.2s;
                ">
                  <input type="radio" name="size" value="${i}" ${i === 0 ? 'checked' : ''} style="display: none;">
                  <span>${s.size}</span>
                  <strong style="color: #C9956C;">${Cart.formatPrice(s.price)}</strong>
                </label>
              `).join('')}
            </div>
          </div>
          
          <div style="margin-bottom: 24px;">
            <label style="display: block; font-weight: 500; margin-bottom: 8px;">Quantité :</label>
            <div style="display: flex; align-items: center; gap: 12px;">
              <button id="qtyMinus" style="width: 40px; height: 40px; border: 1px solid #ddd; background: #f5f5f5; border-radius: 8px; font-size: 20px; cursor: pointer;">−</button>
              <span id="qtyValue" style="font-weight: 600; font-size: 18px; min-width: 30px; text-align: center;">1</span>
              <button id="qtyPlus" style="width: 40px; height: 40px; border: 1px solid #ddd; background: #f5f5f5; border-radius: 8px; font-size: 20px; cursor: pointer;">+</button>
            </div>
          </div>
          
          <button id="addToCartBtn" class="btn btn-primary" style="width: 100%; padding: 16px; font-size: 16px;">
            Ajouter au panier — <span id="totalPrice">${Cart.formatPrice(sizes[0].price)}</span>
          </button>
        </div>
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
  document.body.style.overflow = 'hidden';
  
  let selectedSizeIndex = 0;
  let quantity = 1;
  
  const updateTotal = () => {
    const price = sizes[selectedSizeIndex].price * quantity;
    document.getElementById('totalPrice').textContent = Cart.formatPrice(price);
  };
  
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.id === 'closeModal') {
      modal.remove();
      document.body.style.overflow = '';
    }
  });
  
  document.querySelectorAll('.size-option').forEach((option) => {
    option.addEventListener('click', () => {
      document.querySelectorAll('.size-option').forEach(o => o.style.borderColor = '#ddd');
      option.style.borderColor = '#C9956C';
      selectedSizeIndex = parseInt(option.dataset.index);
      updateTotal();
    });
  });
  
  document.getElementById('qtyMinus').addEventListener('click', () => {
    if (quantity > 1) {
      quantity--;
      document.getElementById('qtyValue').textContent = quantity;
      updateTotal();
    }
  });
  
  document.getElementById('qtyPlus').addEventListener('click', () => {
    quantity++;
    document.getElementById('qtyValue').textContent = quantity;
    updateTotal();
  });
  
  document.getElementById('addToCartBtn').addEventListener('click', () => {
    const size = sizes[selectedSizeIndex];
    Cart.addItem(cake, size.size, size.price, quantity);
    modal.remove();
    document.body.style.overflow = '';
  });
}
