#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let size = list.length - 1, count = 0; size >= 0; size--, count++) {
    newlist[count] = list[size];
  }
  return newlist;
};
