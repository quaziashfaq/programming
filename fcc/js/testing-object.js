let Dog = function(name) {
  this.name = name;
}

Dog.prototype.numLegs = 4;

let beagle = new Dog();

let ownProps = [];
let prototypeProps = [];

for (let property in beagle){
  console.log(property);
  if (beagle.hasOwnProperty(property)){
    ownProps.push(property);
  }
  else {
    prototypeProps.push(property);
  }
}


console.log(ownProps);
console.log(prototypeProps);

console.log(beagle.numLegs);

/*
  This is an Animal and Bird Object
  */
function Animal(name) {
  this.name = name;
  this.color = "Brown";
}

/*
Animal.prototype = {
  constructor: Animal,
  eat: function () {
    console.log("num num num");
  },
  describe: function() {
    console.log("My name is " + this.name);
  },
}
*/

Animal.prototype.constructor =  Animal;
Animal.prototype.eat =  function () {
  console.log("num num num");
}
Animal.prototype.describe = function() {
  console.log("My name is " + this.name);
}

let Bird = function(name) {
  this.name = name;
}

/*
Bird.prototype = {
  constructor: Bird,
  numLegs: 2,
};
*/


Bird.prototype = Object.create(Animal.prototype);
//Bird.prototype = Object.create(Animal);
Bird.prototype.constructor = Bird;
Bird.prototype.numLegs = 2;


let sparrow = new Bird('sparrow');
console.log('Printing sparrow\'s values');
console.log(sparrow.name);
sparrow.describe();
sparrow.eat();
console.log(sparrow.numLegs);
console.log(sparrow.color);

let robin = new Bird('robin');
robin.describe();
robin.eat();
console.log(robin.numLegs);
console.log(robin.color);

let animal = new Animal("An-n-n-imal")
console.log(animal.name);
animal.describe();
animal.eat();

console.log("Hummingbird info")
let hummingbird = new Bird('hummingbird');
hummingbird.describe();
hummingbird.eat();
console.log(hummingbird.numLegs);
console.log(hummingbird.color);
