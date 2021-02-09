#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};

for (const key in dict) {
  newdict[dict[key]] = [];
}

for (const key in dict) {
  newdict[dict[key]].push(key);
}

console.log(newdict);
