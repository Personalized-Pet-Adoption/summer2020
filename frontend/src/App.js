import React, {Component} from 'react';
import ReactDOM from 'react-dom';
// import { Switch, Route } from 'react-router-dom';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import './App.css';
import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';
import 'bootstrap/dist/css/bootstrap.min.css';
import {QuickSearch} from './Components/quick-search/quick-search.component';
import {PetList} from './Components/pet-list/pet-list.component'
import ShopPage from './pages/shop/shop.component.jsx';
import DropdownButton from 'react-bootstrap/DropdownButton'
import Dropdown from 'react-bootstrap/Dropdown'
// import { DatePicker } from 'antd';
// import { Row, Col } from 'antd';
import Header from './Components/header/header.component.jsx';

// import AdvanceSearch from './Components/advance-search/advance-search.component';
// import NavBar from './Components/navigation-bar/navigation-bar.component';
class App extends Component{
  constructor(){
    super();
    this.state={
      pet:[{'id':1,'name':'lu',email:'tliu1@macalester.edu'},
      {'id':2,'name':'huahua',email:'tliu1@macalester.edu'},
      {'id':3,'name':'tianrui',email:'tliu1@macalester.edu'}, 
      {'id':3,'name':'tianrui',email:'tliu1@macalester.edu'},
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
      
      {/* <AdvanceSearch /> */}
      {/* <NavBar /> */}

      <Navbar bg="light" expand="lg">
  <Navbar.Brand href="#home">Adopt a pet</Navbar.Brand>
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
        <NavDropdown.Item href="#action/3.3">Browsing History</NavDropdown.Item>
        <NavDropdown.Divider />
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

