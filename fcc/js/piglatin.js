function translatePigLatin(str) {
  let foundFirstVowel = 0;
  if (isItVowel(str[0])){
    return str + 'way';
  }
  else{
    for(let i=0; i<str.length; i++){
      if (isItVowel(str[i])){
        foundFirstVowel = i;
        break;
      }      
    }
    return str.slice(foundFirstVowel) 
            + str.slice(0,foundFirstVowel) + 'ay';
  }
  return str;
}

function isItVowel(c){
  if(c === 'a'
      || c === 'e'
      || c === 'i'
      || c === 'o'
      || c === 'u'){
        return true;
      }
  return false;
}
console.log(translatePigLatin("consonant"));
console.log(translatePigLatin("glove"));

