module.exports = {
  port: process.env.PORT || 3000,
  frontendUrl: process.env.FRONTEND_URL || 'http://localhost:5500',
  nodeEnv: process.env.NODE_ENV || 'development'
};
