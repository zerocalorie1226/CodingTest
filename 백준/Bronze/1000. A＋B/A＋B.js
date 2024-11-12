let fs=require('fs')

let input = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);


let answer=0

for(let i=0;i<input.length;i++){
    answer=answer+input[i]
}

console.log(answer)