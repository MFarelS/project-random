import logo from './logo.svg';
import React from 'react';
import './App.css';

const Header = () => {
  return(
    <div class=row>
      <div class="mx-auto col-12 col-lg-6">
        <div class="text-center card my-2">
          <div class="card-header pb-0 pt-4">
            <img src={this.props.gambar} height="150px" alt="" class="mx-auto d-block mb-3 rounded-circle"/>
            <h1 class="mb-0 title">
              {this.props.nama}
            </h1>
            <br/>
          </div>
        </div>
      </div>
    </div>
  )
}

function App() {
  return (
    <div class="text-center container" style="min-height:100%;">
      <Header gambar="https://tfkhdyt.web.app/assets/img/me.jpg" nama="Taufik Hidayat"/>
    </div>
  )
}

export default App;