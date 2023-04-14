#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
const targetID = 18;

request(api, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach((film) => {
      if (film.characters.includes(`https://swapi-api.hbtn.io/api/people/${targetID}/`)) {
        count++;
      }
    });

    console.log(count);
  }
});
