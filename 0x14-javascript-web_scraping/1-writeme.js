#!/usr/bin/node

// Write file and content from command line

import { writeFile } from 'fs';
const filename = process.argv[2];
const content = process.argv[3];

writeFile(filename, content, err => {
  if (err) {
    console.error(err);
  }
});
