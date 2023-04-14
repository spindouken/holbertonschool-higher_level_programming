#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const api = `https://swapi-api.hbtn.io/api/films/${id}`;

request(api, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
