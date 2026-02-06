const express = require('express');
const router = express.Router();
const cakeController = require('../controllers/cakeController');

// Public routes
router.get('/', cakeController.getAllCakes);
router.get('/featured', cakeController.getFeaturedCakes);
router.get('/categories', cakeController.getCategories);
router.get('/:id', cakeController.getCakeById);

// Admin routes (add auth middleware later)
router.post('/', cakeController.createCake);
router.put('/:id', cakeController.updateCake);
router.delete('/:id', cakeController.deleteCake);

module.exports = router;
