
# Repeating tasks with for loops

## What is a `for` loop?

A `for` loop is a tool in Python that allows us to **repeat a set of actions** multiple times. It’s great when you need to **go through** each item in a list, string, or any other collection, one by one, and do something with them.

### Imagine this:

You have a list of toys, and you want to play with each one. Instead of playing with them **manually one by one**, the `for` loop can **automate** this for you! Python will “look at” each toy (or item) in the list and perform an action on it, one by one.

---

## How does the `for` loop work?

### Syntax of a `for` loop:

```python
for item in collection:
    # Do something with 'item'
```

- **`item`**: This is a temporary name that represents each element in the collection (it could be anything).
- **`collection`**: This is a group of items, such as a list, tuple, or string.
- The code inside the loop **indented** under the `for` line runs for every `item` in the collection.

---

## Example 1: Looping through a list of numbers

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
```

### What happens here?
- We have a list of numbers: `[1, 2, 3, 4, 5]`.
- The `for` loop goes through each number one by one (`num` will first be `1`, then `2`, and so on).
- **Output**:
  ```
  1
  2
  3
  4
  5
  ```

---

## Example 2: Looping through a string

You can also loop through characters in a string!

```python
name = "Shiraz"

for letter in name:
    print(letter)
```

### What happens here?
- The loop goes through each letter in the word "Shiraz".
- **Output**:
  ```
  S
  h
  i
  r
  a
  z
  ```

---

## Example 3: Doing more inside the loop

You can add more actions inside the loop!

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I love eating {fruit}")
```

### What happens here?
- The loop goes through each fruit in the list.
- It prints a sentence for each fruit.
- **Output**:
  ```
  I love eating apple
  I love eating banana
  I love eating cherry
  ```

---

## Breaking it down in Baby Steps

1. **Step 1**: Define a collection (like a list or string) you want to loop through.
   - Example: `fruits = ["apple", "banana", "cherry"]`

2. **Step 2**: Write the `for` loop.
   - Example: `for fruit in fruits:`

3. **Step 3**: Inside the loop, write what you want to do with each item.
   - Example: `print(f"I love eating {fruit}")`

4. **Step 4**: Run the code. The loop will handle each item for you!

---

## Looping through numbers with `range()`

You can loop over a sequence of numbers using the `range()` function.

```python
for num in range(5):  # range(5) means numbers 0 to 4
    print(num)
```

### What happens here?
- `range(5)` creates a sequence of numbers starting from `0` to `4`.
- The loop prints each number.
- **Output**:
  ```
  0
  1
  2
  3
  4
  ```

---

## Recap

- The `for` loop helps you go through collections (like lists or strings) and **do something** with each item.
- It’s an easy way to **repeat actions**.
- You can loop through different types of collections: **lists, strings, numbers**, and more.

---


