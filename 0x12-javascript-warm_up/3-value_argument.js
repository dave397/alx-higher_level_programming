#!/usr/bin/node
/** script that prints a message depending of the number of arguments passed */

if (typeof process.argv[2] !== 'undefined') {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
