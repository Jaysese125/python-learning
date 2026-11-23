# Build a Travel Weather Planner

## 📌 Overview

This exercise uses conditional statements and Boolean logic to determine whether commuting is possible based on distance, weather conditions, and available transportation.

The program evaluates different commuting scenarios and returns either `True` or `False`.

## 📚 Concepts Learned

### 1. Boolean Variables

Boolean variables represent one of two possible values: `True` or `False`.

```python
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True
```

These variables represent conditions that can affect the commuting decision.

### 2. Truthy and Falsy Values

Python evaluates values as either truthy or falsy when used in conditional statements.

For example:

- `0` is falsy.
- `False` is falsy.
- `None` is falsy.
- Empty strings and collections are falsy.
- Nonzero numbers are truthy.

The `not` operator can be used to check whether a value is falsy.

```python
distance_mi = 0

if not distance_mi:
    print(False)
```

Since `distance_mi` is `0`, the condition evaluates to `True`, and the program prints `False`.

### 3. Conditional Statements

Conditional statements allow a program to make decisions depending on whether a condition is true or false.

Python provides three commonly used branches:

- `if` – Executes when the condition is true.
- `elif` – Checks another condition if the previous condition was false.
- `else` – Executes when none of the preceding conditions are true.

Example:

```python
distance_mi = 4

if distance_mi <= 1:
    print("Short distance")
elif distance_mi <= 6:
    print("Medium distance")
else:
    print("Long distance")
```

### 4. Boolean Operators

Boolean operators combine or reverse conditions.

| Operator | Purpose | Example |
|---|---|---|
| `and` | Both conditions must be true | `has_bike and not is_raining` |
| `or` | At least one condition must be true | `has_car or has_ride_share_app` |
| `not` | Reverses a Boolean condition | `not is_raining` |

Examples from the planner:

```python
not is_raining and has_bike
```

The person must have a bicycle, and it must not be raining.

```python
has_car or has_ride_share_app
```

The person can commute if they have a car or access to a ride-sharing application.

### 5. Evaluating Conditions in Ascending Order

The program evaluates commuting possibilities based on distance:

1. **Falsy distance:** No commuting is possible.
2. **1 mile or less:** Walking is possible only when it is not raining.
3. **More than 1 mile up to 6 miles:** A bicycle is required, and it must not be raining.
4. **More than 6 miles:** A car or ride-sharing application is required.

Conditions are checked from top to bottom. Once a matching branch is found, the remaining branches are skipped.

## 💻 Practice Code

```python
distance_mi = 9
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    print(not is_raining)
elif distance_mi <= 6:
    print(not is_raining and has_bike)
else:
    print(has_car or has_ride_share_app)
```

## 🔍 Understanding the Output

With the current variable values:

- Distance: 9 miles
- Raining: True
- Has bicycle: True
- Has car: True
- Has ride-sharing application: True

The program skips the first three branches because the distance is greater than 6 miles.

It reaches the `else` branch and evaluates:

```python
has_car or has_ride_share_app
```

Both values are `True`, so the output is:

```text
True
```

## 💡 Key Takeaways

- Boolean variables represent true or false conditions.
- Falsy values can be checked using `if not`.
- `if`, `elif`, and `else` control the execution flow.
- `and` requires both conditions to be true.
- `or` requires at least one condition to be true.
- `not` reverses a Boolean value.
- Conditions should be arranged carefully because Python evaluates them sequentially.

---

*Lesson 11 completed – Python Basics.* 🐍