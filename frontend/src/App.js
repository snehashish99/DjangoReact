import logo from './logo.svg';
import './App.css';
import { Component } from 'react';
import axios from 'axios';

class App extends Component {

  constructor(){
    super()
    this.state = {
      all_data: []
    }

    this.fetch_data = this.fetch_data.bind(this)    
  }

  componentDidMount() {
    window.addEventListener('load', this.fetch_data)
  }

  fetch_data()
  {
    let self = this
    fetch('http://127.0.0.1:8000/get-data/')
    .then(response => response.json())
    .then(data => {
      console.log(data)
      self.setState({
        all_data: data['data'],
      })
    })
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log(event)
    let all_data = {}
    for(let i in event.target)
    {
      if(i<6)
      {
        if(event.target[i].value == "")
        {
          alert("Empty field not allowed")
          return
        }
        all_data[event.target[i].name] = event.target[i].value
      }
    }
    console.log(all_data)
    // NOTE: you access FormData fields with `data.get(fieldName)'
    
    axios.get('http://127.0.0.1:8000/submit-data/', {
      params: all_data,
    })
    .then(function (response) {
      console.log(response);
    })
  }

  render(){
    return (
      <div>      
        <form onSubmit={this.handleSubmit}>
          <div className="row">
            <div className="col-sm-6 p-5">
              <div className="form-group">
                <label>Name</label>
                <input type="text" name="name" className="form-control"></input>
              </div>
              <div className="form-group">
                <label>Roll No.</label>
                <input type="text" name="roll" className="form-control"></input>
              </div>
              <div className="form-group">
                <label>Gender</label>
                <select name="gender" className="form-control">
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
              </div>
            </div>
            <div className="col-sm-6 p-5">
              <div className="form-group">
                <label>Marks in physics</label>
                <input type="number" name="physics" min="0" max="100" className="form-control"></input>
              </div>
              <div className="form-group">
                <label>Marks in chemistry</label>
                <input type="number" name="chemistry" min="0" max="100" className="form-control"></input>
              </div>
              <div className="form-group">
                <label>Marks in maths</label>
                <input type="number" name="maths" min="0" max="100" className="form-control"></input>
              </div>
            </div>          
          </div>  
          <div className="row ml-4">
            <div className="form-group">              
              <input type="submit" className="btn btn-info" value="Submit"></input>
            </div>
          </div>        
        </form>        
        <h2 style={{textAlign: "center",width: "100%"}}>Records</h2>          
        <div className="m-5 table-responsive">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Name</th>
                <th>Roll</th>
                <th>Gender</th>
                <th>Physics</th>
                <th>Chemistry</th>
                <th>Maths</th>
                <th>Average</th>
              </tr>
            </thead>
            <tbody>
              {this.state.all_data.map((value, key) => {
                return <tr>
                        <td>{value.name}</td>
                        <td>{value.roll}</td>
                        <td>{value.gender}</td>
                        <td>{value.physics}</td>
                        <td>{value.chemistry}</td>
                        <td>{value.maths}</td>                        
                      </tr>
              })}               
            </tbody>
          </table>
        </div>
      </div>              
    );
  }
}

export default App;
