import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useItems } from '../hooks/useItems';

const ItemsListPage = () => {
  const { items, loadUserItems, loading, error } = useItems();

  useEffect(() => {
    loadUserItems();
  }, []);

  if (loading) return <div>Loading items...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="items-list-page" style={{ padding: '20px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h1>My Items</h1>
        <Link
          to="/create-item"
          style={{
            padding: '10px 20px',
            backgroundColor: '#007bff',
            color: 'white',
            textDecoration: 'none',
            borderRadius: '4px'
          }}
        >
          Add New Item
        </Link>
      </div>

      {items.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '40px' }}>
          <h3>No items found</h3>
          <p>Start by creating your first item!</p>
        </div>
      ) : (
        <div className="items-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '20px' }}>
          {items.map((item) => (
            <div
              key={item.id}
              className="item-card"
              style={{
                border: '1px solid #ddd',
                borderRadius: '8px',
                padding: '20px',
                backgroundColor: 'white',
                boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
              }}
            >
              <h3>{item.name}</h3>
              <p><strong>Price:</strong> ${item.price}</p>
              <p><strong>Quantity:</strong> {item.quantity}</p>
              {item.rarity_display && (
                <p><strong>Rarity:</strong> {item.rarity_display}</p>
              )}
              {item.description && (
                <p><strong>Description:</strong> {item.description}</p>
              )}
              <div style={{ marginTop: '10px', fontSize: '12px', color: '#666' }}>
                Created: {new Date(item.created_at).toLocaleDateString()}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ItemsListPage;