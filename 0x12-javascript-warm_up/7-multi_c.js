#!/usr/bin/node

/**  script that prints x times “C is fun”  */

const h = process.argv[2];

if (/^[0-9]/.test(h)) {
  let i = 0;
  while (i < +h) {
    console.log('C is fun');
    i++;
  }
} else {
  if (typeof h === 'undefined') {
    console.log('Missing number of occurrences');
  }
}
