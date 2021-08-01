const express = require("express");
const bodyParser = require("body-parser");
const session = require("express-session");
const cookieParser = require("cookie-parser");
const flash = require("connect-flash");
const app = express();
const port = 3000;

// View engine setup
app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.urlencoded({ extended: true }));

// konfigurasi flash
app.use(cookieParser("secret"));
app.use(
  session({
    //cookie: { maxAge: 86400000 },
    secret: "secret",
    resave: true,
    saveUninitialized: true,
  })
);
app.use(flash());

let sess;

app.get("/", function (req, res) {
  sess = req.session;
  if (sess.username && sess.password) {
    return res.redirect("/dashboard");
  }
  res.render("login", {
    belumLogin: req.flash("msg"),
    out: req.flash("out"),
  });
});

app.get("/dashboard", (req, res) => {
  sess = req.session;
  if (sess.username && sess.password) {
    res.render("dashboard");
  } else {
    req.flash("msg", "Anda harus login terlebih dahulu!");
    res.redirect("/");
  }
});

app.post("/", (req, res) => {
  sess = req.session;
  const username = req.body.username;
  const password = req.body.password;

  if (username === "taufik") {
    if (password === "hidayat") {
      sess.username = username;
      sess.password = password;
      res.redirect("/dashboard");
    } else {
      req.flash("msg", "Password salah!");
      res.render("login", {
        msg: req.flash("msg"),
      });
    }
  } else {
    console.log("Username salah");
    req.flash("msg", "Username salah!");
    res.render("login", {
      msg: req.flash("msg"),
    });
  }
});

app.get('/add', (req, res) => {
  res.render('add-tanaman')
})

app.get("/logout", (req, res) => {
  res.redirect("/");
  req.session.destroy((err) => {
    if (err) {
      return console.log(err);
    }
  });
});

app.listen(port, function (err) {
  if (err) console.log(err);
  console.log("Server listening on PORT", port);
});
