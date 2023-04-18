#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const tasksCompleted = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId]++;
      } else {
        tasksCompleted[todo.userId] = 1;
      }
    }
  });
  console.log(tasksCompleted);
});
