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

This way, you can easily communicate the purpose of a variable to other team members (or to your future self) in a large codebase.

**3. Avoid Single-Letter Names**
Another convention is to avoid using single-letter variable names. Single-letter names are common in Python, but they should be avoided because they communicate no purpose or meaning:

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

You can use comments to explain your code, leave reminders for yourself, or clarify why a line exists. Comments are especially helpful when you're learning or working in teams.

However, you shouldn't use comments to explain *what* your variable names mean. Instead, the names you choose for your variables should be descriptive and follow the naming rules mentioned earlier to prevent syntax errors.

---

## Knowledge Check

**Q: Which of the following is the correct way to declare a variable in Python?**
A: `age = 25` *(All lowercase, no spaces, no numbers at the start).*

**Q: Which of the following is NOT a rule for naming variables?**
A: Variable names can start with a number. *(This is false; they cannot start with a number).*

**Q: What is the naming convention called where words are separated by an underscore (e.g., `user_age`)?**
A: Snake case.
