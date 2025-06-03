import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ItemProvider } from './context/ItemContext';
import CreateItemPage from './pages/CreateItemPage';
import ItemsListPage from './pages/ItemsListPage';

function App() {
  return (
    <ItemProvider>
      <Router>
        <div className="App">
          <nav style={{
            padding: '1rem',
            backgroundColor: '#f8f9fa',
            borderBottom: '1px solid #dee2e6',
            marginBottom: '20px'
          }}>
            <div style={{ display: 'flex', gap: '20px' }}>
              <a href="/items" style={{ textDecoration: 'none', color: '#007bff' }}>My Items</a>
              <a href="/create-item" style={{ textDecoration: 'none', color: '#007bff' }}>Create Item</a>
            </div>
          </nav>

          <Routes>
            <Route path="/" element={<Navigate to="/items" replace />} />
            <Route path="/items" element={<ItemsListPage />} />
            <Route path="/create-item" element={<CreateItemPage />} />
          </Routes>
        </div>
      </Router>
    </ItemProvider>
  );
}

export default App;