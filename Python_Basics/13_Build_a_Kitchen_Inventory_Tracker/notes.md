# Build a Kitchen Inventory Tracker

## Overview

This workshop applies Python functions, parameters, arguments, local and global scope, conditional statements, and return values to build a simple kitchen inventory tracker.

## 1. Global Variables

Variables declared outside functions are accessible throughout the program.

```python
available_eggs = 1
available_flour = 2
available_sugar = 3
```

These variables represent the initial kitchen inventory.

## 2. Defining and Calling Functions

Functions allow us to organize reusable blocks of code.

```python
def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
```

A function is executed when it is called:

```python
check_kitchen_stock()
```

## 3. Parameters and Arguments

- **Parameters** are variables listed in a function definition.
- **Arguments** are actual values passed when calling a function.

```python
def use_eggs(available_eggs, eggs_to_use):
    return available_eggs - eggs_to_use

use_eggs(1, 1)
```

Here, `available_eggs` and `eggs_to_use` are parameters, while `1` and `1` are arguments.

## 4. Local Scope and Name Shadowing

Parameters and variables declared inside a function belong to its local scope.

When a parameter has the same name as a global variable, the local parameter takes precedence inside the function. This is called **name shadowing**.

Changing a local parameter does not automatically change the global variable.

## 5. Conditional Statements and Return

The `if` statement checks whether enough eggs are available.

```python
if eggs_to_use > available_eggs:
    print('The kitchen does not have enough eggs')
    return available_eggs
```

The `return` statement immediately ends the function and sends a value back to the caller.

If enough eggs are available:

```python
print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
return available_eggs - eggs_to_use
```

## 6. Updating Values Using Return

Returning a new value does not automatically update the original variable.

For example:

```python
use_eggs(available_eggs, 1)
print(available_eggs)
```

The global `available_eggs` remains `1` because the returned value was not assigned.

To update the variable, capture the returned value:

```python
available_eggs = make_fried_egg(available_eggs)
```

This reassigns the global variable using the result returned by the function.

## 7. Function Composition

A function can call another function and use its returned value.

```python
def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs
```

This function checks the inventory, uses an egg when available, and returns the remaining quantity.

## Key Takeaways

- Functions make code reusable and organized.
- Parameters receive arguments when functions are called.
- Local variables are separate from global variables.
- Name shadowing occurs when local parameters share names with global variables.
- `return` sends values back to the caller.
- Returned values must be assigned if we want to update an existing variable.
- Functions can call other functions to perform larger tasks.

## Workshop Result

Initial inventory:

- Eggs: 1
- Flour: 2
- Sugar: 3

Final inventory after making one fried egg:

- Eggs: 0
- Flour: 2
- Sugar: 3

**Total remaining items: 5**