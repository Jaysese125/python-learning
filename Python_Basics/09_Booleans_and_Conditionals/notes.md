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
print(bool(0))     # False
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