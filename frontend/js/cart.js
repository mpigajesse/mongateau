/**
 * MonGâteau - Cart Management
 * Handles cart state with localStorage persistence
 */

const CART_KEY = 'mongateau_cart';

const Cart = {
  /**
   * Get cart items from localStorage
   */
  getItems() {
    try {
      const data = localStorage.getItem(CART_KEY);
      return data ? JSON.parse(data) : [];
    } catch {
      return [];
    }
  },
  
  /**
   * Save cart to localStorage
   */
  save(items) {
    localStorage.setItem(CART_KEY, JSON.stringify(items));
    this.updateUI();
  },
  
  /**
   * Add item to cart
   */
  addItem(cake, size, price, quantity = 1, customMessage = '') {
    const items = this.getItems();
    
    // Check if item already exists
    const existingIndex = items.findIndex(
      item => item.cakeId === cake.id && item.size === size
    );
    
    if (existingIndex > -1) {
      items[existingIndex].quantity += quantity;
    } else {
      items.push({
        cakeId: cake.id,
        cakeName: cake.name,
        image: cake.image,
        size,
        price: parseFloat(price),
        quantity,
        customMessage
      });
    }
    
    this.save(items);
    this.showNotification(`${cake.name} ajouté au panier !`);
    return items;
  },
  
  /**
   * Update item quantity
   */
  updateQuantity(index, quantity) {
    const items = this.getItems();
    if (index >= 0 && index < items.length) {
      if (quantity <= 0) {
        items.splice(index, 1);
      } else {
        items[index].quantity = quantity;
      }
      this.save(items);
    }
    return items;
  },
  
  /**
   * Remove item from cart
   */
  removeItem(index) {
    const items = this.getItems();
    if (index >= 0 && index < items.length) {
      items.splice(index, 1);
      this.save(items);
    }
    return items;
  },
  
  /**
   * Clear cart
   */
  clear() {
    localStorage.removeItem(CART_KEY);
    this.updateUI();
  },
  
  /**
   * Get cart count
   */
  getCount() {
    const items = this.getItems();
    return items.reduce((sum, item) => sum + item.quantity, 0);
  },
  
  /**
   * Get subtotal
   */
  getSubtotal() {
    const items = this.getItems();
    return items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  },
  
  /**
   * Get delivery fee
   */
  getDeliveryFee() {
    return 5.00;
  },
  
  /**
   * Get total
   */
  getTotal() {
    return this.getSubtotal() + this.getDeliveryFee();
  },
  
  /**
   * Format price
   */
  formatPrice(price) {
    return new Intl.NumberFormat('fr-FR', {
      style: 'currency',
      currency: 'EUR'
    }).format(price);
  },
  
  /**
   * Update cart count in header
   */
  updateUI() {
    const countEl = document.getElementById('cartCount');
    if (countEl) {
      const count = this.getCount();
      countEl.textContent = count;
      countEl.style.display = count > 0 ? 'flex' : 'none';
    }
  },
  
  /**
   * Show add to cart notification
   */
  showNotification(message) {
    // Remove existing notification
    const existing = document.querySelector('.cart-notification');
    if (existing) existing.remove();
    
    // Create notification
    const notification = document.createElement('div');
    notification.className = 'cart-notification';
    notification.innerHTML = `
      <span>✓ ${message}</span>
      <a href="panier.html">Voir le panier</a>
    `;
    notification.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: var(--chocolate);
      color: white;
      padding: 16px 24px;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.2);
      display: flex;
      align-items: center;
      gap: 16px;
      z-index: 9999;
      animation: slideUp 0.3s ease;
    `;
    
    const link = notification.querySelector('a');
    link.style.cssText = `
      color: var(--caramel-light);
      font-weight: 500;
      text-decoration: none;
    `;
    
    document.body.appendChild(notification);
    
    // Remove after 3s
    setTimeout(() => {
      notification.style.animation = 'fadeOut 0.3s ease forwards';
      setTimeout(() => notification.remove(), 300);
    }, 3000);
  }
};

// Initialize cart UI on page load
document.addEventListener('DOMContentLoaded', () => {
  Cart.updateUI();
});

// Add notification animations
const style = document.createElement('style');
style.textContent = `
  @keyframes slideUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
  }
  @keyframes fadeOut {
    to { transform: translateY(20px); opacity: 0; }
  }
`;
document.head.appendChild(style);
