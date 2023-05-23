#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const args = process.argv.slice(2);
const request = require('request');

request(args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonObjects = JSON.parse(body);
  const completed = {};
  jsonObjects.forEach(todos => {
    if (todos.completed) {
      if (typeof completed[todos.userId] === 'undefined') {
        completed[todos.userId] = 1;
      } else {
        completed[todos.userId] += 1;
      }
    }
  });
  console.log(completed);
});
