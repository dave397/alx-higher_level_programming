#!/usr/bin/node

/**  script that prints the addition of 2 integers */

const h = process.argv[2];
const i = process.argv[3];

function add (a, b) {
  console.log(a + b);
}

if (/^-?[0-9]/.test(h) && /^-?[0-9]/.test(i)) {
  add(+h, +i);
} else {
  console.log('NaN');
}
