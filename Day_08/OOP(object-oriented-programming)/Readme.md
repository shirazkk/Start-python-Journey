# Object-Oriented Programming (OOP) in Python


### **What is OOP?**

---

OOP, or Object-Oriented Programming, is a programming style that organizes code around **objects** instead of actions, focusing on **data** rather than logic alone. In OOP, objects are instances of **classes**—templates that define the characteristics (attributes) and capabilities (methods) of an object. This approach supports code that’s modular, reusable, and simpler to maintain. Popular OOP languages include Java, Python, and C++, where developers create and manage objects to build intricate applications.

---

Think of OOP like crafting a virtual world full of different things: cars, animals, people—you name it! Instead of creating everything from scratch each time, you design **blueprints** (classes) for each type, allowing you to easily make as many as you need. **Object-Oriented Programming** is all about defining these blueprints so that building virtual objects, like cars or animals, becomes easy and organized.

OOP simplifies programming by allowing you to create blueprints for different objects and then use them as many times as you want. This keeps your code organized, easy to manage, and more closely reflects the real world.

Here’s a quick look at OOP's main benefits:

### **Why OOP?**

- **Reuse**: Write code once and reuse it wherever you need.
- **Organize**: Keeps your code structured, making it easier to maintain and update.
- **Model Real-World Objects**: Allows you to mirror real-world entities, like cars, dogs, or people, making code more intuitive.

In OOP, **classes** act as blueprints, and **objects** are the actual items created from these blueprints. Let’s explore how to use OOP with some Python examples!


### Table of Contents

1. **Introduction to Classes and Objects**
2. **Attributes and Methods**
3. **Magic Methods**
4. **Four Pillars of OOP (Theory Only)**

---

## 1. Introduction to Classes and Objects

### What is a Class?

A class is a blueprint or template for creating objects. You can think of a class as a "recipe" that tells Python how to create an object and what characteristics (attributes) and actions (methods) it should have.

### What is an Object?

An object is an instance of a class. Once you have a class, you can create multiple objects based on that class. Each object will have the characteristics and actions defined by its class.

### Example:

```python
# Define a class called 'Person'
class Person:
    # Constructor method to initialize the object with attributes
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

# Create an object of the Person class
p1 = Person("Ali", 25)

# Accessing the object's attributes
print(p1.name)  # Output: Ali
print(p1.age)   # Output: 25
```

In this example:

- `Person` is the class.
- `p1` is an object of the class `Person`.
- `name` and `age` are attributes of the `Person` class.

---

## 2. Attributes and Methods

### Attributes

Attributes are the characteristics or properties of an object, defined by variables in the class. They hold the data or state of the object.

### Methods

Methods are functions defined inside a class. They describe the actions or behavior the object can perform. Methods often use the `self` parameter to access attributes and other methods within the class.

### Example:

```python
# Define a class called 'Dog'
class Dog:
    def __init__(self, name, breed):
        self.name = name    # Attribute
        self.breed = breed  # Attribute

    # Method to make the dog bark
    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Access attributes
print(dog1.name)   # Output: Buddy
print(dog1.breed)  # Output: Golden Retriever

# Call the bark method
dog1.bark()  # Output: Buddy says Woof!
```

In this example:

- `name` and `breed` are attributes of the `Dog` class.
- `bark` is a method of the `Dog` class that makes the dog "speak" when called.

---

## Magic Methods in Python Classes

In Python, **magic methods** (also known as "dunder methods" because they begin and end with double underscores) allow classes to interact in special ways with built-in functions and operators. Below, we'll cover four commonly used magic methods: `__init__`, `__repr__`, `__str__`, and `__add__`, with examples.

Let's break down how these methods work using an `Animal` class.

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __repr__(self):
        return f"Animal(name='{self.name}', sound='{self.sound}')"

    def __str__(self):
        return f"This is a {self.name} that goes '{self.sound}'!"

    def __add__(self, other):
        return Animal(self.name + "-" + other.name, self.sound + "-" + other.sound)
```

---

### 1. `__init__`: The Initializer (Constructor)

The `__init__` method is a special method called automatically when a new instance of a class is created. It initializes the object's attributes.

- **Purpose**: To set up an object’s initial state.
- **Example Use**: Defining an `Animal` with a `name` and `sound`.

#### Code Explanation:

```python
def __init__(self, name, sound):
    self.name = name
    self.sound = sound
```

**Explanation**: Here, `__init__` takes two arguments, `name` and `sound`, and assigns them to `self.name` and `self.sound`, making them attributes of the `Animal` instance.

#### Example:

```python
lion = Animal("Lion", "Roar")
print(lion.name)   # Output: Lion
print(lion.sound)  # Output: Roar
```

---

### 2. `__repr__`: The Official String Representation

The `__repr__` method provides a detailed, unambiguous string representation of an object. It’s primarily intended for developers and is often used in debugging.

- **Purpose**: To return a string that gives a complete and informative representation of the object, ideally in a way that allows the object to be recreated by Python.
- **Example Use**: Providing a detailed view of the `Animal` instance's state.

#### Code Explanation:

```python
def __repr__(self):
    return f"Animal(name='{self.name}', sound='{self.sound}')"
```

**Explanation**: Here, `__repr__` returns a string showing the `name` and `sound` attributes of the `Animal` instance, structured in a way that resembles valid Python code.

#### Example:

```python
print(repr(lion))  # Output: Animal(name='Lion', sound='Roar')
```

---

### 3. `__str__`: The User-Friendly String Representation

The `__str__` method provides a more readable, user-friendly string representation of an object. This representation is typically meant to be displayed to end users.

- **Purpose**: To return a string that’s more readable and friendly, often for printing.
- **Example Use**: Giving a simple description of the `Animal` instance.

#### Code Explanation:

```python
def __str__(self):
    return f"This is a {self.name} that goes '{self.sound}'!"
```

**Explanation**: Here, `__str__` returns a sentence describing the `Animal` by combining the `name` and `sound` attributes in a natural, descriptive way.

#### Example:

```python
print(str(lion))   # Output: This is a Lion that goes 'Roar'!
# Or simply:
print(lion)        # Output: This is a Lion that goes 'Roar'!
```

> **Note**: If `__str__` is not defined, Python will use `__repr__` as a fallback when printing an object.

---

### 4. `__add__`: The Addition Operator

The `__add__` method allows you to define the behavior of the `+` operator for instances of your class. By overriding `__add__`, you can control what happens when two instances are added together.

- **Purpose**: To customize the behavior of the `+` operator for a class.
- **Example Use**: Creating a new `Animal` with a combined name and sound when two animals are added.

#### Code Explanation:

```python
def __add__(self, other):
    return Animal(self.name + "-" + other.name, self.sound + "-" + other.sound)
```

**Explanation**: Here, `__add__` takes another `Animal` instance (`other`) and combines its `name` and `sound` attributes with those of the current instance (`self`). A new `Animal` instance is created and returned, where `name` and `sound` are combined with hyphens.

#### Example:

```python
tiger = Animal("Tiger", "Growl")
liger = lion + tiger
print(liger)       # Output: This is a Lion-Tiger that goes 'Roar-Growl'!
```

---

### Full Code and Summary

Here’s the complete code for reference, showing how these magic methods enable a natural, Pythonic interface with the `Animal` class:

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __repr__(self):
        return f"Animal(name='{self.name}', sound='{self.sound}')"

    def __str__(self):
        return f"This is a {self.name} that goes '{self.sound}'!"

    def __add__(self, other):
        return Animal(self.name + "-" + other.name, self.sound + "-" + other.sound)

# Create instances
lion = Animal("Lion", "Roar")
tiger = Animal("Tiger", "Growl")

# Use __repr__ and __str__
print(repr(lion))       # Output: Animal(name='Lion', sound='Roar')
print(lion)             # Output: This is a Lion that goes 'Roar'!

# Use __add__
liger = lion + tiger
print(liger)            # Output: This is a Lion-Tiger that goes 'Roar-Growl'!
```

This demonstrates how `__init__`, `__repr__`, `__str__`, and `__add__` work together to make the `Animal` class easy to use and interact with, while also keeping the code clean and readable.

---

## 4. Four Pillars of OOP

### 1. Encapsulation

Encapsulation is the concept of wrapping the data (attributes) and methods (functions) together within a class. This helps in protecting data from outside interference and misuse. You can control access to data by using private variables or methods.

Example:
```python
class Toy:
    def __init__(self, name, sound):
        self.name = name      # Public attribute
        self.__sound = sound  # Private attribute (using __)

    def make_sound(self):
        print(f"{self.name} says {self.__sound}")

my_toy = Toy("Teddy Bear", "Growl")
my_toy.make_sound()  # Output: Teddy Bear says Growl
```
```python
print(my_toy.name)
# my_toy.__sound    #error because sound is private attribute we cant access it outside.
```

- Here, `__sound` is **private**, meaning no one outside can change it.
- You can only interact with it through the method `make_sound()`.

### **More Encapsulation Example**

Consider a **Bank Account** class where we want to keep the balance private:

```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

# Creating an account
my_account = BankAccount("John Doe", 1000)
print(my_account.get_balance())  # Output: 1000
my_account.deposit(500)  # Output: Deposited 500. New balance is 1500
print(my_account.get_balance())  # Output: 1500
# print(my_account.__balance)    # Error: AttributeError: 'BankAccount' object has no attribute '__balance'
```
- The **balance** is kept private to ensure no one can change it directly without using the proper method.

### 2. Abstraction

Abstraction means hiding unnecessary details and only showing the essential features of an object. This allows the user to interact with the object without needing to understand its internal workings.

Example:

- The `Shape` class hides the details of how different shapes calculate area. You just need to use `area()`.

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # ABC stands for Abstract Base Class
    @abstractmethod
    def calculate_area(self):
        pass

# Shape is an abstract base class (ABC) that defines a method calculate_area() using the @abstractmethod
# decorator from the abc module.
# An abstract method is a method that is declared but contains no implementation.
# It must be overridden in any subclass that inherits from Shape.

import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Usage example
circle = Circle(5)
rectangle = Rectangle(3, 4)

print(f"Area of circle: {circle.calculate_area():.2f}")
print("Area of rectangle:", rectangle.calculate_area())
```


### **More Abstraction Example**

Imagine we want to create different types of payment methods, but we don't want users to worry about the details:

In this example, we have an abstract base class `Payment` that defines a common interface for different payment methods. Each payment method subclass (`CreditCardPayment` and `PayPalPayment`) implements the `pay()` method according to its specific logic.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

payment_methods = [CreditCardPayment(), PayPalPayment()]
for method in payment_methods:
    method.pay(100)  # Output: Paid 100 using Credit Card. Paid 100 using PayPal.
```
- Here, `Payment` is abstract, and users only interact with the `pay()` method without needing to know how each payment method works.

#### Benefits of Abstraction in This Example

- **Flexibility and Extensibility**: Adding new payment methods (e.g., `BitcoinPayment`, `ApplePayPayment`) would involve creating new subclasses of `Payment` and implementing `pay()`, without modifying existing code.
- **Code Reusability**: The `Payment` abstraction allows us to reuse the `pay()` method across different payment methods while maintaining a consistent interface.
- **Encapsulation**: Details of how payments are processed (`CreditCardPayment` or `PayPalPayment`) are encapsulated within their respective classes, abstracting away complexity from the client code.

### 3. Inheritance

Inheritance allows one class to inherit attributes and methods from another class. The class that inherits is called the "child class" or "subclass," and the class it inherits from is called the "parent class" or "superclass." This helps with reusability of code.

Example: If you have a `Vehicle` class, you can create a `Car` class that inherits from it, so `Car` automatically has all the features of a `Vehicle`.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print("Beep beep!")

class ElectricCar(Vehicle):  # Car inherits from Vehicle
    def __init__(self, brand, color):
        super().__init__(brand) # super
        self.color = color

    def Car(self):
        print(f"The {self.color} {self.brand} car is driving.")

my_car = ElectricCar("Tesla", "red")
my_car.Car()  # Output: The red Tesla car is driving.
my_car.honk()  # Output: Beep beep!
print(my_car.brand)  # Output: Tesla
print(my_car.color)
```
1. **`__init__` (Constructor Method)**:
   - `__init__` is a special method in Python classes that is automatically called when a new instance (object) of the class is created.
   - Its primary purpose is to initialize the object's state by setting initial values for its attributes.
   - This method is where you typically perform initialization tasks such as assigning values to instance variables based on arguments passed to the constructor.

2. **`super()` (Super() function)**:
   - `super()` is a built-in function in Python used to call methods and constructors from a parent class (superclass) within a subclass (derived class).
   - It allows you to explicitly call methods and constructors of the parent class to reuse code or extend functionality without duplicating it in the subclass.
   - It is often used inside the `__init__` method of a subclass to invoke the constructor of the parent class and initialize inherited attributes.

   ### **More Inheritance Example**

Let's say we have a `Person` class, and we want to create a `Student` class that inherits from `Person`:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

student = Student("Alice", 20, "S12345")
print(student.student_id)  # Output: student id S12345
student.introduce()  # Output: Hello, my name is Alice and I am 20 years old.
student.study()  # Output: Alice is studying.
```
- The `Student` class **inherits** from `Person`, meaning it can introduce itself and also has additional behavior, like studying.

### 4. Polymorphism

**Polymorphism** means **many forms**. It lets you use the same word to mean different things in different contexts. For example, the `make_sound()` function might make a dog bark and a cat meow.

Think of it as **different toys that all make sounds, but different sounds**.

Example:

- The same function name, `make_sound()`, works differently for each animal.

```python

class Animal:
    def make_sound(self):
        pass
    

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()  # Output: Woof! Meow!

```
### **More Polymorphism Example**

Let's say we have different shapes, and each shape can calculate its area in a different way:

```python
import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{math.pi * self.radius * self.radius:.2f}"

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())  # Output: 20, 28.26
```
- The `area()` method is **polymorphic**, meaning it works differently for each shape.


## **Recap**

- **Class**: A blueprint to create objects.
- **Object**: A real thing made from a class.
- **Encapsulation**: Keeping all the data and functions inside one box.
- **Abstraction**: Hiding complex details and showing only the essentials.
- **Inheritance**: Getting features from a parent class.
- **Polymorphism**: Using the same function in different ways for different objects.

OOP helps us create **organized, reusable**, and **easy-to-understand** programs by thinking of our code like real-world objects. 🎉

By adding more examples and exploring each concept deeply, you can build a strong foundation in OOP, making you a more **professional** and **confident** programmer!