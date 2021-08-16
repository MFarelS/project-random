import React, {Component, Fragment} from 'react'
import Post from "../../component/Post"

class BlogPost extends Component {
  render () {
    return (
    <Fragment>
      <div className="card ms-2 mt-2" style={{boxShadow: 'rgba(0, 0, 0, 0.24) 0px 3px 8px'}}>
        <div className='row'>
          <div className='col'>
            <img src="https://placeimg.com/640/500/tech" alt="..." className='img-fluid'/>
          </div>
          <Post title='' desc=''/>
        </div>
      </div>
    </Fragment>
    )
  }
}

export default BlogPost