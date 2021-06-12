function compare(a, b){
  return a === b ? 0: a < b ? -1 : 1;
}

function diffArray(arr1, arr2) {
  var newArr = [];
  let i = 0;
  let j = 0;
  arr1.sort(compare);
  arr2.sort(compare);
  console.log(arr1);
  console.log(arr2);
  while (i < arr1.length && j < arr2.length){
    while (arr1[i] === arr2[j] && i < arr1.length && j < arr2.length){
      console.log("Equal:", arr1[i], arr2[j]);
      i += 1; 
      j += 1;
    }
  while (arr1[i] < arr2[j] && i < arr1.length && j < arr2.length){
      newArr.push(arr1[i]);
      i += 1; 
    }
  while (arr1[i] > arr2[j] && i < arr1.length && j < arr2.length){
      newArr.push(arr2[j]);
      j += 1; 
    }
  }
  while (i < arr1.length){
      newArr.push(arr1[i]);
      i += 1; 
  }
  while (j < arr2.length){
      newArr.push(arr2[j]);
      j += 1; 
  }
  return newArr;
}

// console.log(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]));
console.log(diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]));
