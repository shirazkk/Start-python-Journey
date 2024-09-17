# Logical Operators
Logical operators in Python are used to perform logical operations on Boolean values (True or False). These operators allow us to combine conditional statements, making decisions based on multiple conditions. They return `True` or `False` depending on the logic applied to the operands.

There are three logical operators `AND`, `OR`, `NOT`.
***
## AND Operator
AND operator check both values if one value is `False` it return `False` else `True`.

**for example**
```python
a=False
b=True
print(a and b) #one condition is false it return false 
```
```python
a=True
b=True
print(a and b) #now it return true because both operands are true
```
***
## OR Operator
OR operator returns `True` if at least one operand is `True`.

**for example**
```python
a=True
b=False
print(a or b) #return true if at least one condition is true
```
```python
a=False
b=False
print(a or b) #return false 
```
***
## NOT Operator
The `NOT operator` that negates the Boolean value of its operand, returning `True` if the operand is `False`, and `False` if the operand is `True`.

**for example**
```python
a=False
b=True
print(not a) #value of a is false but it negates it so output will be True
print(not b) #return False 
```
***
There are some more problems related logical operators

```python
a=False
b=False
print(not a or b) #Both values are False, but the not operator negates a, making it True. Since one condition is now True, the or operator returns True.
```
---
```python
a=True
b=True
print(a and not b) #Both values are True.but value b is negates become False so in and operator one condition false it always returns False output will be false
```
---
```python
a=False
b=False
print(not a and not b ) #due to not operator both value become True so it return True