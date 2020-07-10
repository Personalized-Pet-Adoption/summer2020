import React from 'react';
import './pet-list.styles.css'
import {Pet} from '../pet/pet.component';

export const PetList = props => {
    console.log(props);
return (<div className = 'pet-list'>{
    props.Pet.map(pet => 
      <Card key={pet.id} pet = {pet}> {pet.name} </Card>)
    } 
    </div>)
};