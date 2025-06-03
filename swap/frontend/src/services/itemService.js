import apiClient from './api';

export const itemService = {
  // Get item types
  getItemTypes: () => apiClient.get('/item-types/'),

  // Get technic categories
  getTechnicCategories: () => apiClient.get('/technic/categories/'),

  // Get technic subcategories
  getTechnicSubcategories: (category) =>
    apiClient.get(`/technic/categories/${category}/subcategories/`),

  // Get form fields for item creation
  getItemFields: (itemType) => apiClient.get(`/items/${itemType}/`),

  // Get form fields for technic item creation
  getTechnicItemFields: (category, subcategory = null) => {
    const url = subcategory
      ? `/technic/${category}/${subcategory}/`
      : `/technic/${category}/`;
    return apiClient.get(url);
  },

  // Create item
  createItem: (itemType, data) => apiClient.post(`/items/${itemType}/`, data),

  // Create technic item
  createTechnicItem: (category, subcategory = null, data) => {
    const url = subcategory
      ? `/technic/${category}/${subcategory}/`
      : `/technic/${category}/`;
    return apiClient.post(url, data);
  },

  // Get user items
  getUserItems: () => apiClient.get('/my-items/'),

  // Get specific item
  getItem: (id) => apiClient.get(`/my-items/${id}/`),
};