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
    cookie: { maxAge: 6000 },
    secret: "secret",
    resave: true,
    saveUninitialized: true,
  })
);
app.use(flash());

app.get("/", function (req, res) {
  res.render("login");
});

app.get("/dashboard", (req, res) => {
  res.render("dashboard");
});

app.post("/", (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  if (username === "taufik") {
    if (password === "hidayat") {
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

app.listen(port, function (err) {
  if (err) console.log(err);
  console.log("Server listening on PORT", port);
});
