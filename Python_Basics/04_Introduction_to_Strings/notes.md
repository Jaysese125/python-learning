# What Are Strings and What Is String Immutability?

A string is a sequence of characters surrounded by either single or double quotation marks. Python treats both forms as strings, so you can use either one.

```python
my_str_1 = 'Hello'
my_str_2 = "World"
```

## Multiline Strings
If you need a multiline string, you can use triple double quotes or triple single quotes:

```python
my_str_3 = """ Multiline
string"""
my_str_4 = ''' Another multiline string '''
```

## Handling Quotes Inside Strings
If your string contains either single or double quotation marks, then you have two options:

**1. Use the opposite kind of quotes.**
That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:

```python
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
```

**2. Escape the quotation mark with a backslash (`\`).**
With this method, you can use either single or double quotation marks to wrap the string itself:

```python
msg = 'It\'s a sunny day'
quote = "She said, \"Hello World\""
```

## Escape Sequences
The backslash can also be combined with other characters to represent characters that are hard to type directly in a string. These combinations are called **escape sequences**. Here are some common ones:

*   `\n` : a newline
*   `\t` : a tab
*   `\\` : a single backslash

```python
print('Hello\nworld')
# Hello
# world

print('Name:\tAlice')
# Name:  Alice

print('C:\\Users\\Alice')
# C:\Users\Alice
```
In the first example, `\n` makes `world` appear on a new line. In the second example, `\t` adds a tab between `Name:` and `Alice`. In the last example, each `\\` becomes a single backslash in the output.

## Checking for Substrings
Sometimes, you may need to check if a string contains one or more characters. For that, Python provides the `in` operator, which returns a boolean that specifies whether the character or characters exist in the string or not.

```python
my_str = 'Hello world'

print('Hello' in my_str) # True
print('hey' in my_str)   # False
print('hi' in my_str)    # False
print('e' in my_str)     # True
print('f' in my_str)     # False
```

## String Length and Indexing
To get the length of a string, you can use the built-in `len()` function.

```python
my_str = 'Hello world'
print(len(my_str)) # 11
```

Each character in a string has a position called an **index**. The index is zero-based, meaning that the index of the first character of a string is `0`, the index of the second character is `1`, and so on. To access a character by its index, you use square brackets `[]`:

```python
my_str = "Hello world"

print(my_str[0]) # H
print(my_str[6]) # W
```

Negative indexing is also allowed, so you can get the last character of any string with `-1`, and the second-to-last character with `-2`, and so on:

```python
my_str = 'Hello world'
print(my_str[-1]) # d
print(my_str[-2]) # l
```

## String Immutability
In Python, values can be **mutable** or **immutable**. A mutable value can be changed after it is created, while an immutable value cannot. You can point a variable at a new value, which is called **reassignment**, but you can't change an immutable value itself by adding, removing, or replacing any elements.

Strings are **immutable** in Python, but you can still reassign a variable to a different string:

```python
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
```

But direct modification of a string isn't allowed:

```python
greeting = 'hi'
greeting[0] = 'H'
# TypeError: 'str' object does not support item assignment
```

Integers, Floats, and Booleans are also immutable.

### Knowledge Check
**Q: How do you get the length of a string `s`?**
A: `len(s)`

**Q: How do you define a multiline string in Python?**
A: Using triple double quotes `"""` or triple single quotes `'''`

**Q: What does it mean that a string is immutable?**
A: A string cannot be directly modified by changing its individual characters.
