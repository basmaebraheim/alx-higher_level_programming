#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const i of characters) {
    req.get(i, function (error, res, body2) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body2);
      console.log(data1.name);
    });
  }
});
