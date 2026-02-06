const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const OrderItem = sequelize.define('OrderItem', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  orderId: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: {
      model: 'orders',
      key: 'id'
    }
  },
  cakeId: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: {
      model: 'cakes',
      key: 'id'
    }
  },
  cakeName: {
    type: DataTypes.STRING(100),
    allowNull: false
  },
  size: {
    type: DataTypes.STRING(50)
  },
  price: {
    type: DataTypes.DECIMAL(10, 2),
    allowNull: false
  },
  quantity: {
    type: DataTypes.INTEGER,
    defaultValue: 1
  },
  customMessage: {
    type: DataTypes.STRING(200)
  }
}, {
  tableName: 'order_items',
  timestamps: false
});

module.exports = OrderItem;
