#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];

  for (const i in list) {
    newList.unshift(list[i]);
  }
  return (newList);
};
