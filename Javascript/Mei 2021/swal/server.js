const express = require('express');
const app = express();

app.get('/', function(req, res) {
  res.sendFile('index.html');
});

app.listen(5000, console.log('Server is running on port 5000'));
