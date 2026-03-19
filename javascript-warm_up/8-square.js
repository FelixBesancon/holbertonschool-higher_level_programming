#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  let squareLine = '';
  for (let i = squareSize; i > 0; i--) {
    squareLine += 'X';
  }
  for (let i = squareSize; i > 0; i--) {
    console.log(squareLine);
  }
}
