# How Do You Work With Integers and Floating Point Numbers?

Integers and floats are the primary numeric data types in Python. With them, you can store numeric data and perform mathematical operations.

## Working with Integers
Integers are whole numbers without decimal points, including positive numbers, negative numbers, and zero.

```python
my_int_1 = 56
my_int_2 = -4
print(type(my_int_1)) # <class 'int'>
```

Here is how to perform basic arithmetic operations (Addition, Subtraction, Multiplication, and Division) with integers:

```python
my_int_1 = 56
my_int_2 = 12

print('Addition:', my_int_1 + my_int_2)       # 68
print('Subtraction:', my_int_1 - my_int_2)    # 44
print('Multiplication:', my_int_1 * my_int_2) # 672
print('Division:', my_int_1 / my_int_2)       # 4.666666666666667
```
*(Note: Division with `/` always returns a float, even if the numbers are integers).*

## Working with Floats
Floats represent numbers in floating-point form, including zero (e.g., `3.14`, `-0.5`, `0.0`).

```python
my_float_1 = 5.4
my_float_2 = 12.0

print('Float Addition:', my_float_1 + my_float_2) # 17.4
print('Float Division:', my_float_2 / my_float_1) # 2.2222222222222223
```

## Mixing Integers and Floats
If you perform arithmetic operations with a mix of integers and floats, Python will automatically convert the result to a float.

```python
my_int = 56
my_float = 5.34
sum_int_and_float = my_int + my_float
print(sum_int_and_float) # 61.34
print(type(sum_int_and_float)) # <class 'float'>
```

## Complex Arithmetic Operations
Python provides operators for more complex math:

*   **Modulo (`%`)**: Returns the remainder of division.
*   **Floor Division (`//`)**: Divides and rounds down to the nearest whole number.
*   **Exponentiation (`**`)**: Raises a number to the power of another.

```python
my_int_1 = 56
my_int_2 = 12

print('Modulo:', my_int_1 % my_int_2)         # 8
print('Floor Division:', my_int_1 // my_int_2) # 4
print('Exponentiation:', my_int_1 ** my_int_2) # 951166013805414055936
```

## Floating Point Representation and Rounding Errors
Sometimes, float operations result in more decimal digits than expected. For example, `0.1 + 0.2` equals `0.30000000000000004` instead of `0.3`. 
This happens because numbers are stored in binary format, and some fractions cannot be represented exactly in binary. This leads to tiny rounding errors.

## Converting Data into Integers or Floats
Python provides built-in functions to convert data types:
*   `float()`: Converts a number or string to a float.
*   `int()`: Converts a number or string to an integer. (It truncates the decimal, it does not round).

```python
my_float = 12.92563
my_int = int(my_float)
print(my_int) # 12 (The decimal is chopped off)

my_str = '45'
converted_int = int(my_str)
print(converted_int, type(converted_int)) # 45 <class 'int'>
```

### Positive Infinity
You can create a special float value representing infinity using `float('inf')`. This is useful when you need a starting value that is guaranteed to be larger than any other number.

```python
infinity = float('inf')
print(infinity) # inf
```

## Other Useful Functions
*   **`round(number, decimal_places)`**: Rounds a number to the specified number of decimal places.
*   **`abs(number)`**: Returns the absolute (positive) value of a number.
*   **`pow(base, exp, mod)`**: Raises a number to a power, and optionally calculates the modulo of the result.

```python
print(round(4.798))      # 5
print(round(4.253, 1))   # 4.3
print(abs(-15))          # 15
print(pow(2, 3))         # 8 (2**3)
print(pow(2, 3, 5))      # 3 ((2**3) % 5)
```