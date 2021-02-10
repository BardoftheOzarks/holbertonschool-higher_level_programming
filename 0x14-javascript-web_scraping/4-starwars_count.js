#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const movielist = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < movielist.length; i++) {
      for (let j = 0; j < movielist[i].characters.length; j++) {
        if (movielist[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
