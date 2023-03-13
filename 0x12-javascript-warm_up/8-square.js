#!/usr/bin/node

const num = Math.floor(Number(process.argv[2]));

if (isNaN(num)) {
  console.log('Missing size');
}
for (let i = 0; i < num; i++) {
  let square = '';
  for (let j = 0; j < num; j++) {
    square += 'X';
  }
  console.log(square);
}
