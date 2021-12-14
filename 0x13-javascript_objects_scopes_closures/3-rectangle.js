#!/usr/bin/node
'use strict';

export default class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }
  print() {
    for(let h = 0; h < this.height; h++) {
      for(let w = 0; w < this.width; w++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}