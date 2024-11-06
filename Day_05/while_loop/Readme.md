
# Python `while` Loop 

## 1. Basic `while` Loop

### Explanation:
A `while` loop in Python runs as long as a given condition is `True`. It checks the condition before executing the block of code within it.

### Syntax:
```python
while condition:
    # Code block to be executed
```

### Example:
```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
```

**Explanation**:
- The loop starts with `count = 0` and continues to run as long as `count < 5`.
- The `print()` statement displays the current value of `count`.
- The `count += 1` increments `count` by 1 in each iteration to prevent an infinite loop.

**Output**:
```
Count is: 0
Count is: 1
Count is: 2
Count is: 3
Count is: 4
```

## 2. Using `break` in a `while` Loop

### Explanation:
The `break` statement is used to exit a loop prematurely when a certain condition is met, even if the loop's original condition is still `True`.

### Example:
```python
count = 0
while count < 10:
    print("Count is:", count)
    if count == 5:
        print("Breaking the loop")
        break
    count += 1
```

**Explanation**:
- The loop will print `count` from 0 to 5.
- When `count` reaches 5, the `if` condition is `True`, and the `break` statement stops the loop.

**Output**:
```
Count is: 0
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
Breaking the loop
```

## 3. Using `continue` in a `while` Loop

### Explanation:
The `continue` statement skips the current iteration of the loop and proceeds to the next iteration.

### Example:
```python
count = 0
while count < 7:
    count += 1
    if count == 4:
        print("Skipping count 4")
        continue
    print("Count is:", count)
```

**Explanation**:
- The loop runs while `count < 7` and increments `count` at the start of each iteration.
- When `count` is 4, the `continue` statement skips the `print()` call for that iteration and moves to the next one.

**Output**:
```
Count is: 1
Count is: 2
Count is: 3
Skipping count 4
Count is: 5
Count is: 6
Count is: 7
```

## 4. Infinite `while` Loop

### Explanation:
An infinite `while` loop runs forever unless stopped by a `break` statement or an external interruption. Use them with caution and ensure there's a condition to stop.

### Example:
```python
while True:
    print("This loop runs infinitely")
    break  # This line ensures the loop stops after one iteration
```

**Output**:
```
This loop runs infinitely
```

## 5. `else` with `while` Loop

### Explanation:
A `while` loop can also have an `else` clause that runs when the loop condition becomes `False`.

### Example:
```python
count = 0
while count < 3:
    print("Count is:", count)
    count += 1
else:
    print("Loop finished naturally")
```

**Explanation**:
- The `else` block runs when the `while` loop completes without encountering a `break`.

**Output**:
```
Count is: 0
Count is: 1
Count is: 2
Loop finished naturally
```



