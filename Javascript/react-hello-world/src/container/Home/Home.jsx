import React, {Component} from 'react'
import YoutubeComp from '../../component/YoutubeComp/YoutubeComp'
import './Home.css';

class Home extends Component {
  render() {
    return (
      <div>
        <h1>YouChoob</h1>
        <hr/>
        <YoutubeComp 
          title="Source Code CRUD Node.js"
          desc='9x ditonton, 4 hari yang lalu'/>
        <YoutubeComp 
          title='Ngoding Java di Termux'
          desc='123 x ditonton, 3 bulan yang lalu'/>
        <YoutubeComp 
          title='Tutorial Download di Mega'
          desc='59 x ditonton, 3 bulan yang lalu'/>
        <YoutubeComp 
          title='Tutorial Convert Stiker ke WA'
          desc='22 x ditonton, 3 bulan yang lalu'/>
        <YoutubeComp/>
      </div>
    )
  }
}

export default Home