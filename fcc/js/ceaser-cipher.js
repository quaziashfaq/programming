function rot13(str) {
  let newstr = str.split('');

  for (let i=0; i<newstr.length; i++){
    if (newstr[i] >= 'A' && newstr[i] <= 'Z'){
      newstr[i] = rotateEachChar(newstr[i]);
    }
  }
  return newstr.join('');
}

function rotateEachChar(c){
  let v = ((c.charCodeAt() - 65 ) - 13 + 26) % 26 + 65
  return String.fromCharCode(v);
}


console.log(rot13("SERR PBQR PNZC"));

// console.log(rotateEachChar('N'))
