#!/usr/bin/node

/**  script that prints the addition of 2 integers */

const h = process.argv[2];

function fac (a) {
  if (a < 0) {
    return -1;
  }
  if (a === 0) {
    return 1;
  }

  return a * fac(a - 1);
}

if (/^-?[0-9]/.test(h)) {
  console.log(fac(+h));
} else {
  if (typeof h === 'undefined') {
    console.log(1);
  }
}
