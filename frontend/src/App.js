import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import {Route} from 'react-router-dom';
// import { Switch, Route } from 'react-router-dom';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import './App.css';
import Container from 'react-bootstrap/Container';
import 'bootstrap/dist/css/bootstrap.min.css';
import {QuickSearch} from './Components/quick-search/quick-search.component';
import {PetList} from './Components/pet-list/pet-list.component'
import ShopPage from './pages/shop/shop.component.jsx';
import DropdownButton from 'react-bootstrap/DropdownButton'
import Dropdown from 'react-bootstrap/Dropdown'
import { Route,Link, Switch, BrowserRouter, Router} from 'react-router-dom';
// import { Link } from 'react-router';
// import { DatePicker } from 'antd';
// import { Row, Col } from 'antd';
import Header from './Components/header/header.component.jsx';


const API = "https://petadoption-284220.uc.r.appspot.com/pets/"// 'https://jsonplaceholder.typicode.com/users';

class App extends Component{
  constructor(){
    super();
    this.state={
      pet:[],
      searchField:''
    };
    
    this.handleChange=this.handleChange.bind(this);
  }

  componentDidMount(){
    fetch(API)
    .results//('https://jsonplaceholder.typicode.com/users')
    .then(response=>console.log(response.json().data))
    .then(pets=>this.setState({pet:pets}));
    console.log("haaha")
    console.log(this.state);
    console.log("done")
    console.log(fetch('https://petadoption-284220.uc.r.appspot.com/pets/'
      // body:JSON.stringify(options)
    ).then(function(res){ return res.json()}))
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
      <BrowserRouter>
      <Switch>
          {/* <Route exact path = '/' component={App}/> */}
          <Route exact path = '/shop' component = {ShopPage}/>
        </Switch>
      </BrowserRouter>
      <Navbar bg="light" expand="lg">
  <Navbar.Brand href="#home">
    {/* <Link to='/shop'> */}
    Adopt a pet
    {/* </Link> */}
    </Navbar.Brand>
  <Navbar.Toggle aria-controls="basic-navbar-nav" />
  <Navbar.Collapse id="basic-navbar-nav">
    <Nav className="mr-auto">
    {/* <Route exact path='/' component={HomePage} /> */}
      {/* <Nav.Link exact path='/' component={ShopPage} >Home</Nav.Link>
      <Nav.Link href="#link">Link</Nav.Link> */}
    </Nav>
    <Container>
  {/* <Row>
    <Col xs={6} md={4}>
      <Image style={{width:"3rem"}} src="https://s3-eu-west-1.amazonaws.com/w3.cdn.gpd/gb.pedigree.55/large_53b66497-3a2d-420c-a567-b1e0ae5c5823.jpg" roundedCircle />
    </Col>
  </Row> */}
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

