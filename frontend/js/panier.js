/**
 * MonGâteau - Panier (Cart) Page Script
 */

document.addEventListener('DOMContentLoaded', () => {
  renderCart();
});

/**
 * Render cart page
 */
function renderCart() {
  const items = Cart.getItems();
  const cartItems = document.getElementById('cartItems');
  const emptyCart = document.getElementById('emptyCart');
  const cartLayout = document.getElementById('cartLayout');
  const checkoutBtn = document.getElementById('checkoutBtn');
  
  if (items.length === 0) {
    cartLayout.style.display = 'none';
    emptyCart.style.display = 'block';
    return;
  }
  
  cartLayout.style.display = 'grid';
  emptyCart.style.display = 'none';
  
  cartItems.innerHTML = items.map((item, index) => `
    <div class="cart-item" data-index="${index}">
      <img src="${item.image}" alt="${item.cakeName}" class="cart-item-image">
      <div class="cart-item-details">
        <h4 class="cart-item-title">${item.cakeName}</h4>
        <p class="cart-item-options">${item.size}</p>
        ${item.customMessage ? `<p class="cart-item-options"><em>"${item.customMessage}"</em></p>` : ''}
        <div class="cart-item-quantity">
          <button class="qty-btn qty-minus">−</button>
          <span class="qty-value">${item.quantity}</span>
          <button class="qty-btn qty-plus">+</button>
        </div>
      </div>
      <div style="text-align: right;">
        <div class="cart-item-price">${Cart.formatPrice(item.price * item.quantity)}</div>
        <button class="cart-item-remove" title="Supprimer">🗑️</button>
      </div>
    </div>
  `).join('');
  
  // Update totals
  updateTotals();
  
  // Enable/disable checkout
  checkoutBtn.style.pointerEvents = items.length > 0 ? 'auto' : 'none';
  checkoutBtn.style.opacity = items.length > 0 ? '1' : '0.5';
  
  // Add event listeners
  cartItems.querySelectorAll('.cart-item').forEach(item => {
    const index = parseInt(item.dataset.index);
    
    item.querySelector('.qty-minus').addEventListener('click', () => {
      const items = Cart.getItems();
      const newQty = items[index].quantity - 1;
      Cart.updateQuantity(index, newQty);
      renderCart();
    });
    
    item.querySelector('.qty-plus').addEventListener('click', () => {
      const items = Cart.getItems();
      Cart.updateQuantity(index, items[index].quantity + 1);
      renderCart();
    });
    
    item.querySelector('.cart-item-remove').addEventListener('click', () => {
      Cart.removeItem(index);
      renderCart();
    });
  });
}

/**
 * Update totals display
 */
function updateTotals() {
  const subtotal = Cart.getSubtotal();
  const deliveryFee = Cart.getDeliveryFee();
  const total = subtotal + deliveryFee;
  
  document.getElementById('subtotal').textContent = Cart.formatPrice(subtotal);
  document.getElementById('deliveryFee').textContent = Cart.formatPrice(deliveryFee);
  document.getElementById('total').textContent = Cart.formatPrice(total);
}
