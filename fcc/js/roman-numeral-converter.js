function convertToRoman(num) {
  num = num.toString();
  num = Array.from(num);
  num.reverse();

  num = num.map((n) => {
    return parseInt(n);
  });

  console.log(num);

  let str = [];

  for(let i=0; i<num.length; i++){
    if(i === 0){
      str = convertNumberToRoman(num[i], 'I', 'V', 'X') + str;
    } else if (i === 1){
      str = convertNumberToRoman(num[i], 'X', 'L', 'C') + str;
    } else if (i === 2){
      str = convertNumberToRoman(num[i], 'C', 'D', 'M') + str;
    } else if (i === 3){
      str = convertNumberToRoman(num[i], 'M', '', '') + str;
    } else {
      console.log('I should not be printed');
    }
  }

  return str;
}



function times(c, n) {
  let str = [];
  for(let i=0; i<n; i++){
    str = str + c;
  }
  return str;
}

function convertNumberToRoman(n, one, five, ten){
  let s = [];
  if (n >= 1 && n <= 3){
    s = times(one, n);
  } else if (n === 4){
    s = one + five;
  } else if (n === 5) {
    s = five;
  } else if (n >= 6 && n <= 8){
    s = five + times(one, n-5);
  } else if (n === 9){
    s = one + ten;
  }
  return s;
}


console.log(convertToRoman(3999));
