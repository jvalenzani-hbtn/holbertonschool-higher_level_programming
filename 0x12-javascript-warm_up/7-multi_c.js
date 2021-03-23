#!/usr/bin/node
const parsed = parseInt(process.argv[2], 10);
if (isNaN(parsed)) {
  console.log('Missing number of occurrences');
  process.exit(1);
}
for (let i = 0; i < parsed; i++) {
  console.log('C is fun');
}
