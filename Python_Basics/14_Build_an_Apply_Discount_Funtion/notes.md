# Build an Apply Discount Function

## Overview

This lab focuses on creating a reusable Python function that calculates the final price of an item after applying a percentage discount.

It introduces input validation, conditional statements, type checking, percentage calculations, and returning calculated values.

## 1. Defining a Function with Parameters

A function can accept parameters that represent the values it needs to process.

```python
def apply_discount(price, discount):
    pass
```

- `price`: Original price of the item.
- `discount`: Discount percentage to apply.

## 2. Type Validation with isinstance()

Before performing calculations, validate that the supplied values have the correct data types.

```python
if not isinstance(price, (int, float)):
    return 'The price should be a number'
```

The `isinstance()` function checks whether a value belongs to a specified type or tuple of types.

The same validation is applied to the discount.

## 3. Validating Numeric Values

After checking data types, validate the actual values.

**Price validation:**

```python
if price <= 0:
    return 'The price should be greater than 0'
```

The price must be greater than zero.

**Discount validation:**

```python
if discount < 0 or discount > 100:
    return 'The discount should be between 0 and 100'
```

The discount must be between 0 and 100, inclusive.

## 4. Calculating Percentage Discounts

To calculate a percentage discount:

```python
discount_amount = price * (discount / 100)
```

Then subtract the discount amount from the original price:

```python
final_price = price - discount_amount
```

Example:

- Original price: 50
- Discount percentage: 20%
- Discount amount: 50 × (20 / 100) = 10
- Final price: 50 - 10 = 40

## 5. Returning the Final Price

Use `return` to send the calculated final price back to the caller.

```python
return final_price
```

The returned value can be stored in another variable or used by another part of the program.

## Key Takeaways

- Functions can accept multiple parameters.
- `isinstance()` checks data types.
- Input validation prevents calculations using invalid values.
- Conditional statements allow functions to handle different situations.
- The `or` operator checks whether at least one condition is true.
- Percentage calculations involve dividing the percentage by 100.
- `return` sends the calculated result back to the caller.

## Workshop Result

The `apply_discount()` function successfully validates the price and discount inputs, calculates the discount amount, and returns the final price.

**Example:** An item costing 50 with a 20% discount has a final price of 40.
