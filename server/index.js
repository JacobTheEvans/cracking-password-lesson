let express = require("express");
let bodyParser = require("body-parser");
let cors = require("cors");

let app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(cors());

app.post("/", (req, res) => {
  console.log("Here")
  if (req.body.username !== "mike") {
    console.log("here 4")
    res.status(403).send("Must provide a valid username");
  } else if (req.body.password !== "du42") {
    console.log("here 2")
    res.status(403).send("Password is incorrect");
  } else {
    console.log("here 3")
    res.status(200).send("Success you have cracked the password");
  }
});

let PORT = process.env.Port || 9000;
app.listen(PORT, () => {
  console.log(`[+] Server is running on ${PORT}`);
});
