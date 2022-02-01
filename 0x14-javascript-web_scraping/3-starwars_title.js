#!/usr/bin/node

// Gets id and movie title
import request from 'request';
const id = process.argv[2];
const url = "https://swapi-api.hbtn.io/api/films/"+id

if (id > 0){
    request(url, function (error, response, body) {
        if (error) {
          console.error('error:', error);
        }
        console.log(JSON.parse(response.body).title);
      });
}