#!/usr/bin/node

/**  script that prints a square  */

const h = process.argv[2];

function printLine (line, main) {
  let counter = 0;
  let hol = '';
  if (line <= 0) {
    return;
  }

  while (counter < main) {
    hol += 'X';
    counter++;
  }

  console.log(hol);

  printLine(line - 1, main);
}

if (/^[0-9]/.test(h)) {
  printLine(+h, h);
} else {
  if (typeof h === 'undefined') {
    console.log('Missing size');
  }
  if (typeof h === 'string') {
    console.log('Missing size');
  }
}
