#!/usr/bin/node
// A script that prints the number of movies where the character
// “Wedge Antilles” is present.

const args = process.argv.slice(2);
const request = require('request');

request(args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  let count = 0;
  const jsonObjects = JSON.parse(body).results;
  jsonObjects.forEach(film => {
    film.characters.forEach(character => {
      if (character.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
