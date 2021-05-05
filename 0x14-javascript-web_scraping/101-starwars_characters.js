#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      const characters = JSON.parse(body).characters;
      for (const link in characters) {
        request(characters[link], (err, response, body) => {
          if (err) {
            console.log(err);
          } else {
            const name = JSON.parse(body).name;
            console.log(name);
          }
        });
      }
    }
  });
