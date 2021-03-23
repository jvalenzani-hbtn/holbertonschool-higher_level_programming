#!/usr/bin/node
console.log(factorial(process.argv[2]));

function factorial (a) {
  a = parseInt(a, 10);
  if (isNaN(a) || a === 1) {
    return 1;
  }
  return (factorial(a - 1) * a);
}
