import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import ItemTypeSelector from '../components/ItemTypeSelector';
import TechnicCategorySelector from '../components/TechnicCategorySelector';
import DynamicForm from '../components/DynamicForm';
import { useItems } from '../hooks/useItems';
import { itemService } from '../services/itemService';

const CreateItemPage = () => {
  const navigate = useNavigate();
  const { createItem, createTechnicItem, loading } = useItems();

  const [step, setStep] = useState('itemType'); // itemType, category, subcategory, form
  const [selectedItemType, setSelectedItemType] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [selectedSubcategory, setSelectedSubcategory] = useState(null);
  const [subcategories, setSubcategories] = useState([]);
  const [formFields, setFormFields] = useState({});
  const [formLoading, setFormLoading] = useState(false);

  const handleItemTypeSelect = (itemType) => {
    setSelectedItemType(itemType);
    if (itemType.id === 'technic') {
      setStep('category');
    } else {
      loadFormFields(itemType.id);
      setStep('form');
    }
  };

  const handleCategorySelect = async (category) => {
    setSelectedCategory(category);

    try {
      const response = await itemService.getTechnicSubcategories(category.id);
      setSubcategories(response.data);

      if (response.data.length > 0) {
        setStep('subcategory');
      } else {
        loadTechnicFormFields(category.id);
        setStep('form');
      }
    } catch (error) {
      console.error('Error loading subcategories:', error);
    }
  };

  const handleSubcategorySelect = (subcategory) => {
    setSelectedSubcategory(subcategory);
    loadTechnicFormFields(selectedCategory.id, subcategory.id);
    setStep('form');
  };

  const loadFormFields = async (itemType) => {
    try {
      setFormLoading(true);
      const response = await itemService.getItemFields(itemType);
      setFormFields(response.data.fields);
    } catch (error) {
      console.error('Error loading form fields:', error);
    } finally {
      setFormLoading(false);
    }
  };

  const loadTechnicFormFields = async (category, subcategory = null) => {
    try {
      setFormLoading(true);
      const response = await itemService.getTechnicItemFields(category, subcategory);
      setFormFields(response.data.fields);
    } catch (error) {
      console.error('Error loading technic form fields:', error);
    } finally {
      setFormLoading(false);
    }
  };

  const handleFormSubmit = async (formData) => {
    try {
      if (selectedItemType.id === 'technic') {
        await createTechnicItem(
          selectedCategory.id,
          selectedSubcategory?.id,
          formData
        );
      } else {
        await createItem(selectedItemType.id, formData);
      }

      alert('Item created successfully!');
      navigate('/items');
    } catch (error) {
      console.error('Error creating item:', error);
      alert('Error creating item. Please try again.');
    }
  };

  const renderStepContent = () => {
    switch (step) {
      case 'itemType':
        return <ItemTypeSelector onSelectType={handleItemTypeSelect} />;

      case 'category':
        return <TechnicCategorySelector onSelectCategory={handleCategorySelect} />;

      case 'subcategory':
        return (
          <div>
            <h3>Select Subcategory for {selectedCategory.name}</h3>
            <div className="subcategory-grid">
              {subcategories.map((subcategory) => (
                <div
                  key={subcategory.id}
                  className="subcategory-card"
                  onClick={() => handleSubcategorySelect(subcategory)}
                  style={{
                    border: '1px solid #ccc',
                    padding: '20px',
                    margin: '10px',
                    borderRadius: '8px',
                    cursor: 'pointer',
                    textAlign: 'center'
                  }}
                >
                  <h4>{subcategory.name}</h4>
                </div>
              ))}
              <div
                className="subcategory-card"
                onClick={() => {
                  setSelectedSubcategory(null);
                  loadTechnicFormFields(selectedCategory.id);
                  setStep('form');
                }}
                style={{
                  border: '1px solid #ccc',
                  padding: '20px',
                  margin: '10px',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  textAlign: 'center',
                  backgroundColor: '#f8f9fa'
                }}
              >
                <h4>General {selectedCategory.name}</h4>
              </div>
            </div>
          </div>
        );

      case 'form':
        if (formLoading) {
          return <div>Loading form...</div>;
        }

        return (
          <div>
            <h3>
              Create {selectedItemType.name}
              {selectedCategory && ` - ${selectedCategory.name}`}
              {selectedSubcategory && ` - ${selectedSubcategory.name}`}
            </h3>
            <DynamicForm
              fields={formFields}
              onSubmit={handleFormSubmit}
              loading={loading}
            />
          </div>
        );

      default:
        return null;
    }
  };

  const renderBreadcrumb = () => {
    const breadcrumbs = [];

    if (selectedItemType) {
      breadcrumbs.push(selectedItemType.name);
    }

    if (selectedCategory) {
      breadcrumbs.push(selectedCategory.name);
    }

    if (selectedSubcategory) {
      breadcrumbs.push(selectedSubcategory.name);
    }

    return breadcrumbs.length > 0 ? (
      <div style={{ marginBottom: '20px', padding: '10px', backgroundColor: '#f8f9fa' }}>
        <strong>Selected: </strong>{breadcrumbs.join(' > ')}
      </div>
    ) : null;
  };

  return (
    <div className="create-item-page" style={{ padding: '20px' }}>
      <h1>Create New Item</h1>

      {renderBreadcrumb()}

      {step !== 'itemType' && (
        <button
          onClick={() => {
            if (step === 'form') {
              if (selectedSubcategory) {
                setStep('subcategory');
              } else if (selectedCategory) {
                setStep('category');
              } else {
                setStep('itemType');
              }
            } else if (step === 'subcategory') {
              setStep('category');
            } else if (step === 'category') {
              setStep('itemType');
            }
          }}
          style={{
            marginBottom: '20px',
            padding: '8px 16px',
            backgroundColor: '#6c757d',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          ← Back
        </button>
      )}

      {renderStepContent()}
    </div>
  );
};

export default CreateItemPage;