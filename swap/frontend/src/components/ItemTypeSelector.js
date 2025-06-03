import React, { useEffect } from 'react';
import { useItems } from '../hooks/useItems';

const ItemTypeSelector = ({ onSelectType }) => {
  const { itemTypes, loadItemTypes, loading, error } = useItems();

  useEffect(() => {
    loadItemTypes();
  }, []);

  if (loading) return <div>Loading item types...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="item-type-selector">
      <h3>Select Item Type</h3>
      <div className="type-grid">
        {itemTypes.map((type) => (
          <div
            key={type.id}
            className="type-card"
            onClick={() => onSelectType(type)}
            style={{
              border: '1px solid #ccc',
              padding: '20px',
              margin: '10px',
              borderRadius: '8px',
              cursor: 'pointer',
              textAlign: 'center'
            }}
          >
            <h4>{type.name}</h4>
            <p>{type.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ItemTypeSelector;