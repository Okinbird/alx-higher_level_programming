#!/usr/bin/node
const dict = require('./101-data').dict;

const newd = {};
let list = [];
for (const [key, value] of Object.entries(dict)) {
  if (!(value in newd)) {
    list = [];
  } else {
    list = newd[value];
  }
  list.push(key);
  newd[value] = list;
}
console.log(newd);
