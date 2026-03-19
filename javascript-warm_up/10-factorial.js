#!/usr/bin/node

function recFactorial (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  }
  return recFactorial(num - 1) * num;
}

console.log(recFactorial(parseInt(process.argv[2])));
