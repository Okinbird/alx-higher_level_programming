#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    listCharacters(characters, 0);
  }
});

function listCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        listCharacters(characters, index + 1);
      }
    }
  });
}
