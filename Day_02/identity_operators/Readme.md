# Identity operators
These operators checks whether the variable is equal to other variable and so on just like = 
operator

```python
a=22
b=a
print(a is b) 
print(b is a) 
z=33
print(z is a) #return false bcz z is not = a
print(z is not b) #now its return true due to not operator
```