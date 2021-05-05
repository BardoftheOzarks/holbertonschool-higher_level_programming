#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      const characters = JSON.parse(body).characters;
      let characters_sorted = {}
      for (const link in characters) {
        request(characters[link], (err, response, body) => {
          if (err) {
            console.log(err);
          } else {
            let name = JSON.parse(body).name;
            characters_sorted[link] = name;
          }
          if (Object.values(characters_sorted).length === characters.length) {
	    for (let i = 0; i < characters.length; i++) {
		console.log(characters_sorted[i]);
            }
          }
        });
      }
    }
  });
