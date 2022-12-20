#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const newList = list.map(function (item, index) {
  return (item * index);
});
console.log(newList);
