const express = require("express");
const { exec } = require("child_process");
const mysql = require("mysql");
const app = express();

// hardcoded credentials (should be in env/secret manager)
const DB_PASSWORD = "SuperSecretP@ssw0rd123";
const INTERNAL_TOKEN = "corridor_internal_a1b2c3d4e5f6g7h8i9j0";

const db = mysql.createConnection({ host: "localhost", user: "root", password: DB_PASSWORD });

app.get("/user", (req, res) => {
  const q = "SELECT * FROM users WHERE id = '" + req.query.id + "'";   // SQL injection
  db.query(q, (e, r) => res.json(r));
});

app.get("/ping", (req, res) => {
  exec("ping -c 1 " + req.query.host, (e, out) => res.send(out));        // command injection
});

app.listen(3000, () => console.log("up token=" + INTERNAL_TOKEN));
