import React, {Component, Fragment} from 'react'
import Post from "../../component/Post"
import axios from 'axios'

class BlogPost extends Component {
  state = {
    post : [],
    formBlogPost : {
      id: 1,
      title: '',
      body: '',
      userId: 1
    }
  }
  
  getPostAPI = () => {
    axios.get('http://localhost:3001/posts')
    .then(res => {
      this.setState({
        post : res.data
      })
    })
  }
  
  handleRemove = (data) => {
    console.log(data)
    axios.delete('http://localhost:3001/posts/' + data)
    .then((res) => {
      this.getPostAPI()
    })
  }
  
  handleFormChange = (e) => {
    const formBlogSpotNew = {...this.state.formBlogPost}
    formBlogSpotNew[e.target.name] = e.target.value
    this.setState({
      formBlogPost: formBlogSpotNew
    }, () => {
      console.log(this.state.formBlogPost)
    })
  }
  
  componentDidMount(){
    this.getPostAPI()
  }
  
  render(){
    return (
      <Fragment>
        <div className='row m-3'>
          <div className='col-12 col-md-9 p-4' style={{boxShadow: 'rgba(0, 0, 0, 0.24) 0px 3px 8px'}}>
            <div className="form-floating mb-3">
              <input type="text" className="form-control" id="title" name="title" placeholder="Judul" onChange={this.handleFormChange}/>
              <label htmlFor="title">Judul</label>
            </div>
            <div className="form-floating">
              <textarea className='form-control' id='body' name="body" placeholder='Body' style={{height:'100px'}} onChange={this.handleFormChange}>
              </textarea>
              <label htmlFor="body">Deskripsi</label>
            </div>
            <button className='btn btn-success mt-3'>Simpan</button>
          </div>
        </div>
        {
          this.state.post.map(post => {
            return <Post key={post.id} data={post} remove={this.handleRemove}/>
          })
        }
      </Fragment>
    )
  }
}

export default BlogPost