#!/usr/bin/node
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filepath, body, 'utf-8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
