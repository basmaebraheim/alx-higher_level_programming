#!/usr/bin/node

const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
const num = process.argv[2];

request(API_URL + num, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
