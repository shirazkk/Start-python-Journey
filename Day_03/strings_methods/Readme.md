### Python String Methods

Below is an explanation of common Python string methods, with their definitions, and examples. I'll start with an overview of some important string methods.

---
### 1. `capitalize()`
**Definition**: Capitalizes the first letter of the string.

```python
text = "hello world"
print(text.capitalize())  # Output: Hello world
```

### 2. `casefold()`
**Definition**: Converts the string to lowercase (more aggressive than `lower()` for certain locales).

```python
text = "HELLO"
print(text.casefold())  # Output: hello
```

### 3. `center(width)`
**Definition**: Returns a centered string with spaces padded to a specified width.

```python
text = "hello"
print(text.center(10))  # Output: '  hello   '
```

### 4. `count(substring)`
**Definition**: Counts the number of occurrences of a substring in a string.

```python
text = "banana"
print(text.count("a"))  # Output: 3
```

### 5. `endswith(suffix)`
**Definition**: Checks if the string ends with a specified suffix.

```python
text = "hello"
print(text.endswith("o"))  # Output: True
```

### 6. `find(substring)`
**Definition**: Returns the index of the first occurrence of a substring or `-1` if not found.

```python
text = "hello"
print(text.find("e"))  # Output: 1
```

### 7. `isalnum()`
**Definition**: Checks if all characters in the string are alphanumeric.

```python
text = "hello123"
print(text.isalnum())  # Output: True
```

### 8. `isalpha()`
**Definition**: Checks if all characters in the string are alphabetic.

```python
text = "hello"
print(text.isalpha())  # Output: True
```

### 9. `isdigit()`
**Definition**: Checks if all characters in the string are digits.

```python
text = "12345"
print(text.isdigit())  # Output: True
```

### 10. `islower()`
**Definition**: Checks if all characters in the string are lowercase.

```python
text = "hello"
print(text.islower())  # Output: True
```

### 11. `isspace()`
**Definition**: Checks if the string consists of whitespace characters only.

```python
text = "   "
print(text.isspace())  # Output: True
```

### 12. `istitle()`
**Definition**: Checks if the string is in title case (first letter of each word is capitalized).

```python
text = "Hello World"
print(text.istitle())  # Output: True
```

### 13. `join(iterable)`
**Definition**: Joins elements of an iterable (e.g., list) with the string as a separator.

```python
text = "-"
print(text.join(["a", "b", "c"]))  # Output: a-b-c
```

### 14. `lower()`
**Definition**: Converts all characters in the string to lowercase.

```python
text = "HELLO"
print(text.lower())  # Output: hello
```

### 15. `replace(old, new)`
**Definition**: Replaces occurrences of a substring with another substring.

```python
text = "hello world"
print(text.replace("world", "Python"))  # Output: hello Python
```

### 16. `split(separator)`
**Definition**: Splits the string into a list using a specified separator.

```python
text = "hello world"
print(text.split(" "))  # Output: ['hello', 'world']
```

### 17. `startswith(prefix)`
**Definition**: Checks if the string starts with a specified prefix.

```python
text = "hello"
print(text.startswith("he"))  # Output: True
```

### 18. `strip()`
**Definition**: Removes leading and trailing whitespace characters.

```python
text = "  hello  "
print(text.strip())  # Output: hello
```

### 19. `title()`
**Definition**: Converts the first character of each word to uppercase and the rest to lowercase.

```python
text = "hello world"
print(text.title())  # Output: Hello World
```

### 20. `upper()`
**Definition**: Converts all characters in the string to uppercase.

```python
text = "hello"
print(text.upper())  # Output: HELLO
```

---



