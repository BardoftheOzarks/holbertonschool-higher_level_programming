#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const tasklist = JSON.parse(body);
    const results = {};
    for (let i = 0; i < tasklist.length; i++) {
      if (tasklist[i].completed === true) {
        if (!(tasklist[i].userId in results)) {
          results[tasklist[i].userId] = 1;
        } else {
          results[tasklist[i].userId] += 1;
        }
      }
    }
    console.log(results);
  }
});
