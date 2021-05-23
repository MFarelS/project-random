const express = require('express');
const fs = require('fs');
const sys = require('sys');
const app = express();

app.get('/', function(req, res){
  res.render('/index.html');
});

app.listen(5000, console.log('Server is running on port 5000'));
