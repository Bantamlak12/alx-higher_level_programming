#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode
// number matches a given integer.

const args = process.argv.slice(2);
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const jsonObject = JSON.parse(body);
  console.log(jsonObject.title);
});
