#!/usr/bin/node

let xTimes = parseInt(process.argv[2]);
if (isNaN(xTimes)) {
  console.log('Missing number of occurrences');
} else {
  while (xTimes > 0) {
    console.log('C is fun');
    xTimes--;
  }
}
