#!/usr/bin/node
/** script that prints My number:
 * <first argument converted in integer>
 * if the first argument can be converted to an integer
 *  */

const h = process.argv[2];

if (/^[0-9]/.test(h)) {
  console.log(`My number: ${Math.floor(+h)}`);
} else {
  console.log('Not a number');
}
