#!/usr/bin/node
// Imports a dictionary of occurrences by user id and computes
// a dictionary of user ids by occurrence

const data = require('./101-data.js');

const newDict = {};
for (const key in data.dict) {
  if (newDict[data.dict[key]] === undefined) {
    newDict[data.dict[key]] = [key];
  } else {
    newDict[data.dict[key]].push(key);
  }
}
console.log(newDict);
