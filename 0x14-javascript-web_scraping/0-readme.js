#!/usr/bin/node

// process.argv

import { readFile } from 'fs';
const filename = process.argv[2];


readFile(filename, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
