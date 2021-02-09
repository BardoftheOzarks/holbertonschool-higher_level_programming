#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      let row = '';
      for (i = 0; i < this.width; i++) {
        row += c;
      }
      for (i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
}

module.exports = Square;
