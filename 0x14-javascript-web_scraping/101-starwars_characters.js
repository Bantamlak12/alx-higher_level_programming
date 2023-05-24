#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
// Display one character name by line in the same order of the
// list “characters” in the /films/ response.
const args = process.argv.slice(2);
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const jsonObjects = JSON.parse(body).characters;
  const characterPromises = [];

  jsonObjects.forEach(characterUrl => {
    const promise = new Promise((resolve, reject) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          reject(error);
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
    characterPromises.push(promise);
  });

  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => {
        console.log(name);
      });
    })
    .catch(error => {
      console.error(error);
    });
});
