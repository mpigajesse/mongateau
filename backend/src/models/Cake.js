const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const Cake = sequelize.define('Cake', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  name: {
    type: DataTypes.STRING(100),
    allowNull: false
  },
  description: {
    type: DataTypes.TEXT,
    allowNull: false
  },
  category: {
    type: DataTypes.ENUM('anniversaire', 'mariage', 'enfants', 'personnalise', 'classique', 'special'),
    defaultValue: 'classique'
  },
  basePrice: {
    type: DataTypes.DECIMAL(10, 2),
    allowNull: false
  },
  image: {
    type: DataTypes.STRING(500),
    defaultValue: '/images/default-cake.jpg'
  },
  ingredients: {
    type: DataTypes.ARRAY(DataTypes.STRING),
    defaultValue: []
  },
  allergens: {
    type: DataTypes.ARRAY(DataTypes.STRING),
    defaultValue: []
  },
  available: {
    type: DataTypes.BOOLEAN,
    defaultValue: true
  },
  featured: {
    type: DataTypes.BOOLEAN,
    defaultValue: false
  },
  preparationDays: {
    type: DataTypes.INTEGER,
    defaultValue: 2
  }
}, {
  tableName: 'cakes',
  timestamps: true
});

module.exports = Cake;
