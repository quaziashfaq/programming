function * range(start, end, step=1) {
  for (let i = start; i <= end; i += step){
    console.log("In range:", i);
    yield i;
  }
}

function reduce(func, initial, it) {
  let output = initial;
  for (let x of it){
    console.log("In reduce:", output, x);
    output = func(output, x);
  }
  return output;
}

function sum(x, y){
  return x + y
}


// function sumAll(arr) {
//   arr.sort();  
//   const total = Array.from(range(arr[0], arr[1])).reduce((t, item) => {
//     console.log("In sumAll:", t, item);
//     return t + item; 
//   },
//   0);  
//   return total;
// }

function sumAll(arr){
  arr.sort((a,b) => a-b);
  const r = range(arr[0], arr[1]);
  const total = reduce(sum, 0, r);
  return total;
}

console.log(sumAll([1, 4]));

console.log(sumAll([1, 4]));
