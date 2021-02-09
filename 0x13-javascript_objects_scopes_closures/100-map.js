#!/usr/bin/node
const list = require('./100-data').list;
const newlist = [];

for (let count = 0; list[count]; count++) {
  newlist[count] = list[count] * count;
}
console.log(list);
console.log(newlist);
