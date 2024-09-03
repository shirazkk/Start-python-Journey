# Python Variables

## Overview

**Variables** are containers for storing data values. In Python, variables are created by directly assigning values to them. Unlike some other programming languages, Python does not require explicit keywords (like `let` or `const` in JavaScript) to declare variables.

## Examples

### Basic Variable Assignment

```python
a = "shiraz"
print(a)  # This will print the string value "shiraz"

b = 2
print(b)  # This will print the integer value 2
```

## Type-Specific Variable Declaration

In Python, you can declare variables with specific types using type hints. This feature helps in providing better code clarity and can assist in type checking tools.

### Example:

```python
# Declaring a variable with a specific type
d: str = "Hello"
print(d)  # This prints the string value "Hello"

e: int = 4
print(e)  # This prints the integer value 4

r: bool = True
print(r)  # This prints the boolean value True
```

## Checking the type of a variable
```python
print(type(r))  # Output: <class 'bool'>
print(type(d))  # Output: <class 'str'>
```

## Case sensitivity in variable names
```
p = "hello-world1"
P = "hello-world2"

print(p)  # Output: hello-world1
print(P)  # Output: hello-world2

```
#### Notes:
- Be consistent with variable naming to avoid confusion and potential bugs.
- Use meaningful variable names and follow a consistent naming convention to improve code readability.
#
## Python - Variable Names

A variable name can be short, like `a` or `b`, but it’s also a good practice to use logical and descriptive names that convey the purpose of the variable.

### Rules for Python Variables

- A Python variable must start with a letter or an underscore (`_`).
- A variable name cannot begin with a number.
- A variable name can only contain alphanumeric characters and underscores (A-Z, a-z, 0-9, and `_`).
- Variable names are case-sensitive, meaning `apple`, `Apple`, and `APPLE` are considered three different variables.
- You cannot use Python keywords as variable names.


## Variable Case

We use different casing styles to create readable variable names. There are three common cases for declaring variable names:

## Camel Case

In Camel Case, the first letter of each word is capitalized, except for the first word.

`Example:`
```python
camelCaseVar = "camelcase"
```
 ## Pascal Case
In Pascal Case, the first letter of every word is capitalized.

`Example`

```
PascalCaseVar = "pascalcase"
```

## Snake Case
In Snake Case, each word is separated by an underscore.

`Example`
```
snake_case_var = "snakecase"
```
#
## Python Variables - Assign Multiple Values

in python we assign multiple values into multiple variables in one line.

`Example`

```
a,b,c="apple","Mango","Cheeku"
print(a)
print(b)
print(c)
```
## One Value To Multiple Variables

 You also assign one value to multiple variables.

`Example`
```
one=two=three="values" #print "values" in all variables.
print(one)
print(two)
print(three)
```
## Unpack a Collection

 if you have collection of values like list,tuple so  Python allows you to extract the values into variables. This is called unpacking.

Example

`Example`
```
myList = ["apple" ,"mango","watermelon"]
q,t,c=myList
print(q)
print(t)
print(c)
```