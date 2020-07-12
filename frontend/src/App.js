import React, {Component} from 'react';
// import { Switch, Route } from 'react-router-dom';

import './App.css';
import {QuickSearch} from './Components/quick-search/quick-search.component';


// import HomePage from './pages/homepage/homepage.component';
// import ShopPage from './pages/shop/shop.component.jsx';
import Header from './Components/header/header.component.jsx';

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
      <QuickSearch placeholder='search pet' handleChange={this.handleChange}/>

      {/* <Switch> */}
        {/* <Route exact path='/' component={HomePage} /> */}
        {/* <Route path='/shop' component={ShopPage} /> */}
      {/* </Switch> */}
    </div>
  );
}
}



export default App;