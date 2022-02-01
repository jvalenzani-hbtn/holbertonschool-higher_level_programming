#!/usr/bin/node
// Gets URL and return status code

import request from 'request';
const url = process.argv[2];


request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response && response.statusCode);
});
