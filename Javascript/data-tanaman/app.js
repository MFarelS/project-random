const express = require('express')
const bodyParser = require('body-parser');
const app = express()
const port = 3000

// View engine setup
app.set('view engine', 'ejs');  
app.use(express.static('public'))
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', function(req, res){
    res.render('login')
});

app.get('/dashboard', (req, res) => {
  res.render('dashboard')
})

app.post('/auth', (req, res) => {
  const username = req.body.username
  const password = req.body.password

  if(username === "taufik"){
    if(password === "hidayat"){
      res.redirect('/dashboard')
    }
  }else{
    console.log("Username salah");
  }
})

  
app.listen(port, function(err){
    if (err) console.log(err);
    console.log("Server listening on PORT", port);
});
