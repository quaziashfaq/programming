class Dog:
    """A simple dog."""

    def __init__(self, name, age):
        """Initialize name and age."""
        self.name = name
        self.age = age

    def sit(self):
        """Command a dog to sit."""
        print(f'{self.name} is now sitting.')
        
    def roll_over(self):
        """Command a dog to roll over."""
        print(f'{self.name} rolled over.')

