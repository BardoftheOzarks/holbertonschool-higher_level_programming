#!/usr/bin/node
class Square extends require('./5-square') {
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
