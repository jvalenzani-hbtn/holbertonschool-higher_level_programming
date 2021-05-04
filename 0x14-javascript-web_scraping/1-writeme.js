#!/usr/bin/node

// Write file and content from command line

const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, err => {
  if (err) {
    console.error(err);
  }
});
