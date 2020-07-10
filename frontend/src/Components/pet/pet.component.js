import React from 'react';
import './pet.styles.css';

export const Pet = props =>(
    <div className = 'pet-container'>
        <img alt = "pet"   />
        <h2>
            {props.Pet}
        </h2>
        <p>{props.Pet.name}</p> 
    </div>
);