# POO is paradigm of programming that uses objects to represent data and methods to manipulate them.
# Class is a blueprint for objects. It defines the attributes and methods that will have the objects.
# Class definition

class Person:
    
    # Attributes
    # Attributes are variables that store data
    # Attributes can be public, private or protected
    # Public attributes can be accessed from outside the class
    # Private attributes can only be accessed from inside the class
    # Protected attributes can be accessed from inside the class and from subclasses
    # Ex: public_attribute, _protected_attribute, __private_attribute
    name = None
    age = None
    
    # Constructor
    # Constructor is a special method that is called when an object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Public method
    # Public methods are functions that can be called from outside the class
    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')
        
    # Private method
    # Private methods are functions that can only be called from inside the class
    def __private_method(self):
        print('This is a private method.')
    
    # Protected method
    # Protected methods are functions that can be called from inside the class and from subclasses
    def _protected_method(self):
        print('This is a protected method.')     

# Creating objects

person1 = Person('Alice', 25)

person2 = Person('Bob', 30)

# Accessing attributes

print(person1.name)
print(person2.age)

# Accessing methods

person1.say_hello()
person2.say_hello()

# Inheritance
# Inheritance is a mechanism that allows a class to inherit the attributes and methods of another class

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def say_hello(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}.')
    
    def study(self):
        print('I am studying.')

student1 = Student('Charlie', 20, 123)
student1.say_hello()

# Encapsulation
# Encapsulation is a mechanism that restricts direct access to some of the object's components

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Insufficient funds.')
            
    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
print(account.get_balance())

# Polymorphism
# Polymorphism is a mechanism that allows objects of different classes to be treated as objects of a common superclass

class Animal:
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print('Woof!')

class Cat(Animal):
    def make_sound(self):
        print('Meow!')
        
def make_animal_sound(animal):
    animal.make_sound()
    
# Example of polymorphism
dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()

make_animal_sound(dog)
make_animal_sound(cat)



# Overriding
# Overriding is a mechanism that allows a subclass to provide a specific implementation of a method that is already provided by its superclass

class Vehicle:
    def drive(self):
        print('Driving...')
        
class Car(Vehicle):
    def drive(self):
        print('Driving a car...')
        
class Truck(Vehicle):
    def drive(self):
        print('Driving a truck...')
        
vehicle = Vehicle()
vehicle.drive()

car = Car()
car.drive()

truck = Truck()
truck.drive()

# Composition
# Composition is a mechanism that allows a class to contain objects of other classes

class Engine:
    def start(self):
        print('Engine started.')
        
    def stop(self):
        print('Engine stopped.')
        
class Car:
    def __init__(self):
        self.engine = Engine()
        
    def start(self):
        self.engine.start()
        
    def stop(self):
        self.engine.stop()
        
car = Car()
car.start()
car.stop()

# Aggregation
# Aggregation is a mechanism that allows a class to contain objects of other classes, but the objects can exist independently

class Wheel:
    def rotate(self):
        print('Wheel rotating.')
        
class Car:
    def __init__(self):
        self.wheel = Wheel()
        
    def rotate_wheel(self):
        self.wheel.rotate()
        
car = Car()
car.rotate_wheel()

# Association
# Association is a mechanism that allows a class to interact with objects of other classes, but the objects are not part of the class

class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self, person):
        print(f'Hello, {person.name}!')
        
person1 = Person('Alice')
person2 = Person('Bob')

person1.greet(person2)

# Dependency
# Dependency is a mechanism that allows a class to use objects of other classes, but the objects are not part of the class

class Engine:
    def start(self):
        print('Engine started.')
        
class Car:
    def start(self):
        engine = Engine()
        engine.start()
        
car = Car()
car.start()

# Association vs. Dependency
# Association is a weak relationship between two classes
# Dependency is a strong relationship between two classes

# Abstraction
# Abstraction is a mechanism that hides the implementation details of a class and only shows the necessary information

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    
class Circle(Shape):
    
    def draw(self):
        print('Circle drawn.')
        
class Rectangle(Shape):
        
    def draw(self):
        print('Rectangle drawn.')
            
circle = Circle()
circle.draw()

rectangle = Rectangle()
rectangle.draw()

# Abstract class
# Abstract class is a class that cannot be instantiated and must be subclass

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print('Woof!')
        
class Cat(Animal):
    def make_sound(self):
        print('Meow!')
        
dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()

# Abstract method
# Abstract method is a method that must be implemented by a subclass, otherwise an error will occur

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
# class Dog(Animal):
#     pass

# dog = Dog()
# dog.make_sound()

# Error: Can't instantiate abstract class Dog with abstract methods make_sound

# Interface
# Interface is a class that contains only abstract methods
# Interface is a contract that specifies the methods that a class must implement

#Ex: interface.py

# Interface in Python
# Interface is a class that contains only abstract methods
# Interface is a contract that specifies the methods that a class must implement

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    
class Circle(Shape):
    def draw(self):
        print('Circle drawn.')
        
class Rectangle(Shape):
    
    def draw(self):
        print('Rectangle drawn.')
        
circle = Circle()
circle.draw()

rectangle = Rectangle()

rectangle.draw()

# Interface vs. Abstract class
# Interface is a class that contains only abstract methods
# Abstract class is a class that contains abstract methods and concrete methods

# Ex: interface_vs_abstract_class.py

# Interface vs. Abstract class in Python
# Interface is a class that contains only abstract methods
# Abstract class is a class that contains abstract methods and concrete methods

from abc import ABC, abstractmethod

# Interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
        
        @abstractmethod
        def area(self):
            pass
            
# Abstract class
class Circle(Shape):
    def draw(self):
        print('Circle drawn.')
        
    def area(self):
        print('Circle area.')
        
class Rectangle(Shape):
    def draw(self):
        print('Rectangle drawn.')
        
    def area(self):
        print('Rectangle area.')
        
circle = Circle()
circle.draw()
circle.area()

rectangle = Rectangle()
rectangle.draw()
rectangle.area()