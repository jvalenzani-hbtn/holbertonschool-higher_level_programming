#!/usr/bin/node

// process.argv
const filename = process.argv[2];

const fs = require('fs');
fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
