const { Cake, CakeSize } = require('../models');
const { Op } = require('sequelize');

// Get all cakes
exports.getAllCakes = async (req, res) => {
  try {
    const { category, available, featured } = req.query;
    const where = {};
    
    if (category) where.category = category;
    if (available !== undefined) where.available = available === 'true';
    if (featured !== undefined) where.featured = featured === 'true';
    
    const cakes = await Cake.findAll({
      where,
      include: [{ model: CakeSize, as: 'sizes' }],
      order: [['createdAt', 'DESC']]
    });
    res.json(cakes);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Get single cake
exports.getCakeById = async (req, res) => {
  try {
    const cake = await Cake.findByPk(req.params.id, {
      include: [{ model: CakeSize, as: 'sizes' }]
    });
    if (!cake) {
      return res.status(404).json({ error: 'Gâteau non trouvé' });
    }
    res.json(cake);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Create cake
exports.createCake = async (req, res) => {
  try {
    const { sizes, ...cakeData } = req.body;
    const cake = await Cake.create(cakeData);
    
    if (sizes && sizes.length > 0) {
      const sizeRecords = sizes.map(s => ({ ...s, cakeId: cake.id }));
      await CakeSize.bulkCreate(sizeRecords);
    }
    
    const result = await Cake.findByPk(cake.id, {
      include: [{ model: CakeSize, as: 'sizes' }]
    });
    res.status(201).json(result);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// Update cake
exports.updateCake = async (req, res) => {
  try {
    const { sizes, ...cakeData } = req.body;
    const cake = await Cake.findByPk(req.params.id);
    
    if (!cake) {
      return res.status(404).json({ error: 'Gâteau non trouvé' });
    }
    
    await cake.update(cakeData);
    
    if (sizes) {
      await CakeSize.destroy({ where: { cakeId: cake.id } });
      const sizeRecords = sizes.map(s => ({ ...s, cakeId: cake.id }));
      await CakeSize.bulkCreate(sizeRecords);
    }
    
    const result = await Cake.findByPk(cake.id, {
      include: [{ model: CakeSize, as: 'sizes' }]
    });
    res.json(result);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
};

// Delete cake
exports.deleteCake = async (req, res) => {
  try {
    const cake = await Cake.findByPk(req.params.id);
    if (!cake) {
      return res.status(404).json({ error: 'Gâteau non trouvé' });
    }
    await CakeSize.destroy({ where: { cakeId: cake.id } });
    await cake.destroy();
    res.json({ message: 'Gâteau supprimé' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Get featured cakes
exports.getFeaturedCakes = async (req, res) => {
  try {
    const cakes = await Cake.findAll({
      where: { featured: true, available: true },
      include: [{ model: CakeSize, as: 'sizes' }],
      limit: 6
    });
    res.json(cakes);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

// Get categories
exports.getCategories = async (req, res) => {
  try {
    const cakes = await Cake.findAll({
      attributes: ['category'],
      group: ['category']
    });
    const categories = cakes.map(c => c.category);
    res.json(categories);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};
