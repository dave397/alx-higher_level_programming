#!/usr/bin/node

/**  script that prints the addition of 2 integers */

const h = process.argv[2];

if (typeof h === 'undefined') {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let counter = 2;
  const list = [];
  while (counter < process.argv.length) {
    list.push(+process.argv[counter]);
    counter++;
  }

  list.sort((a, b) => b - a);
  console.log(list[1]);
}
