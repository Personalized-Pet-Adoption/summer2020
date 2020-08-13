import React, {Component} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {QuickSearch} from './Components/quick-search/quick-search.component';
import {PetList} from './Components/pet-list/pet-list.component'
import ShopPage from './pages/shop/shop.component.jsx';
import { Link, Switch, BrowserRouter, Router, withRouter, Route} from 'react-router-dom';
import {Navbar, Nav, NavDropdown, Button, Form, FormControl, Container, Dropdown} from 'react-bootstrap';
import Header from './Components/header/header.component.jsx';

const API = 'https://petadoption-284220.uc.r.appspot.com/pets/';

class App extends Component{
  constructor(){
    super();
    this.state={
      pet:[],
      searchField:''
    };
    
    this.handleChange=this.handleChange.bind(this);
  }
  componentDidMount (){
    let res = fetch(API).then(function(response) {
      return response.json();
    })
    .then( pets => 
      this.setState({pet: pets.results}))
  }
  
  
  handleChange=(e)=>{
    this.setState({searchField:e.target.value});
  };

  render(){
    const {pet, searchField}=this.state;
    console.log(pet)
    const filteredPet=pet.filter(pet=>
      pet.name.toLowerCase().includes(searchField.toLowerCase())
    )
  return (
    <div>
      <BrowserRouter>
        <Switch>
          <Route exact path = '/shop' exact component = {ShopPage}/>
        </Switch>
      </BrowserRouter>
      <Navbar bg="light" expand="lg">
  <Navbar.Brand href="#home">
    Adopt a pet
    </Navbar.Brand>
  <Navbar.Toggle aria-controls="basic-navbar-nav" />
  <Navbar.Collapse id="basic-navbar-nav">
    <Nav className="mr-auto">
    </Nav>
    <Container>
</Container>
    <NavDropdown title="My username" id="basic-nav-dropdown">
        <NavDropdown.Item href="#action/3.1">My favorites</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.2">Trade Board</NavDropdown.Item>
        <NavDropdown.Item>  
          <BrowserRouter>
              <Switch>
                <Route path = '/shop' component={ShopPage}> Browsing History</Route> 
              </Switch>
          </BrowserRouter>
          {/* <Link to = {ShopPage}>Browsing History</Link> */}
          </NavDropdown.Item>
        <NavDropdown.Divider/>
        <NavDropdown.Item href="#action/3.4">Log out</NavDropdown.Item>
      </NavDropdown>
  </Navbar.Collapse>
    <Form inline>
      <FormControl type="text" placeholder="Search" className="mr-sm-2" />
      <Button variant="outline-success">Search</Button>
    </Form>
   
</Navbar>
 
<Header />

<div>
<Dropdown style={{ margin: '2rem', width : '40ox' }} >
  <Dropdown.Toggle variant="success" id="dropdown-basic">
    Cats Only
  </Dropdown.Toggle>
  <Dropdown.Menu>
    <Dropdown.Item href="#/action-1">Dogs Only</Dropdown.Item>
    <Dropdown.Item href="#/action-2">Cats and Dogs</Dropdown.Item>
  </Dropdown.Menu>
</Dropdown>
<Dropdown style={{ margin: '2rem' }} >
  <Dropdown.Toggle variant="success" id="dropdown-basic">
  within 5 miles
  </Dropdown.Toggle>
  <Dropdown.Menu>
    <Dropdown.Item href="#/action-1">within 5 miles</Dropdown.Item>
    <Dropdown.Item href="#/action-2">wihtin 10 miles</Dropdown.Item>
  </Dropdown.Menu>
</Dropdown>



<Form inline style={{ margin: '2rem' }}  >
      <FormControl type="text" placeholder="Search" className="mr-sm-2" />
      <Button variant="outline-success">Search</Button>
    </Form>
{/* <QuickSearch inline placeholder='search pet' handleChange={this.handleChange}/> */}
</div>

      {/* <Switch> */}
        {/* <Route exact path='/' component={HomePage} /> */}
        {/* <Route path='/shop' component={ShopPage} /> */}
      {/* </Switch> */}

      <PetList pets = {filteredPet} />
    </div>
  );
}
}



export default App;

