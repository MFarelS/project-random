import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

class Product extends React.Component {
  state = {
    order: 0
  }
  
  handleCounterChange = (value) => {
    this.props.onCounterChange(value)
  }
  
  handlePlus = () => {
    this.setState({
      order: this.state.order + 1
    }, () => {
      this.handleCounterChange(this.state.order)
    })
  }
  
  handleMinus = () => {
    if (this.state.order > 0){
      this.setState({
        order: this.state.order - 1
      }, () => {
        this.handleCounterChange(this.state.order)
      })
    }
  }
  
  render(){
    return (
      <div className="card" style={{boxShadow: 'rgba(0, 0, 0, 0.24) 0px 3px 8px'}}>
        <img src="https://baksojwr.com/wp-content/uploads/2018/02/2-1.jpg" className="card-img-top" alt="..."/>
        <div className="card-body">
          <h6 className="card-title">Mie Bakso yang rasanya enak banged</h6>
          <p className="card-text" style={{color:'orange',fontWeight:'bold'}}>Rp15.000</p>
          <div className="input-group mb-3">
            <button className="btn btn-primary" type="button" id="buttonKurang" onClick={this.handleMinus}> - </button>
            <input type="number" className="form-control" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1" value={this.state.order} style={{textAlign: "center"}} disabled/>
            <button className="btn btn-primary" type="button" id="buttonTambah" onClick={this.handlePlus}> + </button>
          </div>
        </div>
      </div>
    )
  }
}

export default Product