import React from 'react';
import './pet.styles.css';

export const Pet = props =>(
    <div className = 'pet-container'>
        <img alt = "pet" src={`https://www.pexels.com/search/pet/?set=set2&size=180x180`} />
        <h2>
            {props.Pet}
        </h2>
        <p>{props.Pet.name}</p> 
    </div>
);