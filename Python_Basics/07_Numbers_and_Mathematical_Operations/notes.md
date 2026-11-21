# How Do Conditional Statements and Comparison Operators Work?

Conditional statements, or conditionals, let you control the flow of your program based on whether certain conditions are true or false.

## Comparison Operators
Comparison operators let you compare two or more values and return a boolean value (`True` or `False`).

| Operator | Name | Description |
| :--- | :--- | :--- |
| `==` | Equal | Checks if two values are equal. |
| `!=` | Not equal | Checks if two values are not equal. |
| `>` | Greater than | Checks if the left value is greater than the right. |
| `<` | Less than | Checks if the left value is less than the right. |
| `>=` | Greater than or equal | Checks if the left value is greater than or equal to the right. |
| `<=` | Less than or equal | Checks if the left value is less than or equal to the right. |

```python
print(3 > 4)  # False
print(3 < 4)  # True
print(3 == 4) # False
print(3 != 4) # True
```

## Using `if` Statements
The most basic conditional is the `if` statement. If the condition is `True`, the indented code block runs. (Python recommends using 4 spaces for indentation).

```python
age = 18

if age >= 18:
    print('You are an adult')

# If age is 12, nothing is printed because the condition is False.
```

*Note: You can use the `pass` keyword as a placeholder if you want to create an empty code block for now.*

## Adding `else`
The `else` clause runs when the `if` condition is `False`.

```python
age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet')
```

## Adding `elif` (Else If)
Use `elif` to check multiple conditions. Python will check them from top to bottom and run the first block that evaluates to `True`. If none are true, it falls back to `else`.

```python
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')
```

---

# What are Truthy and Falsy Values, and How Do Boolean Operators Work?

In Python, every value has an inherent boolean value. 
**Falsy values** evaluate to `False`, while **Truthy values** evaluate to `True`.

*   **Falsy Values:** `False`, `0` (integer), `0.0` (float), `""` (empty string).
*   **Truthy Values:** Everything else (non-zero numbers, non-empty strings, etc.).

You can check this using the `bool()` function:
```python
print(bool(0))       # False
print(bool('Hello')) # True
```

## Boolean Operators
These operators allow you to combine multiple expressions: `and`, `or`, and `not`.

### The `and` Operator
Both operands must be truthy for the result to be truthy. It returns the first falsy operand, or the second operand if both are truthy.
```python
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote')
```

### The `or` Operator
At least one operand must be truthy for the result to be truthy. It returns the first truthy operand, or the second operand if both are falsy.
```python
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount')
```

### The `not` Operator
The `not` operator takes a single operand and inverts its boolean value.
```python
is_admin = False

if not is_admin:
    print('Access denied for non-administrators.')
```

## Short-Circuiting
Python evaluates expressions from left to right and **stops as soon as it determines the final result**.
*   With `and`: If the first operand is `False`, Python stops and returns `False` (it doesn't check the second operand).
*   With `or`: If the first operand is `True`, Python stops and returns `True` (it doesn't check the second operand).

---

# How Do Identity Operators Work?

In Python, variables are names that refer to objects. Identity operators check whether two operands refer to the **same object**.

*   `is` returns `True` if they refer to the same object.
*   `is not` returns the opposite result.

**Identity differs from equality:** `==` and `!=` compare *values*, while `is` and `is not` compare *object identity*. Use equality operators when comparing number or string values.

`None` represents the absence of a value. It is the only value of the `NoneType` data type. Objects like `None`, `True`, and `False` are **singletons**, meaning there is exactly one object for each in memory.

## Checking for None
You can use `is None` to check whether a value is missing, or `is not None` to check whether it is present.

```python
response = None

print(response is None)     # True
print(response is not None) # False
```

`None` is falsy, but it is not the same object as `False`. For example, a response could be `True` for yes, `False` for no, or `None` if no answer has been given:

```python
response = False

if response is None:
    print('No answer yet')
else:
    print('An answer was given') # An answer was given
```

Using `if not response:` instead would treat both `False` and `None` alike. The identity check distinguishes a negative answer from a missing answer.

## Checking for True and False
You can also use identity to check specifically for the boolean objects:

```python
response = False
print(response is True)     # False
print(response is False)    # True
print(response is not None) # True
```