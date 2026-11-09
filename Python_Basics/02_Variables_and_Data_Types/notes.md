# How Do You Declare Variables and What Are Naming Conventions?

## Declaring Variables

In Python, variables are like labeled boxes for storing and referencing data of different types. To create a variable, write its name on the left, followed by the assignment (`=`) operator and the value you want to store on the right. 

Here is an example of how to create `name` and `age` variables:

```python
name = 'John Doe'
age = 25
```

In the example above, the variable `name` holds the value `'John Doe'`. This value is a **string**, which is a series of characters used to represent text. Strings are written with single or double quotes (e.g., `'Hello'` or `"Hello"`).

---

## Following Naming Rules

When naming variables in Python, there are some important rules you must keep in mind:

*   Variable names can only start with a letter or an underscore (`_`), **not a number**.
*   Variable names can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (`_`).
*   Variable names are **case-sensitive**: `age`, `Age`, and `AGE` are all considered unique.
*   Variable names cannot be one of Python's reserved keywords such as `if`, `class`, or `def`.

If you break any of those rules, your Python program will raise a `SyntaxError`:

```python
5variable_name = 5
```
```text
SyntaxError: invalid syntax
```

---

## Following Naming Conventions

Here are some common naming conventions for variables in Python:

**1. Snake Case**
Variable names should be in lowercase, with words separated by an underscore. This is called `snake_case`:

```python
my_variable_name = 'freeCodeCamp'
```

**2. Descriptive Names**
You should use descriptive names for variables. For example, if you want to save a user's age as a variable, `user_age` is better than `age` or an abbreviation like `ua`:

```python
user_age = 30
```

**3. Avoid Single-Letter Names**
Another convention is to avoid using single-letter variable names because they communicate no purpose or meaning:

```python
x = 56  # What do you mean by x?
```

---

## Writing Comments

The pound symbol (`#`) and the text that follows it form a comment. Comments let you add notes and explanations to your code. Python ignores everything after the `#` symbol on that line.

```python
# This is a single-line comment
```

Multi-line comments can be created by using consecutive single-line comments:

```python
# This is a
# Multi-line
# Comment
```

---

# How Does the Print Function Work?

## The Terminal
The terminal is the area where you can see text output from a program.

Python includes `print()` as a built-in function, which means you can use it without defining it yourself. The `print()` function sends text and other values to the terminal. 

A common first program displays `Hello world!` in the terminal. You can write this program in Python with the print function. To do that, you just put the string `Hello world!` in between the opening and closing parentheses:

```python
print('Hello world!') # Output: Hello world!
```

Consider strings as a sequence of characters surrounded by either single (`'`) or double (`"`) quotation marks.

In the `print('Hello world!')` example, the string `'Hello world!'` is an argument passed to the print function. You can also use the print function to show multiple values or arguments at once by separating them with commas. For example:

```python
print('My favorite colors are', 'blue', 'green', 'red')
# Output: My favorite colors are blue green red
```

Python automatically adds a space between each item when you separate them with commas. This is helpful when you want to print several pieces of information together.

### Knowledge Check
**Q: Why does the following code print all the values on the same line with spaces?**
`print('My favorite colors are', 'blue', 'green', 'red')`
A: Because separating values with commas in `print()` adds spaces between them.

**Q: What would the output of the following code be?**
`print('Hello', 'world!')`
A: `Hello world!`

**Q: What is the purpose of the quotation marks around Hello world! in the following code?**
`print('Hello world!')`
A: They define a string to be printed by the `print()` function.

---

# What are Common Data Types in Python?

A data type describes the kind of value a variable holds, for example, a number or a piece of text. Programming languages use data types so they know how to store and work with different kinds of information.

Python is a **dynamically typed language**. This means you do not specify a variable's data type when you create it. Python determines the type from the value assigned to the variable.

Here are some examples:

```python
name = 'John Doe' # Python knows this is a string because of the quotes
age = 25 # Python knows this is an integer
```

A variable can later be assigned a value of a different type:

```python
age = 25
age = 'Twenty-five'
```
After the second assignment, `age` contains a string instead of an integer.

For now, focus on four data types that you will use frequently:

**1. Integer**
A whole number without decimals (e.g., `10` or `-5`).
```python
my_integer_var = 10
print('Integer:', my_integer_var) # Output: Integer: 10
```

**2. Float**
A number with a decimal point (e.g., `4.41` or `-0.4`).
```python
my_float_var = 4.50
print('Float:', my_float_var) # Output: Float: 4.5
```

**3. String**
A sequence of characters enclosed in single or double quotation marks (e.g., `'Hello world!'`).
```python
my_string_var = 'hello'
print('String:', my_string_var) # Output: String: hello
```

**4. Boolean**
A true or false type, written as `True` or `False`.
```python
my_boolean_var = True
print('Boolean:', my_boolean_var) # Output: Boolean: True
```

### Knowledge Check
**Q: What does it mean that Python is dynamically typed?**
A: Python automatically determines the data type based on the assigned value.

**Q: What is the difference between the integer and float data types?**
A: Integers are whole numbers without decimals, while floats are numbers with decimal points.

**Q: Which of the following is a True or False type in Python?**
A: Boolean

---

# How Do the type() and isinstance() Functions Work?

In the prior lesson, you learned about common data types in Python including the string, integer, and float types. As you build out your programs, you will need to learn how to view the type of a variable.

Here is an example variable:

```python
developer = 'Devin' # A string
```

To see what type `developer` is, you can use the `type()` function like this:

```python
developer = 'Devin'
print(type(developer)) # Output: <class 'str'>
```
The output of `<class 'str'>` means that `developer` is a string type.

If you fail to provide any arguments to the `type()` function, then you will receive the following error message:

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
```
*(This means if you use the `type()` function, you must pass arguments to it).*

Here are the data types you have learned so far, along with what the `type()` function prints for each one:

```python
my_integer_var = 10
print(type(my_integer_var)) # Output: <class 'int'>

my_float_var = 4.50
print(type(my_float_var)) # Output: <class 'float'>

my_string_var = 'hello'
print(type(my_string_var)) # Output: <class 'str'>

my_boolean_var = True
print(type(my_boolean_var)) # Output: <class 'bool'>
```

## The isinstance() Function

There will be times in your program when you need to verify that a particular variable is a specific type before performing operations on it. This is where the `isinstance()` function comes in handy.

Here is an example variable with a string assigned to it:

```python
account_balance = '12'
```

If you try to perform mathematical operations like division using the `account_balance` variable, then you will receive an error message:

```python
account_balance = '12'
account_balance / 2
```

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

To see if `account_balance` is an integer, you can check using the `isinstance()` function like this:

```python
account_balance = '12'
print(isinstance(account_balance, int)) # Output: False
```

The built-in `isinstance()` function lets you check if a variable matches a specific data type. It takes a value and the type you want to check it against, then returns a boolean. In this case, since `account_balance` is a string, it will return `False`.

The `isinstance()` function also allows you to check for multiple types at once.

Here is an example checking if `account_balance` is an `int` or `float`:

```python
account_balance = 12
print(isinstance(account_balance, (int, float))) # Output: True
```
*(In this example, `account_balance` is an integer, so `isinstance()` returns `True`. If `account_balance` were `12.0`, `isinstance()` would still return `True` because you are checking for integers or floats).*

In future workshops and labs, you will use the `type()` and `isinstance()` functions to ensure your variables contain the correct data types before performing operations on them.

### Knowledge Check
**Q: What will be the output for the following code?**
```python
developer = 'Devin'
print(type(developer))
```
A: `<class 'str'>`

**Q: Which function is used to check if a variable is a specific type?**
A: `isinstance()`

**Q: What will be returned in this use of the isinstance() function?**
```python
account_balance = 12
isinstance(account_balance, (int, float))
```
A: `True`
