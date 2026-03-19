#!/usr/bin/node

function findMax (sortedList) {
  if (sortedList.length <= 1) {
    return 0;
  }
  return sortedList[1];
}

const sortedList = process.argv.slice(2).sort((a, b) => b - a);
console.log(findMax(sortedList));
