#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const args = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request(args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(args[1], body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
