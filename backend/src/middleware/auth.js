// Simple auth middleware placeholder
// In production, implement JWT or session-based auth

exports.isAuthenticated = (req, res, next) => {
  // TODO: Implement proper authentication
  // For now, allow all requests
  next();
};

exports.isAdmin = (req, res, next) => {
  // TODO: Implement admin check
  // For now, allow all requests
  next();
};
