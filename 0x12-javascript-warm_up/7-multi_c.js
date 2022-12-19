#!/usr/bin/node
const str = 'C is fun';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(str);
  }
}
