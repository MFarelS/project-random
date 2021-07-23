const express = require('express')
const app = express()
const port = 3000

// gunakan ejs
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  //res.sendFile('./index.html', {root: __dirname})
  res.render('index')
})

app.get('/about', (req, res) => {
  res.sendFile('./about.html', {root: __dirname})
})

app.get('/product/:id', (req, res) => {
  res.send(`Product ID : ${req.params.id}<br>
Category ID : ${req.query.category}`)
})

app.use('/', (req, res) => {
  res.status(404)
  res.send('<h1>404</h1>')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
