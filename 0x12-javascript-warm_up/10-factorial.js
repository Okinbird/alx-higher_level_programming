#!/usr/bin/node
function factorial (n) {
  if (n === 0 || Number.isNaN(n)) {
    return (1);
  }
  return (factorial(n - 1) * n);
}
const n = Number(process.argv[2]);
console.log(factorial(n));
