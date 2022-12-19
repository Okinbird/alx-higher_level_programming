#!/usr/bin/node
if (process.argv.length <= 0) {
  console.log('No argument');
}
if (process.argv.length === 1) {
  console.log('Argument found');
}
if (process.argv.length > 1) {
  console.log('Arguments found');
}
