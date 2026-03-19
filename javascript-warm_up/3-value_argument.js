#!/usr/bin/node

const argv2 = process.argv[2];
if (argv2 === undefined) {
  console.log('No argument');
} else {
  console.log(argv2);
}
