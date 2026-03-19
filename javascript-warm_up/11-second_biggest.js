#!/usr/bin/node

const sortedList = process.argv.slice(2).map(Number).sort((a, b) => b - a);
let secondMax = 0;
if (sortedList.length > 1) {
  secondMax = sortedList[1];
}
console.log(secondMax);
