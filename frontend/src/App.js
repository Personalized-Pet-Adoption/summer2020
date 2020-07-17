import React, {Component} from 'react';
// import { Switch, Route } from 'react-router-dom';

import './App.css';
import {QuickSearch} from './Components/quick-search/quick-search.component';
import {PetList} from './Components/pet-list/pet-list.component'
import ShopPage from './pages/shop/shop.component.jsx';


// import HomePage from './pages/homepage/homepage.component';
// import ShopPage from './pages/shop/shop.component.jsx';
import Header from './Components/header/header.component.jsx';
import AdvanceSearch from './Components/advance-search/advance-search.component';
import NavBar from './Components/navigation-bar/navigation-bar.component';
class App extends Component{
  constructor(){
    super();
    this.state={
      pet:[{'id':1,'name':'lu',email:'tliu1@macalester.edu'},
      {'id':2,'name':'huahua',email:'tliu1@macalester.edu'},
      {'id':3,'name':'tianrui',email:'tliu1@macalester.edu'}],
      searchField:''
    };
    
    this.handleChange=this.handleChange.bind(this);
  }
  componentDidMount(){
    fetch('https://jsonplaceholder.typicode.com/users')
    .then(response=>response.json())
    .then(users=>this.setState({monsters:users}));
  }
  handleChange=(e)=>{
    this.setState({searchField:e.target.value});
  };

  render(){
    const {pet, searchField}=this.state;
    const filteredPet=pet.filter(pet=>
      pet.name.toLowerCase().includes(searchField.toLowerCase())
    )
  return (
    <div>
      <Header />
      <AdvanceSearch />
      <NavBar />

      {/* <Switch> */}
        {/* <Route exact path='/' component={HomePage} /> */}
        {/* <Route path='/shop' component={ShopPage} /> */}
      {/* </Switch> */}
        <QuickSearch 
          placeholder='search pet' 
          handleChange={this.handleChange}
        />
      <PetList pets = {filteredPet} />
    </div>
  );
}
}



export default App;