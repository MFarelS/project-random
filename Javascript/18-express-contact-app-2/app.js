const express = require('express')
const expressLayouts = require('express-ejs-layouts')
const app = express()
const port = 3000
const {loadContact, findContact} = require('./utils/contacts')

// gunakan ejs
app.set('view engine', 'ejs');

// third party middleware
app.use(expressLayouts)

// built in middleware
app.use(express.static('public'))

app.get('/', (req, res) => {
  const mahasiswa = [
    {
      nama: 'Taufik',
      email: 'tfkhdyt@pm.me'
    },
    {
      nama: 'Fauzi',
      email: 'fauzi@pm.me'
    },
    {
      nama: 'Doni',
      email: 'doni@pm.me'
    },
  ]
  res.render('index', {
    layout: 'layouts/main-layouts',
    title : 'Halaman home',
    mahasiswa,
  })
})

app.get('/about', (req, res) => {
  res.render('about', {
    layout: 'layouts/main-layouts',
    title : "Halaman about"
  })
})

app.get('/contact', (req, res) => {
  const contacts = loadContact()
  console.log(contacts)
  res.render('contact', {
    layout: 'layouts/main-layouts',
    title : "Halaman contact",
    contacts
  })
})

app.get('/contact/:nama/', (req, res) => {
  const contact = findContact(req.params.nama)
  res.render('detail', {
    layout: 'layouts/main-layouts',
    title : "Halaman Detail Contact",
    contact,
  })
})

app.use('/', (req, res) => {
  res.status(404)
  res.send('<h1>404</h1>')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
