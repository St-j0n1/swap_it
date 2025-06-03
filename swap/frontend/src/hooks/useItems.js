import { useEffect } from 'react';
import { useItemContext } from '../context/ItemContext';
import { itemService } from '../services/itemService';

export const useItems = () => {
  const { state, dispatch } = useItemContext();

  const loadItemTypes = async () => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true });
      const response = await itemService.getItemTypes();
      dispatch({ type: 'SET_ITEM_TYPES', payload: response.data });
    } catch (error) {
      dispatch({ type: 'SET_ERROR', payload: error.message });
    }
  };

  const loadTechnicCategories = async () => {
    try {
      const response = await itemService.getTechnicCategories();
      dispatch({ type: 'SET_TECHNIC_CATEGORIES', payload: response.data });
    } catch (error) {
      dispatch({ type: 'SET_ERROR', payload: error.message });
    }
  };

  const loadUserItems = async () => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true });
      const response = await itemService.getUserItems();
      dispatch({ type: 'SET_ITEMS', payload: response.data });
    } catch (error) {
      dispatch({ type: 'SET_ERROR', payload: error.message });
    }
  };

  const createItem = async (itemType, data) => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true });
      const response = await itemService.createItem(itemType, data);
      dispatch({ type: 'ADD_ITEM', payload: response.data });
      return response.data;
    } catch (error) {
      dispatch({ type: 'SET_ERROR', payload: error.message });
      throw error;
    }
  };

  const createTechnicItem = async (category, subcategory, data) => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true });
      const response = await itemService.createTechnicItem(category, subcategory, data);
      dispatch({ type: 'ADD_ITEM', payload: response.data });
      return response.data;
    } catch (error) {
      dispatch({ type: 'SET_ERROR', payload: error.message });
      throw error;
    }
  };

  return {
    ...state,
    loadItemTypes,
    loadTechnicCategories,
    loadUserItems,
    createItem,
    createTechnicItem,
    setSelectedItemType: (type) => dispatch({ type: 'SET_SELECTED_ITEM_TYPE', payload: type }),
    setSelectedCategory: (category) => dispatch({ type: 'SET_SELECTED_CATEGORY', payload: category }),
    setSelectedSubcategory: (subcategory) => dispatch({ type: 'SET_SELECTED_SUBCATEGORY', payload: subcategory }),
    clearError: () => dispatch({ type: 'CLEAR_ERROR' }),
  };
};