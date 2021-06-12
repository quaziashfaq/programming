function palindrome(str) {
  str = str.replaceAll(/[^\w]|[_]/g, '');
  console.log(str);
  return palindromeChecker(str);
}

function palindromeChecker(str){
  let i = 0;
  let j = str.length - 1;
  let match = true;
  str = str.toLowerCase();
  while( i <= j ) {
    if (str[i] !== str[j]){
      match = false;
      break;
    }
    i += 1;
    j -= 1;
  }
  return match;
}



console.log(palindrome("_eye"));
console.log(palindrome('0_0 (: /-\ :) 0-0'));
console.log(palindrome("five|\_/|four"));
console.log(palindrome("1 eye for of 1 eye."));
console.log(palindrome("1 eye for of  eye.1"));
console.log(palindrome("A man, a plan, a canal. Panama"));
