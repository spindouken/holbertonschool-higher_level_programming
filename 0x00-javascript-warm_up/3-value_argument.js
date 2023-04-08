#!/usr/bin/node
const argvContent = process.argv[2];
if (argvContent === undefined) {
  console.log('No argument');
} else {
  console.log(argvContent);
}
