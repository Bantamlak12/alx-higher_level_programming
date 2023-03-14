#!/usr/bin/node
// A class Square that defines a square and inherits from Square of 5-square.js

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let rectangle = '';
        for (let j = 0; j < this.width; j++) {
          rectangle += 'c';
        }
        console.log(rectangle);
      }
    }
  }
};
