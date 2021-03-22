#!/usr/bin/node
const integer = process.argv[2];

function factorialize (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else if (num < 0) {
    return -1;
  } else {
    return (num * factorialize(num - 1));
  }
}
console.log(factorialize(integer));
