#!/usr/bin/node
exports.esrever = function (list) {
  const index = list.length - 1;
  for (let j = 0; j <= index / 2; j++) {
    const temp = list[j];
    list[j] = list[index - j];
    list[index - j] = temp;
  }
  return list;
};
