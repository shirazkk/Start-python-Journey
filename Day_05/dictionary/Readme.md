
# Dictionaries in Python

## What is a Dictionary?

A **dictionary** in Python is like a real-life dictionary. It stores data in a way that allows you to look up values using keys. 

- **Key**: A unique identifier for a value. It’s like a word you search for in a dictionary.
- **Value**: The data you want to store. It’s like the definition of the word.

### Example

Think of a dictionary that contains the names and ages of your friends:

```python
friends = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22
}
```

In this example:
- `"Alice"`, `"Bob"`, and `"Charlie"` are **keys**.
- `25`, `30`, and `22` are their corresponding **values**.

## Why Use Dictionaries?

Dictionaries are useful when you want to store data pairs. They allow for:
- Quick access to data.
- Storing related information together.

## Creating a Dictionary

You can create a dictionary using curly braces `{}` or the `dict()` function.

### Method 1: Using Curly Braces

```python
my_dict = {
    "key1": "value1",
    "key2": "value2"
}
```

### Method 2: Using `dict()`

```python
my_dict = dict(key1="value1", key2="value2")
```

## Accessing Values

To get a value from a dictionary, use the key in square brackets `[]`.

### Example

```python
age_of_bob = friends["Bob"]
print(age_of_bob)  # Output: 30
```

## Adding or Updating Values

You can add a new key-value pair or update an existing one:

```python
# Adding a new friend
friends["David"] = 28

# Updating Charlie's age
friends["Charlie"] = 23
```

## Removing Values

You can remove a key-value pair using the `del` statement or the `pop()` method.

### Example

```python
# Using del
del friends["Alice"]

# Using pop()
age_of_charlie = friends.pop("Charlie")
```

## Looping Through a Dictionary

You can loop through keys, values, or both.

### Example

```python
# Looping through keys
for friend in friends:
    print(friend)

# Looping through values
for age in friends.values():
    print(age)

# Looping through keys and values
for friend, age in friends.items():
    print(friend, age)
```

## Dictionary Methods

Here are some useful methods you can use with dictionaries:

### 1. `keys()`

Returns a view object that displays a list of all the keys in the dictionary.

```python
keys = friends.keys()
print(keys)  # Output: dict_keys(['Bob', 'Charlie', 'David'])
```

### 2. `values()`

Returns a view object that displays a list of all the values in the dictionary.

```python
values = friends.values()
print(values)  # Output: dict_values([30, 23, 28])
```

### 3. `items()`

Returns a view object that displays a list of dictionary's key-value tuple pairs.

```python
items = friends.items()
print(items)  # Output: dict_items([('Bob', 30), ('Charlie', 23), ('David', 28)])
```

### 4. `get(key)`

Returns the value for the specified key. If the key does not exist, it returns `None` or a default value if provided.

```python
age_of_eve = friends.get("Eve", "Not Found")
print(age_of_eve)  # Output: Not Found
```

### 5. `update()`

Updates the dictionary with the elements from another dictionary or an iterable of key-value pairs.

```python
friends.update({"Eve": 27})
print(friends)  # Output: {'Bob': 30, 'Charlie': 23, 'David': 28, 'Eve': 27}
```

### 6. `clear()`

Removes all items from the dictionary.

```python
friends.clear()
print(friends)  # Output: {}
```

### 7. `popitem()`

Removes and returns the last inserted key-value pair as a tuple. Raises `KeyError` if the dictionary is empty.

```python
last_friend = friends.popitem()
print(last_friend)  # Output will vary depending on what was the last item
```

## Summary

- A dictionary is a collection of key-value pairs.
- You can create, access, add, update, and remove items easily.
- Dictionaries are very helpful for organizing related information.
- You can use various methods to interact with dictionaries effectively.

## Additional Resources

- [Python Official Documentation on Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

---
