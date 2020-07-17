import React from 'react';

import './quick-search.styles.css';

export const QuickSearch=({placeholder,handleChange})=>(<input 
    className ='search'    
    type='search' 
    placeholder={placeholder} 
    onChange={handleChange}/>)
    