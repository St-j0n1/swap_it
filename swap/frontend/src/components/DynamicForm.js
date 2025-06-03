import React, { useState, useEffect } from 'react';

const DynamicForm = ({ fields, onSubmit, loading }) => {
  const [formData, setFormData] = useState({});
  const [errors, setErrors] = useState({});

  useEffect(() => {
    // Initialize form data with default values
    const initialData = {};
    Object.keys(fields).forEach(fieldName => {
      const field = fields[fieldName];
      initialData[fieldName] = field.choices ? '' : '';
    });
    setFormData(initialData);
  }, [fields]);

  const handleChange = (fieldName, value) => {
    setFormData(prev => ({
      ...prev,
      [fieldName]: value
    }));

    // Clear error when user starts typing
    if (errors[fieldName]) {
      setErrors(prev => ({
        ...prev,
        [fieldName]: null
      }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Basic validation
    const newErrors = {};
    Object.keys(fields).forEach(fieldName => {
      const field = fields[fieldName];
      if (field.required && !formData[fieldName]) {
        newErrors[fieldName] = `${field.label} is required`;
      }
    });

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    try {
      await onSubmit(formData);
      // Reset form after successful submission
      const resetData = {};
      Object.keys(fields).forEach(fieldName => {
        resetData[fieldName] = '';
      });
      setFormData(resetData);
    } catch (error) {
      console.error('Form submission error:', error);
    }
  };

  const renderField = (fieldName, field) => {
    const value = formData[fieldName] || '';
    const error = errors[fieldName];

    const baseProps = {
      id: fieldName,
      name: fieldName,
      value: value,
      onChange: (e) => handleChange(fieldName, e.target.value),
      required: field.required,
      style: error ? { borderColor: 'red' } : {}
    };

    let inputElement;

    if (field.choices && field.choices.length > 0) {
      inputElement = (
        <select {...baseProps}>
          <option value="">Select {field.label}</option>
          {field.choices.map(choice => (
            <option key={choice.value} value={choice.value}>
              {choice.display}
            </option>
          ))}
        </select>
      );
    } else if (field.type === 'BooleanField') {
      inputElement = (
        <input
          type="checkbox"
          {...baseProps}
          checked={value}
          onChange={(e) => handleChange(fieldName, e.target.checked)}
        />
      );
    } else if (field.type === 'IntegerField' || field.type === 'DecimalField') {
      inputElement = <input type="number" {...baseProps} />;
    } else if (field.type === 'TextField') {
      inputElement = <textarea {...baseProps} rows="4" />;
    } else {
      inputElement = <input type="text" {...baseProps} />;
    }

    return (
      <div key={fieldName} className="form-field" style={{ marginBottom: '15px' }}>
        <label htmlFor={fieldName} style={{ display: 'block', marginBottom: '5px' }}>
          {field.label} {field.required && <span style={{ color: 'red' }}>*</span>}
        </label>
        {inputElement}
        {field.help_text && (
          <small style={{ color: '#666', display: 'block', marginTop: '5px' }}>
            {field.help_text}
          </small>
        )}
        {error && (
          <div style={{ color: 'red', fontSize: '14px', marginTop: '5px' }}>
            {error}
          </div>
        )}
      </div>
    );
  };

  return (
    <form onSubmit={handleSubmit} className="dynamic-form">
      {Object.keys(fields).map(fieldName => renderField(fieldName, fields[fieldName]))}

      <button
        type="submit"
        disabled={loading}
        style={{
          padding: '10px 20px',
          backgroundColor: loading ? '#ccc' : '#007bff',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: loading ? 'not-allowed' : 'pointer'
        }}
      >
        {loading ? 'Creating...' : 'Create Item'}
      </button>
    </form>
  );
};

export default DynamicForm;