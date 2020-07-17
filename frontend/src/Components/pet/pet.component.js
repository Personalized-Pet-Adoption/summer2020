import React from 'react';
import './pet.styles.css';

export const Pet = props =>(
    <div className = 'pet-container'>
        <img alt = "pet" src={`https://s3-eu-west-1.amazonaws.com/w3.cdn.gpd/gb.pedigree.55/large_53b66497-3a2d-420c-a567-b1e0ae5c5823.jpg`} />
        <h2>
            {props.pet.name}
        </h2>
        <p>{props.pet.name}</p> 
    </div>
);