#!/usr/bin/node
/** script that prints a message depending of the number of arguments passed */

if (process.argv.length > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
