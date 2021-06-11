function smallestCommons(arr) {
  let a = 0;
  let b = 0;

  if (arr[0] > arr[1]){
    a = arr[1];
    b = arr[0];
  } else {
    a = arr[0];
    b = arr[1];
  }

  // console.log(a, b);
  let num = new Array(b-a +1);
  for(let i=0; i<num.length; i++){
    num[i] = a + i;
  }

  console.log(num);

  for(let i=0; i<num.length; i++){
    for(let j=i+1; j<num.length; j++){
      let l = lcd(num[j], num[i]);
      if (l != 1){
        num[j] /= l;
      }
    }
  }


  console.log(num);

  let total = 1;
  for(let i=0; i<num.length; i++){
    total *= num[i];
  }


  // let leastCommonDivisor = lcd(arr[0] , arr[1]);
  // return arr[0] * arr[1] / leastCommonDivisor;

  return total;
}

function lcd(a, b){
  let r = a % b;
  while(r > 0){
    a = b;
    b = r
    r = a % b;
  }
  return b;
}

// console.log(lcd(8, 12));
console.log(smallestCommons([12,8]));
console.log(smallestCommons([5,1]));
console.log(smallestCommons([2,10]));
console.log(smallestCommons([1, 13]));
console.log(smallestCommons([23, 18]));




// 1 2 3 4 5
// 1 2 3 2 5
