#!/usr/bin/node

// Define the target URL to retrieve the data from
const targetURL = process.argv[2];

// Import the request library
const request = require('request');

// Define the request options
const requestOptions = {
  url: targetURL,
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
};

// Make the HTTP request
request(requestOptions, function (error, response, body) {
  if (error) {
    console.error('Error occurred while making request:', error);
    return;
  }

  // Extract the films from the response body
  const films = JSON.parse(body).results;

  // Count the number of characters with the string '18' in their URL
  let characterCount = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        characterCount++;
      }
    }
  }

  // Print the character count to the console
  console.log(characterCount);
});
