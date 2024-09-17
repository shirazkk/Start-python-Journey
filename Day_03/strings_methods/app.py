
# Python String Methods Examples

# 1. capitalize()
text = "hello world"
print(text.capitalize())  # Output: Hello world

# 2. casefold()
text = "HELLO"
print(text.casefold())  # Output: hello

# 3. center(width)
text = "hello"
print(text.center(10))  # Output: '  hello   '

# 4. count(substring)
text = "banana"
print(text.count("a"))  # Output: 3

# 5. endswith(suffix)
text = "hello"
print(text.endswith("o"))  # Output: True

# 6. find(substring)
text = "hello"
print(text.find("e"))  # Output: 1

# 7. isalnum()
text = "hello123"
print(text.isalnum())  # Output: True

# 8. isalpha()
text = "hello"
print(text.isalpha())  # Output: True

# 9. isdigit()
text = "12345"
print(text.isdigit())  # Output: True

# 10. islower()
text = "hello"
print(text.islower())  # Output: True

# 11. isspace()
text = "   "
print(text.isspace())  # Output: True

# 12. istitle()
text = "Hello World"
print(text.istitle())  # Output: True

# 13. join(iterable)
text = "-"
print(text.join(["a", "b", "c"]))  # Output: a-b-c

# 14. lower()
text = "HELLO"
print(text.lower())  # Output: hello

# 15. replace(old, new)
text = "hello world"
print(text.replace("world", "Python"))  # Output: hello Python

# 16. split(separator)
text = "hello world"
print(text.split(" "))  # Output: ['hello', 'world']

# 17. startswith(prefix)
text = "hello"
print(text.startswith("he"))  # Output: True

# 18. strip()
text = "  hello  "
print(text.strip())  # Output: hello

# 19. title()
text = "hello world"
print(text.title())  # Output: Hello World

# 20. upper()
text = "hello"
print(text.upper())  # Output: HELLO
