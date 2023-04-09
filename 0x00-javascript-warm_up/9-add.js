#!/usr/bin/node
function add (a, b) {
  const c = Number(a) + Number(b);
  return c;
}

const a = process.argv[2];
const b = process.argv[3];

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
