import React, { useEffect, useState } from 'react';
import { itemService } from '../services/itemService';

const TechnicCategorySelector = ({ onSelectCategory }) => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadCategories = async () => {
      try {
        setLoading(true);
        const response = await itemService.getTechnicCategories();
        setCategories(response.data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    loadCategories();
  }, []);

  if (loading) return <div>Loading categories...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="category-selector">
      <h3>Select Technic Category</h3>
      <div className="category-grid">
        {categories.map((category) => (
          <div
            key={category.id}
            className="category-card"
            onClick={() => onSelectCategory(category)}
            style={{
              border: '1px solid #ccc',
              padding: '20px',
              margin: '10px',
              borderRadius: '8px',
              cursor: 'pointer',
              textAlign: 'center'
            }}
          >
            <h4>{category.name}</h4>
            <p>{category.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TechnicCategorySelector;