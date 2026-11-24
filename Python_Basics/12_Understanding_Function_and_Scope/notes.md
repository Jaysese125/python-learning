# How Do Functions Work in Python?

## What Are Functions?
Functions are reusable pieces of code that run when you call them. Python provides built-in functions, including `print()`. 

Another helpful built-in function is `input()`, which lets you prompt the user for input:
```python
name = input('What is your name?') # User types "Kolade" and presses Enter
print('Hello', name) # Output: Hello Kolade
```

`int()` converts a number, a boolean, or a string representing an integer into an integer:
```python
print(int(3.14))  # 3
print(int('42'))  # 42
print(int(True))  # 1
print(int(False)) # 0
```

## Defining and Calling Functions
You can write your own custom functions using the `def` keyword, followed by the function name, a pair of parentheses, and a colon. The indented code inside is the function's body.

```python
def hello():
    print('Hello World')

# To run the function, you must "call" it:
hello() # Hello World
```

## Using Parameters and Arguments
Parameters are placeholder variables in the function definition. Arguments are the actual values you pass when calling the function.

```python
def calculate_sum(a, b): # a and b are parameters
    print(a + b)

calculate_sum(3, 1) # 3 and 1 are arguments. Output: 4
```

If you call the function without the correct number of arguments, you'll get a `TypeError`.

## Positional and Keyword Arguments
**Positional arguments** are matched to parameters by their position (order matters).
```python
def introduce(name, age):
    print(f'My name is {name} and I am {age} years old.')

introduce('Alice', 25) # My name is Alice and I am 25 years old.
```

**Keyword arguments** are passed by writing the parameter name followed by `=` and a value. Python matches these by name, so order doesn't matter.
```python
introduce(age=25, name='Alice') 
# My name is Alice and I am 25 years old.
```

You can combine them, but **positional arguments must come first**:
```python
introduce('Alice', age=25) # Valid
# introduce(name='Alice', 25) # SyntaxError!
```

## Returning Values From Functions
Functions use the `return` keyword to exit the function and send back a value. If you don't explicitly use `return`, Python returns `None` by default.

```python
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # Prints 4
print(my_sum) # None (because there is no return statement)

# Fix it with return:
def calculate_sum_fixed(a, b):
    return a + b

my_sum_fixed = calculate_sum_fixed(3, 1)
print(my_sum_fixed) # 4
```
