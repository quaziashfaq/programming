function steamrollArray(arr) {
  let newarr = [];
  // console.log(arr);
  for(let i=0; i<arr.length; i++){
    // console.log("new arr:", newarr);

    if(Array.isArray(arr[i])){
      // console.log("I am an array")
      // console.log(arr[i]);
      newarr = newarr.concat(steamrollArray(arr[i]));
    } else {
      newarr.push(arr[i]);
    }
  }
  // console.log("Returning:", newarr);
  return newarr;
}

console.log(steamrollArray([1, [2], [3, [[4]]]]));
