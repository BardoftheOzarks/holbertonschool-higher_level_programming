#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(process.argv[3], body, 'UTF-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
