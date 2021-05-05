#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < data.length; i++) {
    const characters = data[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
