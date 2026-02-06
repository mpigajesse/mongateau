const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const CakeSize = sequelize.define('CakeSize', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  cakeId: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: {
      model: 'cakes',
      key: 'id'
    }
  },
  size: {
    type: DataTypes.STRING(50),
    allowNull: false
  },
  price: {
    type: DataTypes.DECIMAL(10, 2),
    allowNull: false
  },
  servings: {
    type: DataTypes.INTEGER,
    allowNull: true
  }
}, {
  tableName: 'cake_sizes',
  timestamps: false
});

module.exports = CakeSize;
