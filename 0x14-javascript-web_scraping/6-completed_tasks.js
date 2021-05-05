#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const completed = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (!(task.userId in completed)) {
          completed[task.userId] = 0;
        }
        completed[task.userId] += 1;
      }
    }
    console.log(completed);
  }
});
