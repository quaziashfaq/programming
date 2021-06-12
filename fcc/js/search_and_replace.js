function myReplace(str, before, after) {
  let newarr = [];
  let before_re = "\\b" + before + "\\b";
  // console.log(before_re);
  let re = new RegExp(before_re, "i");
  let pos = str.search(re);
  // console.log(pos);
  // console.log(str.slice(0, pos));
  let nextpos = pos + before.length;
  
  if (isCapital(str[pos])){
    after = after[0].toUpperCase() + after.slice(1);
  } else {
    after = after[0].toLowerCase() + after.slice(1);
  }
  // console.log(nextpos);
  // console.log(str.slice(nextpos));
  return str.slice(0, pos) + after + str.slice(nextpos);
  // return str;
}

function isCapital(c){
  if (c >= 'A' && c <= 'Z'){
    return true;
  }
  return false;
}

console.log(myReplace("A quick brown fox jumped over the lazy dog", "Jumped", "Leaped"));

let sentence = "A quick brown fox Jumpedd over the lazy dog";
let before = "\\bjumped\\b";
let re = new RegExp(before, "i");
let pos = sentence.search(re);
console.log(pos);
