#!/usr/bin/node
exports.esrever = function (list) {
  let new_list = [];
  for (let size = list.length - 1, count = 0; size >= 0; size--, count++) {
    new_list[count] = list[size];
  }
  return new_list;
}
