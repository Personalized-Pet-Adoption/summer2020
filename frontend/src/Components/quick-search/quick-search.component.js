import React from 'react';

import './quick-search.styles.css';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button'
export const QuickSearch=({placeholder,handleChange})=>
(
<input 
    className ='search'    
    type='search' 
    placeholder={placeholder} 
    onChange={handleChange}/> 
)
    