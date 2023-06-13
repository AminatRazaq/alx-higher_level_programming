#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let rr = 0; rr < size; rr++) {
    let row = '';
    for (let cc = 0; cc < size; cc++) row += 'X';
    console.log(row);
  }
}
