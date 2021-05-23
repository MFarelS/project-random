const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('<h1>Hello World</h1>');
});

app.get('/:name', (req, res) => {
  res.send(`<h1>Welcome to ${req.params.name}!</h1>`);
});

app.listen(5000, console.log('Server is running on port 5000'));
