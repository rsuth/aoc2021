const fs = require('fs')

fs.readFile('./input','utf-8', (err, data) => {
    let nums = data.split('\n').map(Number);
    
    let solution = nums.reduce((count, current, index, arr) => {
        if(arr[index+1] > current){
            return count +=1;
        } else {
            return count;
        }
    }, 0);
    
    console.log(solution);

})

fs.readFile('./input','utf-8', (err, data) => {
    let nums = data.split('\n').map(Number);
    
    let solution = nums.reduce((count, current, index, arr) => {
        if(arr[index+3] > current){
            return count +=1;
        } else {
            return count;
        }
    }, 0);
    
    console.log(solution);

})