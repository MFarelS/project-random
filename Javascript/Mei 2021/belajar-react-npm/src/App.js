//import logo from './logo.svg';
import React from 'react';
import './App.css';
import ReactTooltip from "react-tooltip";

const copyNomer = (nomor) => {
  var dummy = document.createElement("textarea");
  document.body.appendChild(dummy);
  dummy.value = nomor;
  dummy.select();
  document.execCommand("copy");
  document.body.removeChild(dummy);
}

const Header = (props) => {
  return(
    <div class="row">
      <div class="mx-auto col-12 col-lg-6">
        <div class="text-center card my-2">
          <div class="card-header pb-0 pt-4">
            <img src={props.gambar} height="150px" alt="" class="mx-auto d-block mb-3 rounded-circle" />
            <h1 class="mb-0 title">
              {props.nama}
            </h1>
            <br />
    </div>
    </div>
    </div>
    </div>
  )
}

const Tab = (props) => {
  return(
    <li class={props.kelasLi} role="presentation">
    <button class={props.kelasA}
      aria-controls={props.nama}
      aria-selected="true"
      data-bs-target={props.id}
      data-bs-toggle="tab"
      id={props.tab}
      role="tab">{props.title}</button>
    </li>
  )
}

const ThreeButton = (props) => {
  return(
    <div>
    <button onMouseOver={() => copyNomer('0895338865375')}  type="button" class="btn btn-outline-primary mb-1" data-tip="Nomor telah disalin" data-event="click" data-effect="solid" data-delay-hide='500'><i class="fa fa-mobile-alt"></i> {props.nomor}</button><br/>
      <button class="btn btn-primary" data-bs-target={props.modal} data-bs-toggle="modal">
          <i class="fas fa-qrcode"></i> QR Code
      </button>&nbsp;
      <a href={props.link} class="btn btn-success" target="_blank" rel="noreferrer"><i class="fas fa-external-link-alt"></i> Buka {props.nama}</a>
      <ReactTooltip globalEventOff="click" />
    </div>
  );
}

const TwoButton = (props) => {
  return(
    <div>
    <button onMouseOver={() => copyNomer('0895338865375')}  type="button" class="btn btn-outline-primary mb-1" data-tip="Nomor telah disalin" data-event="click" data-effect="solid" data-delay-hide='500'><i class="fa fa-mobile-alt"></i> {props.nomor}</button>&nbsp;
      <button class="btn btn-primary" data-bs-target={props.modal} data-bs-toggle="modal">
          <i class="fas fa-qrcode"></i> QR Code
      </button>
      <ReactTooltip globalEventOff="click" />
    </div>
  );
}

const CardBody = (props) => {
  if(props.nama === "OVO"){
    return(
      <div class="fade tab-pane show active" id={props.id} aria-labelledby={props.tab} role="tabpanel">
        <h5 class="card-title">Support me via {props.nama}</h5>
        <p class="card-text my-4">
          <img src="https://tfkhdyt.web.app/assets/img/ovo.svg" alt="" height="50vh"/>
        </p>
        <p class="card-text">
          
          <ThreeButton nama={props.nama}
                       nomor={props.nomor}
                       modal={props.modal}
                       link={props.link}
          />
        </p>
      </div>
    )
  }else if(props.nama === "LinkAja"){
    return(
      <div class="fade tab-pane show active" id={props.id} aria-labelledby={props.tab} role="tabpanel">
        <h5 class="card-title">Support me via {props.nama}</h5>
        <p class="card-text my-4">
          <img src="https://tfkhdyt.web.app/assets/img/ovo.svg" alt="" height="50vh"/>
        </p>
        <p class="card-text">
          
          <TwoButton nama={props.nama}
                       nomor={props.nomor}
                       modal={props.modal}
                       link={props.link}
          />
        </p>
      </div>
    )
  }
}

const Body = () => {
  return(
      <div class="row">
      <div class="mx-auto col-12 col-lg-6">
        <div class="text-center card">
          <div class="card-header">
            <ul class="card-header-pills nav nav-pills nav-fill" id="myTabs" role="tablist">
              <Tab kelasLi="nav-item mx-auto" kelasA="nav-link active" nama="ovo" id="#ovo" tab="ovo-tab" title="OVO" />
              <Tab kelasLi="nav-item" kelasA="nav-link" nama="linkaja" id="#linkaja" tab="linkaja-tab" title="LinkAja" />
              <Tab kelasLi="nav-item" kelasA="nav-link" nama="dana" id="#dana" tab="dana-tab" title="Dana" />
              <Tab kelasLi="nav-item" kelasA="nav-link" nama="gopay" id="#gopay" tab="gopay-tab" title="Gopay" />
              <Tab kelasLi="nav-item" kelasA="nav-link" nama="paypal" id="#paypal" tab="paypal-tab" title="PayPal" />
              <Tab kelasLi="nav-item" kelasA="nav-link" nama="saweria" id="#saweria" tab="saweria-tab" title="Saweria" />
              <Tab kelasLi="nav-item" kelasA="nav-link" nama="Trakteer" id="#trakteer" tab="trakteer-tab" title="Trakteer" />
            </ul>
          </div>
          <div class="card-body">
            <div class="tab-content" id="myTabsContent">
              <CardBody id="#ovo"
                        tab="ovo-tab"
                        nama="OVO"
                        nomor="0895338865375"
                        modal="#modalOvo"
                        link="ovo://transfer"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

function App() {
    return (
      <div class="text-center container">
      <Header gambar="https://tfkhdyt.web.app/assets/img/me.jpg" nama="Taufik Hidayat" />
      <Body />
      </div>
    )
    }

export default App;