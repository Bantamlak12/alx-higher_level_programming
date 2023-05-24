#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const args = process.argv.slice(2);
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsonObjects = JSON.parse(body).characters;
  jsonObjects.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const characters = JSON.parse(body);
      console.log(characters.name);
    });
  });
});
