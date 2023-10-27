let sum = 0;
let newArr = [];
const generateNumber = (arr) => {
    for(let i=0; i < arr.length ; i++)
    {
        if(arr[i] % 2 == 0) newArr.push(arr[i]);
    }
    return newArr;
}

console.log(generateNumber([2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]));


console.log('one');