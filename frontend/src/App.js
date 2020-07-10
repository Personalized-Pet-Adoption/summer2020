import React from 'react';
import logo from './logo.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

class App extends Component{
  constructor(){
    super();
    this.state={
      pets:[],
      searchField:''
    };
    this.handleChange=this.handleChange.bind(this);
  }

  handleChange=(e)=>{
    this.setState({searchField:e.target.value});
  };

  render(){
    const {pets, searchField}=this.state;
    const filteredPets=pets.filter(pet=>
      pet.name.toLowerCase().includes(searchField.toLowerCase())
    )
    return(
      <div className='App'>
        <SearchBox placeholder='search pet' handleChange={this.handleChange}/>
        <PetList pets={filteredPets}/>
      </div>
    )
  }
}



export default App;
