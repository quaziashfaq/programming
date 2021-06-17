function checkCashRegister(price, cash, cid) {
  // Currency Value;
  let cvkey = ["PENNY", "NICKEL", "DIME", "QUARTER", "ONE", "FIVE", "TEN", "TWENTY", "ONE HUNDRED"];
  /*
  let cv = {
    "PENNY": 0.01,
    "NICKEL": 0.05,
    "DIME": 0.10,
    "QUARTER": 0.25,
    "ONE": 1,
    "FIVE": 5,
    "TEN": 10,
    "TWENTY": 20,
    "ONE HUNDRED": 100,
    };
*/
let cv = [0.01, 0.05, 0.10, 0.25, 1, 5, 10, 20, 100];

  var change = [];
  var diff = cash - price;

  // change everything from float to cash.
  let ccid = [];
  diff = parseInt(Math.round(diff*100));
  for (let i=0; i<cv.length; i++){
    cv[i] = parseInt(Math.round(cv[i] * 100));
    ccid.push([cvkey[i], parseInt(Math.round(cid[i][1]*100))]);
  }
  // console.log(ccid);

  // Check if the total cid is less than change
  var total_ccid = 0;
  for(let i=0; i<ccid.length; i++){
    total_ccid += ccid[i][1];
  }
  console.log("diff:", diff, "\t\t", "cid total:", total_ccid);
  if (total_ccid === diff){
    return {"status": "CLOSED", "change": cid};
  } else if (total_ccid < diff){
    return {"status": "INSUFFICIENT_FUNDS", "change": []};
  } else {
    //diff = parseInt(diff);

    console.log("Diff\tCVKEY\tCID");
    for(let i=cvkey.length-1; i>=0 && diff>0; i--){
      if (ccid[i][1] > 0) { // I have some amount in that bill category.
        let count = parseInt(Math.floor(diff / cv[i])); // how many will I need for that bill category?
        console.log(diff, "\t", cv[i], "\t", ccid[i][1], "\t", count);
        if (count > 0) {
          if (ccid[i][1] >= diff) {
            change.push([cvkey[i], count*cv[i]]);
            diff = diff - count * cv[i];
          }
          else if (ccid[i][1] < diff) {
              change.push([cvkey[i], ccid[i][1]]);
              diff = diff - ccid[i][1];
          }
          else {
            console.log("I should not be printed");
          }
        }
      }
    }
    if (diff > 0){
      return {"status": "INSUFFICIENT_FUNDS", "change": []};
    } else{
      for(let i=0; i<change.length; i++){
        change[i][1] = change[i][1] / 100;
      }
      return {"status": "OPEN", "change": change};
    }
  }
  return change;
}



// console.log(checkCashRegister(110, 200, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));


// console.log(checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));

console.log(checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));

// console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) );

// console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) );

// console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
