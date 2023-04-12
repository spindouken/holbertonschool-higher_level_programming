#!/usr/bin/node
exports.converter = function (base) {
  return j => j.toString(base);
};
