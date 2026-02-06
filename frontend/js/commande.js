/**
 * MonGâteau - Commande (Checkout) Page Script
 */

document.addEventListener('DOMContentLoaded', () => {
  initOrderPage();
  initForm();
});

/**
 * Initialize order page
 */
function initOrderPage() {
  const items = Cart.getItems();
  
  // Redirect if cart is empty
  if (items.length === 0) {
    window.location.href = 'catalogue.html';
    return;
  }
  
  // Render order items summary
  const orderItems = document.getElementById('orderItems');
  orderItems.innerHTML = items.map(item => `
    <div style="display: flex; gap: 12px; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #eee;">
      <img src="${item.image}" alt="${item.cakeName}" style="width: 60px; height: 60px; border-radius: 8px; object-fit: cover;">
      <div style="flex: 1;">
        <div style="font-weight: 500;">${item.cakeName}</div>
        <div style="font-size: 14px; color: #888;">${item.size} × ${item.quantity}</div>
      </div>
      <div style="font-weight: 600; color: #C9956C;">${Cart.formatPrice(item.price * item.quantity)}</div>
    </div>
  `).join('');
  
  // Update totals
  updateTotals();
  
  // Set minimum delivery date (2 days from now)
  const minDate = new Date();
  minDate.setDate(minDate.getDate() + 2);
  const dateInput = document.getElementById('deliveryDate');
  dateInput.min = minDate.toISOString().split('T')[0];
  dateInput.value = minDate.toISOString().split('T')[0];
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

/**
 * Initialize form handling
 */
function initForm() {
  const form = document.getElementById('orderForm');
  
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '⏳ Traitement en cours...';
    
    try {
      const formData = new FormData(form);
      const items = Cart.getItems();
      
      const orderData = {
        firstName: formData.get('firstName'),
        lastName: formData.get('lastName'),
        email: formData.get('email'),
        phone: formData.get('phone'),
        address: formData.get('address'),
        city: formData.get('city'),
        postalCode: formData.get('postalCode'),
        deliveryDate: formData.get('deliveryDate'),
        deliveryTimeSlot: formData.get('deliveryTimeSlot'),
        deliveryInstructions: formData.get('deliveryInstructions'),
        paymentMethod: formData.get('paymentMethod'),
        notes: formData.get('notes'),
        items: items.map(item => ({
          cakeId: item.cakeId,
          cakeName: item.cakeName,
          size: item.size,
          price: item.price,
          quantity: item.quantity,
          customMessage: item.customMessage
        }))
      };
      
      // Try to send to API
      let orderNumber;
      
      try {
        const result = await api.createOrder(orderData);
        orderNumber = result.orderNumber;
      } catch (apiError) {
        // Demo mode - generate fake order number
        console.log('API unavailable, using demo mode');
        orderNumber = 'MG' + new Date().getFullYear() + String(new Date().getMonth() + 1).padStart(2, '0') + '-' + String(Math.floor(Math.random() * 9000) + 1000);
      }
      
      // Clear cart
      Cart.clear();
      
      // Show success modal
      document.getElementById('orderNumber').textContent = orderNumber;
      document.getElementById('successModal').style.display = 'flex';
      
    } catch (error) {
      console.error('Order error:', error);
      alert('Erreur lors de la commande: ' + error.message);
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
    }
  });
}
