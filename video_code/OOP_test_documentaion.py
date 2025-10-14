
import doctest

class Person:
    """
    A class representing a person.

    Attributes:
    - name (str): The name of the person.
    - age (int): The age of the person.
    - gender (str): The gender of the person ('Male', 'Female', 'Non-binary', etc.).

    Methods:
    - greet(): Prints a greeting message.
    - have_birthday(): Increments the age of the person by one.

    Example usage:
    >>> person1 = Person("Alice", 25, "Female")
    >>> person1.greet()
    Hello, I'm Alice!
    >>> person1.have_birthday()
    >>> person1.age
    26
    """
    
    def __init__(self, name, age, gender):
        """
        Initializes a new instance of the Person class.

        Parameters:
        - name (str): The name of the person.
        - age (int): The age of the person.
        - gender (str): The gender of the person.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        """Prints a greeting message."""
        print(f"Hello, I'm {self.name}!")

    def have_birthday(self):
        """Increments the age of the person by one."""
        self.age += 1

if __name__ == '__main__':
    doctest.testmod(verbose=True)
