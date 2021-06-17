function spinalCase(str) {
  let segments = str.split(/[\s_]/);
  console.log(segments);
  let words = [];
  for(let i=0; i<segments.length; i++){
    console.log(words);
    words = words.concat(splitWords(segments[i]));
  }
  return (words.map(s => s.toLowerCase()).join('-'));
//  return str;
}

function splitWords(s){
  let words = [];
  let i = 0;
  let start = i;
  while(i<s.length){
    if (s[i] >= 'A' && s[i] <= 'Z' && i < s.length){
      start = i;
      i++;
    }
    while(s[i] >= 'a' && s[i] <= 'z' && i < s.length){
      i++;
    }
    if (s[i] >= 'A' && s[i] <= 'Z' && i < s.length){
      words.push(s.slice(start, i));
      start = i;
      i++;
    }   
  }
  words.push(s.slice(start));

  return words;
}

console.log(spinalCase('ThisIs SpinalTap_Treat'));
