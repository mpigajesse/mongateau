const { Order, OrderItem, Cake } = require('../models');

// Create order
exports.createOrder = async (req, res) => {
  try {
    const { items, ...orderData } = req.body;
    
    // Calculate totals
    const subtotal = items.reduce((sum, item) => sum + (parseFloat(item.price) * item.quantity), 0);
    const deliveryFee = 5.00;
    const total = subtotal + deliveryFee;
    
    const order = await Order.create({
      ...orderData,
      subtotal,
      deliveryFee,
      total
    });
    
    // Create order items
    if (items && items.length > 0) {
      const itemRecords = items.map(item => ({
        ...item,
        orderId: order.id
      }));
      await OrderItem.bulkCreate(itemRecords);
    }
    
    const result = await Order.findByPk(order.id, {
      include: [{ model: OrderItem, as: 'items' }]
    });
    
    res.status(201).json(result);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// Get all orders
exports.getAllOrders = async (req, res) => {
  try {
    const { status } = req.query;
    const where = status ? { status } : {};
    
    const orders = await Order.findAll({
      where,
      include: [{ 
        model: OrderItem, 
        as: 'items',
        include: [{ model: Cake, as: 'cake' }]
      }],
      order: [['createdAt', 'DESC']]
    });
    res.json(orders);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Get order by ID
exports.getOrderById = async (req, res) => {
  try {
    const order = await Order.findByPk(req.params.id, {
      include: [{ 
        model: OrderItem, 
        as: 'items',
        include: [{ model: Cake, as: 'cake' }]
      }]
    });
    if (!order) {
      return res.status(404).json({ error: 'Commande non trouvée' });
    }
    res.json(order);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Get order by order number
exports.getOrderByNumber = async (req, res) => {
  try {
    const order = await Order.findOne({
      where: { orderNumber: req.params.orderNumber },
      include: [{ model: OrderItem, as: 'items' }]
    });
    if (!order) {
      return res.status(404).json({ error: 'Commande non trouvée' });
    }
    res.json(order);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Update order status
exports.updateOrderStatus = async (req, res) => {
  try {
    const { status } = req.body;
    const order = await Order.findByPk(req.params.id);
    
    if (!order) {
      return res.status(404).json({ error: 'Commande non trouvée' });
    }
    
    await order.update({ status });
    res.json(order);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// Cancel order
exports.cancelOrder = async (req, res) => {
  try {
    const order = await Order.findByPk(req.params.id);
    if (!order) {
      return res.status(404).json({ error: 'Commande non trouvée' });
    }
    if (['delivered', 'cancelled'].includes(order.status)) {
      return res.status(400).json({ error: 'Impossible d\'annuler cette commande' });
    }
    await order.update({ status: 'cancelled' });
    res.json(order);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};
