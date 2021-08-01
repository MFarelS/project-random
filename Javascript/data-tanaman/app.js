const express = require('express')
const app = express()

const port = 3000

// View engine setup
app.set('view engine', 'ejs');
  
app.use(express.static('public'))

app.use('/', function(req, res){
    res.render('login/index')
});
  
app.listen(port, function(err){
    if (err) console.log(err);
    console.log("Server listening on PORT", port);
});
