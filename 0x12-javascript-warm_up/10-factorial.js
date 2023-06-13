#!/usr/bin/node
function factorial (nn) {
  return nn === 0 || isNaN(nn) ? 1 : nn * factorial(nn - 1);
}

console.log(factorial(Number(process.argv[2])));
