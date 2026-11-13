# Build a Report Card Printer

## Step 1: Creating the Name Variable
In this workshop, you will practice Python data types by creating and printing data for a simple report card.

Variables are assigned in this way:
```python
greeting = 'Hello world'
```
In the example above, the variable `greeting` has the value of a string, which is a sequence of characters surrounded by quotes.

Create a variable called `name` and assign it the string `Alice`. 
*Important: Python uses indentation (the spaces at the beginning of a line) to organize code. Make sure there are no extra spaces at the start of each line of code.*

```python
name = 'Alice'
```

## Step 2: Printing the Variable
You can print the value of a variable using the `print()` function.

```python
greeting = 'Hello world'
print(greeting) # Output: Hello world
```

A function is a reusable block of code that can be called to run its code, and arguments can be passed to it. In `print(greeting)`, `greeting` is the argument.

Print the `name` variable:
```python
name = 'Alice'
print(name)
```

## Step 3: Checking the Type
Python provides a function named `type()` that you can use to check the type of a value.

```python
platform = 'freeCodeCamp'
print(type(platform)) # Output: <class 'str'>
```
The output `<class 'str'>` means that the variable passed to the `type()` function is a string.

```python
name = 'Alice'
print(name)
print(type(name))
```

## Step 4: Adding a Boolean
Add the student's enrollment status to the report card data using a boolean value. Boolean values represent yes-or-no conditions (`True` or `False`).

```python
name = 'Alice'
print(name)
print(type(name))

is_student = True
```

## Step 5: Printing Multiple Values
The `print()` function can display more than one value at a time. Separate values with a comma `,` to print them on the same line.

```python
subject = 'Python'
print(subject, type(subject)) # Output: Python <class 'str'>
```

Print both `is_student` and its type:
```python
name = 'Alice'
print(name)
print(type(name))

is_student = True
print(is_student, type(is_student))
```

## Step 6: Reformatting the Name
Remove the earlier outputs of the `name` variable. Then, print `name` and `type(name)` together on one line separated by a comma.

```python
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))
```

## Step 7: Adding the Age (Integer)
Declare a variable named `age` and assign it the integer value `20`. Then, print the value and the data type of `age` together separated by a comma.

```python
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))
```

## Step 8: Adding the Score and using `isinstance()`
Declare a variable named `score` and assign it the value `80.5`. 

Although both `age` and `score` are numbers, they may not be the same kind. Python provides the `isinstance()` function to check this.

```python
x = 10
print(isinstance(x, int)) # Output: True
```

Use `isinstance()` to check whether `score` is an `int`:
```python
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, int)) # Output: False
```

## Step 9 & 10: Checking for Float
The output is `False`, which shows that `score` is not an `int`. Another common kind of number in Python is `float`, which represents a number with decimals. Replace `int` with `float` in the existing `isinstance()` call to confirm this.

To complete the report card, print the `score` value along with its data type using a single `print()` statement.

```python
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, float)) # Output: True
print(score, type(score))
```