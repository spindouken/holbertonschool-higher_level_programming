#!/usr/bin/node
const argvContent = process.argv[2];
if (isNaN(argvContent)) {
  console.log('Not a number');
} else {
  console.log('My number:', argvContent);
}
