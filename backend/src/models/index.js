const sequelize = require('../config/database');
const Cake = require('./Cake');
const CakeSize = require('./CakeSize');
const Order = require('./Order');
const OrderItem = require('./OrderItem');
const User = require('./User');

// Cake has many sizes
Cake.hasMany(CakeSize, { foreignKey: 'cakeId', as: 'sizes' });
CakeSize.belongsTo(Cake, { foreignKey: 'cakeId' });

// Order has many items
Order.hasMany(OrderItem, { foreignKey: 'orderId', as: 'items' });
OrderItem.belongsTo(Order, { foreignKey: 'orderId' });

// OrderItem references Cake
OrderItem.belongsTo(Cake, { foreignKey: 'cakeId', as: 'cake' });

// User has many orders
User.hasMany(Order, { foreignKey: 'userId', as: 'orders' });
Order.belongsTo(User, { foreignKey: 'userId' });

module.exports = {
  sequelize,
  Cake,
  CakeSize,
  Order,
  OrderItem,
  User
};
