#!/usr/bin/node
const Rectangle = require('/home/okinamos/alx-higher_level_programming/0x13-javascript_objects_scopes_closures/4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();
