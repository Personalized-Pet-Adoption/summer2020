import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import { QuickSearch } from './Components/quick-search/quick-search.component';

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
    return(
      <div className='App'>
        <QuickSearch placeholder='search pet' handleChange={this.handleChange}/>
        <pet-list pet={filteredPet}/>
      </div>
    )
  }
}



export default App;
