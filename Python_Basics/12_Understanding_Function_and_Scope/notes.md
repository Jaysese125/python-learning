# How Do Functions Work in Python?

## What Are Functions?
Functions are reusable pieces of code that run when you call them. Python provides built-in functions, including `print()`. 

Another helpful built-in function is `input()`, which lets you prompt the user for input:
```python
name = input('What is your name?') # User types "Kolade" and presses Enter
print('Hello', name) # Output: Hello Kolade
```

## Defining and Calling Functions
You can write your own custom functions using the `def` keyword, followed by the function name, a pair of parentheses, and a colon. The indented code inside is the function's body.

```python
def hello():
    print('Hello World')

hello() # Hello World
```

## Using Parameters and Arguments
Parameters are placeholder variables in the function definition. Arguments are the actual values you pass when calling the function.

```python
def calculate_sum(a, b): # a and b are parameters
    print(a + b)

calculate_sum(3, 1) # 3 and 1 are arguments. Output: 4
```
*Note: If you call the function without the correct number of arguments, you'll get a `TypeError`.*

## Positional and Keyword Arguments
**Positional arguments** are matched to parameters by their position (order matters).
**Keyword arguments** are passed by writing the parameter name followed by `=` and a value.

```python
def introduce(name, age):
    print(f'My name is {name} and I am {age} years old.')

introduce('Alice', 25)        # Positional
introduce(age=25, name='Alice') # Keyword (order doesn't matter)

# You can combine them, but positional arguments must come first:
introduce('Alice', age=25) # Valid
```

## Returning Values From Functions
Functions use the `return` keyword to exit the function and send back a value. If you don't explicitly use `return`, Python returns `None` by default.

```python
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4
```

---

# What is Scope in Python and How Does It Work?

Scope determines where you can use a variable in your code. We focus on **local** and **global** scope.

*   **Global Scope:** A variable created outside a function. It can be used both inside and outside functions.
*   **Local Scope:** A variable created inside a function (including parameters). It can only be used inside that function.

```python
tax_rate = 0.1  # Global variable

def calculate_tax(price):
    tax = price * tax_rate  # 'tax' is local, 'price' is local
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate)          # 0.1 (Global is accessible here)
# print(tax)             # NameError! 'tax' only exists inside the function.
```

## Pass by Assignment
Python passes arguments by assignment. When you call a function, the parameter becomes a local name that refers to the object supplied. Reassigning that parameter does not change the original variable you passed:

```python
def double_number(number):
    number = number * 2
    print(number) # 20

original = 10
double_number(original)
print(original) # 10 (The original variable is unchanged!)
```
