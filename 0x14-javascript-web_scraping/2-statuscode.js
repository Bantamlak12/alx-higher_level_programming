#!/usr/bin/node
// A script that display the status code of a GET request.

const args = process.argv.slice(2);
const request = require('request');

request(args[0], function (error, response) {
  if (error) {
    console.log(error);
  }
  if (response.statusCode === 200) {
    console.log('code: ', response.statusCode);
  }
  if (response.statusCode !== 200) {
    console.log('code: ', response.statusCode);
  }
});
