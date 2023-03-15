#!/usr/bin/node
// A script that imports an array and computes a new array

const numbers = require('./100-data.js');
const multipliedArray = numbers.list.map((num, index) => num * index);

console.log(numbers.list);
console.log(multipliedArray);
