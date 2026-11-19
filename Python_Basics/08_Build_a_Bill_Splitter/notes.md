# Build a Bill Splitter

In this workshop, we practiced working with numbers and mathematical operations to build a bill splitter. This tool calculates how much each person owes after adding meal costs and a tip.

## 1. Setting Up Variables
We start by keeping track of the total amount and the number of people. Since food costs include cents, we use **floats**.

```python
running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21
```

## 2. Adding Costs with Augmented Assignment (`+=`)
We can use the `+=` operator to add multiple values to our `running_total` in one step.

```python
running_total += appetizers + main_courses + desserts + drinks
print(f'Total bill so far: {running_total}')
```
*Note: You might notice the output has more decimal digits than expected. This is a floating-point rounding error (binary representation), so we can use `round()` to fix it if we want.*

## 3. Calculating Percentages
To calculate a percentage, multiply the total by the decimal equivalent of the percentage (e.g., 25% = `0.25`).

```python
tip = running_total * 0.25
print(f'Tip amount: {tip}')
```

## 4. Adding the Tip to the Total
We use `+=` again to add the tip to the running total.

```python
running_total += tip
print(f'Total with tip: {running_total}')
```

## 5. Splitting the Bill
We use the forward slash `/` to divide the total bill by the number of friends.

```python
final_bill = running_total / num_of_friends
print(f'Bill per person: {final_bill}')
```

## 6. Rounding to Two Decimal Places
Because money is typically represented with two decimal places, we use the `round()` function. It takes two arguments: the number to round, and the number of decimal places to keep.

```python
each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')
```