const express = require('express');
const path = require('path');
const app = express();

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname+'/index.html'));
});

app.listen(5000, console.log('Server is running on port 5000'));
