#!/usr/bin/node
const converter = require('/home/okinamos/alx-higher_level_programming/0x13-javascript_objects_scopes_closures/10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
