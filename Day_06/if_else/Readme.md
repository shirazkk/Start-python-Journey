
# Python `if...else` Statements

## Overview

In Python, `if...else` statements allow you to execute specific blocks of code based on logical conditions. Python supports several logical operators that enable comparison between values:

- `==` : Equals
- `!=` : Not Equals
- `<`  : Less than
- `<=` : Less than or equal to
- `>`  : Greater than
- `>=` : Greater than or equal to

These operators are used in combination with Python's `if`, `elif`, and `else` keywords to create conditional logic.

## Syntax

### Basic `if` Statement
The `if` statement checks a condition, and if it's `True`, the code block indented underneath is executed.

```python
a = 33
b = 200
if b > a:
    print("b is greater than a")
```

### Indentation
Python uses indentation to define the scope of code blocks. Forgetting to indent will raise an error.

```python
a = 33
b = 200
if b > a:
print("b is greater than a")  # This will cause an indentation error
```

### `elif` (Else If)
The `elif` statement allows for additional conditions if the first `if` condition is `False`.

```python
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
```

### `else`
The `else` block is executed if none of the previous conditions are `True`.

```python
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
```

### Short-Hand `if` Statements
If there is only one line of code to execute in an `if` or `else`, you can write the statement in one line.

```python
if a > b: print("a is greater than b")
```

### Short-Hand `if...else`
This is also called a ternary operator or conditional expression. You can condense `if` and `else` into one line.

```python
a = 2
b = 330
print("A") if a > b else print("B")
```

### Logical Operators
- **`and`**: Both conditions must be `True`.
  
    ```python
    if a > b and c > a:
        print("Both conditions are True")
    ```

- **`or`**: At least one of the conditions must be `True`.

    ```python
    if a > b or a > c:
        print("At least one condition is True")
    ```

- **`not`**: Reverses the result of the condition.

    ```python
    if not a > b:
        print("a is NOT greater than b")
    ```

### Nested `if`
You can place `if` statements inside other `if` statements to handle more complex logic.

```python
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
```

### `pass` Statement
The `pass` statement can be used as a placeholder in situations where an `if` statement is required syntactically, but no action is needed.

```python
a = 33
b = 200
if b > a:
    pass  # Do nothing, but avoid an error
```

---

## Summary

Python's `if...else` statements allow for flexible control over program logic based on conditions. Whether using basic conditions, nested logic, or short-hand syntax, Python's clear indentation structure ensures readable and efficient code. Combining `if` with logical operators such as `and`, `or`, and `not` enables handling complex logic flows. Always remember to use the `pass` statement if a condition requires no action but still needs to be syntactically valid.

## Credits

This documentation is inspired by the content available at [W3Schools Python If...Else](https://www.w3schools.com/python/python_conditions.asp).

