let first = [
    [1,0,0,0,0],
    [0,0,1,0,1],
    [0,0,1,0,1],
    [0,0,1,0,1],
    [0,0,1,0,1]
];

let second = [
    [0,0,0,0,1],
    [0,0,0,0,3],
    [0,0,0,0,4],
    [0,2,0,0,2],
    [4,5,0,2,0]
];

let sample = [];

for(var i =0; i<first.length; i++){
    sample[i] = new Array(first[0].length);
}
console.log(sample)

for(var i =0; i<second.length; i++){
    for(var j=0; j<second.length; j++){
        sample[i][j] = second[j][second[0].length-1-i];
        sample[i][j] += first[i][j] // +
    }
}
console.log(sample)
result = '';
for(var v of sample){
    console.log(String.fromCharCode(parseInt(v.join(''), 8)));
    result += String.fromCharCode(parseInt(v.join(''), 8));
}
console.log(result);