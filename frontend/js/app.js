/**
 * MonGâteau - Main Application Script
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize components
  initHeader();
  initMobileMenu();
  loadFeaturedCakes();
});

/**
 * Header scroll effect
 */
function initHeader() {
  const header = document.getElementById('header');
  if (!header) return;
  
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
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
  
  // Close on link click
  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('active');
      document.body.style.overflow = '';
    });
  });
}

/**
 * Load featured cakes on homepage
 */
async function loadFeaturedCakes() {
  const container = document.getElementById('featuredCakes');
  if (!container) return;
  
  try {
    // Wait for API to initialize
    await new Promise(r => setTimeout(r, 100));
    
    const cakes = await getApi().getFeaturedCakes();
    
    if (cakes.length === 0) {
      container.innerHTML = '<p class="text-center text-muted">Aucun gâteau disponible pour le moment.</p>';
      return;
    }
    
    container.innerHTML = cakes.slice(0, 6).map(cake => createCakeCard(cake)).join('');
    
    // Add click handlers
    container.querySelectorAll('.cake-card').forEach(card => {
      card.addEventListener('click', (e) => {
        // Don't navigate if clicking add button
        if (e.target.closest('.cake-card-btn')) {
          e.preventDefault();
          const cakeId = card.dataset.cakeId;
          const cake = cakes.find(c => c.id == cakeId);
          if (cake) {
            const defaultSize = cake.sizes?.[0] || { size: 'Standard', price: cake.basePrice };
            Cart.addItem(cake, defaultSize.size, defaultSize.price);
          }
        } else {
          // Navigate to product page (or show modal)
          showCakeModal(cakes.find(c => c.id == card.dataset.cakeId));
        }
      });
    });
    
  } catch (error) {
    console.error('Error loading cakes:', error);
    container.innerHTML = '<p class="text-center text-muted">Erreur de chargement. Veuillez réessayer.</p>';
  }
}

/**
 * Create cake card HTML
 */
function createCakeCard(cake) {
  const price = cake.sizes?.[0]?.price || cake.basePrice;
  const categoryLabels = {
    'anniversaire': 'Anniversaire',
    'mariage': 'Mariage',
    'enfants': 'Enfants',
    'personnalise': 'Personnalisé',
    'classique': 'Classique',
    'special': 'Spécial'
  };
  
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
          <button class="cake-card-btn" title="Ajouter au panier">+</button>
        </div>
      </div>
    </div>
  `;
}

/**
 * Show cake detail modal
 */
function showCakeModal(cake) {
  if (!cake) return;
  
  // Remove existing modal
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
    animation: fadeIn 0.2s ease;
  `;
  
  const sizes = cake.sizes || [{ size: 'Standard', price: cake.basePrice }];
  
  modal.innerHTML = `
    <div style="
      background: white;
      border-radius: 24px;
      max-width: 800px;
      width: 100%;
      max-height: 90vh;
      overflow: auto;
      display: grid;
      grid-template-columns: 1fr 1fr;
      animation: slideUp 0.3s ease;
    ">
      <div style="position: relative;">
        <img src="${cake.image}" alt="${cake.name}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 24px 0 0 24px;">
      </div>
      <div style="padding: 32px;">
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
        ">✕</button>
        
        <span style="
          display: inline-block;
          background: #E8B4B8;
          color: #4A3728;
          font-size: 12px;
          font-weight: 500;
          padding: 4px 12px;
          border-radius: 20px;
          margin-bottom: 12px;
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
              <label style="
                display: flex;
                align-items: center;
                gap: 8px;
                padding: 12px 16px;
                border: 2px solid ${i === 0 ? '#C9956C' : '#ddd'};
                border-radius: 12px;
                cursor: pointer;
                transition: all 0.2s;
              " class="size-option ${i === 0 ? 'selected' : ''}">
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
            <button id="qtyMinus" style="
              width: 40px;
              height: 40px;
              border: 1px solid #ddd;
              background: #f5f5f5;
              border-radius: 8px;
              font-size: 20px;
              cursor: pointer;
            ">−</button>
            <span id="qtyValue" style="font-weight: 600; font-size: 18px; min-width: 30px; text-align: center;">1</span>
            <button id="qtyPlus" style="
              width: 40px;
              height: 40px;
              border: 1px solid #ddd;
              background: #f5f5f5;
              border-radius: 8px;
              font-size: 20px;
              cursor: pointer;
            ">+</button>
          </div>
        </div>
        
        <button id="addToCartBtn" class="btn btn-primary btn-lg" style="width: 100%;">
          Ajouter au panier — <span id="totalPrice">${Cart.formatPrice(sizes[0].price)}</span>
        </button>
        
        ${cake.ingredients ? `
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid #eee;">
            <strong style="font-size: 14px;">Ingrédients :</strong>
            <p style="color: #888; font-size: 14px; margin-top: 4px;">${cake.ingredients.join(', ')}</p>
          </div>
        ` : ''}
      </div>
    </div>
  `;
  
  document.body.appendChild(modal);
  document.body.style.overflow = 'hidden';
  
  // State
  let selectedSizeIndex = 0;
  let quantity = 1;
  
  const updateTotal = () => {
    const price = sizes[selectedSizeIndex].price * quantity;
    document.getElementById('totalPrice').textContent = Cart.formatPrice(price);
  };
  
  // Event listeners
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.id === 'closeModal') {
      modal.remove();
      document.body.style.overflow = '';
    }
  });
  
  document.querySelectorAll('.size-option').forEach((option, i) => {
    option.addEventListener('click', () => {
      document.querySelectorAll('.size-option').forEach(o => {
        o.style.borderColor = '#ddd';
        o.classList.remove('selected');
      });
      option.style.borderColor = '#C9956C';
      option.classList.add('selected');
      option.querySelector('input').checked = true;
      selectedSizeIndex = i;
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
