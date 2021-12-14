#!/usr/bin/node

export function nbOccurences (list, searchElement) {
    let count = 0;
    list.forEach(element => {
        if(element == searchElement) {
            count++;
        }
    });
    return count;
}