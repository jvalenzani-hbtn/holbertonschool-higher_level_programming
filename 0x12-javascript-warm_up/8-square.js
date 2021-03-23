#!/usr/bin/node
const parsed = parseInt(process.argv[2], 10);
if (isNaN(parsed)) {
  console.log('Missing size');
  process.exit(1);
}
for (let i = 0; i < parsed; i++) {
  let p = '';
  for (let j = 0; j < parsed; j++) {
    p += 'X';
  }
  console.log(p);
}
