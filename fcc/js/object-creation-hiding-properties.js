var Person = function(firstAndLast) {
  // Only change code below this line
  // Complete the method below and implement the others similarly


  this.getFullName = function() {
    return this.getFirstName() + ' ' + this.getLastName();n
  };

  this.setFirstName = function(str) {
    let firstName = str;

    this.getFirstName = function(){
      return firstName;
    }
  }

  this.setLastName = function(str) {
    let lastName = str;

    this.getLastName = function() {
      return lastName;
    }
  }

  this.setFullName = function(str) {
    str = str.split(' ');
    this.setFirstName(str[0]);
    this.setLastName(str[1]);
  }

  this.setFullName(firstAndLast);

}




var bob = new Person('Bob Ross');
console.log(bob.getFullName());

bob.setFullName("Quazi Ashfaq");
console.log(Object.keys(bob).length);
console.log(bob.getFirstName());
console.log(bob.getLastName());


let Human = function(name){
    this.setName = function(name){
        let myName = name;

        this.getName = function(){
            return myName;
        }
    }
    this.setName(name);
}

let h = new Human('nazrul')
console.log(h.getName());
