#!/usr/bin/node
console.log(add(process.argv[2], process.argv[3]));

function add (a, b) {
  a = parseInt(a, 10);
  b = parseInt(b, 10);
  return a + b;
}
