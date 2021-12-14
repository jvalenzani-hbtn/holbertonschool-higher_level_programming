#!/usr/bin/node
'use strict';

import Rectangle from "./4-rectangle.js";

export default class Square extends Rectangle {
    constructor(size){
        super(size, size);  
    }

    charPrint(c='X') {
        for(let i = 0; i < this.width; i++)
        {
            for(let j = 0; j < this.width; j++)
            {
                process.stdout.write(c);
            }
            process.stdout.write('\n');
        }
    }
}