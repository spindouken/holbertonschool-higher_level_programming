#!/usr/bin/node
const argvContent = process.argv[2];
if (isNaN(argvContent)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = argvContent; i > 0; i--) {
    console.log('C is fun');
  }
}
