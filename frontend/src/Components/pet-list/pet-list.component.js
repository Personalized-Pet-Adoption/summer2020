import React from 'react';
import './pet-list.styles.css'
import {Pet} from '../pet/pet.component';

export const PetList = props => {
return (<div className = 'pet-list'>{
    props.pets.map(pet => 
      <Pet key={pet.id} pet = {pet}> {pet.name} </Pet>)
    } 
    </div>)
};