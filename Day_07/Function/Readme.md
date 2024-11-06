## Python Functions Documentation

### What is a Function?
A function is a block of code that runs when it is called. Functions help organize code, improve reusability, and make programs easier to understand and maintain.

**Why Use Functions?**
- **Reusability**: Write code once and use it multiple times.
- **Modularity**: Break the program into smaller, manageable, and more readable parts.
- **Abstraction**: Hide the details and complexities of operations.

### Creating a Function
To create a function, use the `def` keyword followed by the function name and parentheses `()`:

```python
def my_function():
    print("Hello from a function!")
```

### Calling a Function
You call a function by writing its name followed by parentheses.

```python
my_function()  # Output: Hello from a function!
```

### Arguments
Functions can accept data passed to them, called arguments.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### Parameters or Arguments?
- **Parameters**: Variables defined in the function declaration (e.g., `name` in `def greet(name)`).
- **Arguments**: Actual values passed to the function when it is called (e.g., `"Alice"` in `greet("Alice")`).

### Number of Arguments
You must pass the correct number of arguments defined by the function.

```python
def add(a, b):
    return a + b

print(add(5, 10))  # Output: 15

# Error example:
# add(5)  # TypeError: add() missing 1 required positional argument: 'b'
```

### Arbitrary Arguments, *args
Use `*args` to allow a function to accept any number of positional arguments.

```python
def print_fruits(*args):
    for fruit in args:
        print(fruit)

print_fruits("Apple", "Banana", "Cherry")  # Output: Apple Banana Cherry
```

### Keyword Arguments
Keyword arguments are passed with a key and value pair.

```python
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Bob")  # Output: Name: Bob, Age: 25
```

### Arbitrary Keyword Arguments, **kwargs
Use `**kwargs` to pass a variable number of keyword arguments.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```

### Default Parameter Value
Provide a default value for a parameter to make it optional.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
```

### Passing a List as an Argument
You can pass a list (or any iterable) as an argument.

```python
def print_items(items):
    for item in items:
        print(item)

print_items(["A", "B", "C"])  # Output: A B C
```

### Return Values
Functions can return values using the `return` keyword.

```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)  # Output: 15
```

### The `pass` Statement
Use `pass` as a placeholder to create a function that you want to implement later.

```python
def not_implemented_yet():
    pass

# No output or error when the function is called.
```

### Positional-Only Arguments
Use `/` to specify that arguments before `/` must be positional-only.

```python
def func(a, b, /, c):
    print(a, b, c)

# Correct call
func(1, 2, c=3)  # Output: 1 2 3

# Error example:
# func(a=1, b=2, c=3)  # TypeError: func() got some positional-only arguments passed as keyword arguments
```

### Keyword-Only Arguments
Use `*` to specify that arguments after `*` must be keyword-only.

```python
def func(a, *, b, c):
    print(a, b, c)

# Correct call
func(1, b=2, c=3)  # Output: 1 2 3

# Error example:
# func(1, 2, 3)  # TypeError: func() takes 1 positional argument but 3 were given
```

### Recursion
A function that calls itself is recursive. Use recursion carefully to avoid infinite loops.

```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### **Lambda Functions in Python (Simplified)**

#### **What is a Lambda Function?**

A **lambda function** is a small, anonymous function in Python. It is used when you need a simple function for a short period and don’t want to define it with the `def` keyword.

#### **Basic Syntax:**

```python
lambda arguments: expression
```

- **arguments**: These are the inputs that the function will accept.
- **expression**: The operation or logic that the function performs and returns.

#### **Simple Example:**

```python
# A simple lambda function that adds 10 to a given number
add_10 = lambda x: x + 10

# Using the lambda function
result = add_10(5)  # Output: 15
print(result)
```

This function adds 10 to the number passed to it.

---

#### **Why Use Lambda Functions?**

- **Short & Simple**: Lambda functions are used when the function is small and doesn't need a name.
- **Quick Operations**: They're great for small operations that are only needed once.

---

#### **Lambda with Multiple Arguments:**

Lambda functions can accept multiple arguments.

```python
# Lambda function that multiplies two numbers
multiply = lambda x, y: x * y

result = multiply(4, 5)  # Output: 20
print(result)
```

Here, the lambda function multiplies `x` and `y`.

---

#### **Lambda with If-Else (Conditional)**

You can use an if-else condition inside a lambda function.

```python
# Lambda function to find the larger of two numbers
max_value = lambda x, y: x if x > y else y

result = max_value(10, 20)  # Output: 20
print(result)
```

This lambda checks if `x` is larger than `y` and returns the larger value.

---

#### **Using Lambda with `map()` and `filter()`**

Lambda functions are commonly used with functions like `map()` and `filter()` to work with lists.

- **`map()`**: Applies the function to each element in a list.

```python
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x ** 2, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16]
```

- **`filter()`**: Filters elements based on a condition.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Output: [2, 4]
```

---

#### **Key Points:**

- **One Expression Only**: Lambda functions can only have one line of code.
- **Short Usage**: They're good for quick, one-off tasks.
- **No Name**: They don't have a name like regular functions, which makes them "anonymous."

---

#### **Limitations of Lambda Functions:**

1. **One expression**: They can only have one line of code.
2. **Less readable**: If the lambda function gets too complex, it may be harder to understand.
   
---

#### **Lambda vs Regular Function**

- **Lambda**: Used for simple, one-liner functions.
- **Regular Function**: Used for more complex logic and operations.

Example of both:

```python
# Lambda function
add = lambda x, y: x + y

# Regular function
def add(x, y):
    return x + y
```

---

### **Conclusion**

Lambda functions are a simple way to define small functions in Python. They're perfect for quick tasks but should be avoided if the function is too complex. Use them for short operations, and when the function is not going to be reused multiple times.

### Python Generator Function with `yield`

A **generator function** in Python is a special type of function that generates a sequence of values lazily, meaning it produces values one at a time as they are needed, instead of all at once. This is done using the `yield` keyword.

### Key Concepts:

1. **`yield` Keyword**:
   - The `yield` statement is used in a function to turn it into a generator.
   - Each time the generator function is called, it executes until it encounters `yield`, then pauses and returns the value.
   - The function's state is saved, so when the generator is called again, it resumes where it left off.

2. **Generator Object**:
   - When you call a generator function, it does not execute immediately. Instead, it returns a **generator object**.
   - The values are generated on-demand as you iterate over the generator.

### Basic Syntax:

```python
def generator_function():
    yield value  # Generates a value and pauses the function
```

### Example:

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Yielding the current count
        count += 1

# Create the generator object
counter = count_up_to(5)

# Iterate over the generator to get the values
for num in counter:
    print(num)
```

### Output:
```
1
2
3
4
5
```

### Key Points:
- **Lazy Evaluation**: Values are computed and returned only when requested, rather than all at once.
- **Memory Efficiency**: Since it does not store all the values in memory, it is useful for working with large data sets or infinite sequences.
- **State Preservation**: After each `yield`, the function remembers where it left off, maintaining its state between calls.

### Advantages of Generator Functions:
1. **Memory Efficiency**: They don't store the entire sequence in memory, which is ideal for large datasets.
2. **Performance**: Because values are generated on the fly, you don't need to wait for the entire sequence to be created.
3. **Infinite Sequences**: Can be used to generate potentially infinite sequences without consuming all memory.

### Example: Infinite Generator

```python
def infinite_count():
    count = 1
    while True:
        yield count  # Keeps generating values indefinitely
        count += 1

# Using the infinite generator
gen = infinite_count()
for _ in range(5):  # Get first 5 numbers from the infinite generator
    print(next(gen))
```

### Output:
```
1
2
3
4
5
```

### Important Notes:
- **`return` vs `yield`**: While `return` ends the function and sends a value, `yield` allows the function to pause, return a value, and resume later.
- **`next()` Function**: You can use the `next()` function to manually retrieve the next value from a generator.

---

### Conclusion:
Generator functions are a powerful tool for managing sequences of data, especially when you need efficiency or are working with large or infinite data sets. By using `yield`, you can create functions that are both memory and performance efficient.