#!/usr/bin/node
const parsed = parseInt(process.argv[2], 10);
if (isNaN(parsed)) { 
  console.log('Not a number');
  process.exit(0);
}
console.log('My number: ' + parsed);
