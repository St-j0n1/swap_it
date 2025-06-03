import React, { createContext, useContext, useReducer } from 'react';

const ItemContext = createContext();

const initialState = {
  items: [],
  itemTypes: [],
  technicCategories: [],
  loading: false,
  error: null,
  selectedItemType: null,
  selectedCategory: null,
  selectedSubcategory: null,
};

const itemReducer = (state, action) => {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, loading: action.payload };
    case 'SET_ERROR':
      return { ...state, error: action.payload, loading: false };
    case 'SET_ITEMS':
      return { ...state, items: action.payload, loading: false };
    case 'SET_ITEM_TYPES':
      return { ...state, itemTypes: action.payload };
    case 'SET_TECHNIC_CATEGORIES':
      return { ...state, technicCategories: action.payload };
    case 'SET_SELECTED_ITEM_TYPE':
      return { ...state, selectedItemType: action.payload };
    case 'SET_SELECTED_CATEGORY':
      return { ...state, selectedCategory: action.payload };
    case 'SET_SELECTED_SUBCATEGORY':
      return { ...state, selectedSubcategory: action.payload };
    case 'ADD_ITEM':
      return { ...state, items: [...state.items, action.payload] };
    case 'CLEAR_ERROR':
      return { ...state, error: null };
    default:
      return state;
  }
};

export const ItemProvider = ({ children }) => {
  const [state, dispatch] = useReducer(itemReducer, initialState);

  return (
    <ItemContext.Provider value={{ state, dispatch }}>
      {children}
    </ItemContext.Provider>
  );
};

export const useItemContext = () => {
  const context = useContext(ItemContext);
  if (!context) {
    throw new Error('useItemContext must be used within ItemProvider');
  }
  return context;
};