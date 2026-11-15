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
The backslash can also be combined with other characters to represent characters that are hard to type directly in a string. These combinations are called **escape sequences**:

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

## Checking for Substrings
Python provides the `in` operator, which returns a boolean that specifies whether the character or characters exist in the string or not.

```python
my_str = 'Hello world'
print('Hello' in my_str) # True
print('hey' in my_str)   # False
```

## String Length and Indexing
To get the length of a string, use the built-in `len()` function. The index is zero-based, meaning the first character is `0`. You can also use negative indexing (e.g., `-1` for the last character).

```python
my_str = 'Hello world'
print(len(my_str)) # 11
print(my_str[0])   # H
print(my_str[-1])  # d
```

## String Immutability
Values can be **mutable** (changeable) or **immutable** (unchangeable). Strings are **immutable** in Python. You can reassign a variable to a new string, but you cannot modify the string directly by changing individual characters.

```python
greeting = 'hi'
greeting = 'hello' # Reassignment is fine
print(greeting) # hello

# greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
```

---

# What Are String Concatenation and String Interpolation?

## Concatenation Strings
You can combine multiple strings together with the plus (`+`) operator:

```python
my_str_1 = 'Hello'
my_str_2 = "World"
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World
```

## Repeating Strings
You can repeat a string by multiplying it with an integer using the `*` operator:

```python
sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) # hahaha
```

## Concatenating Strings with Numbers
Concatenation only works with strings. If you try to concatenate a string with a number, you'll get a `TypeError`. To fix this, convert the number into a string with the built-in `str()` function.

```python
name = 'John Doe'
age = 26
name_and_age = name + str(age)
print(name_and_age) # John Doe26
```

You can also use the augmented assignment operator (`+=` and `*=`) to perform the operation and assign it back to the same variable:

```python
name = 'John Doe'
age = 26
name_and_age = name
name_and_age += str(age)
print(name_and_age) # John Doe26

sound = 'ha'
sound *= 3
print(sound) # hahaha
```

## String Interpolation
Inserting variables and expressions into a string is called **string interpolation**. Python uses **f-strings** (formatted string literals) for this. F-strings start with an `f` before the quotes, and you embed variables or expressions inside curly braces `{}`.

```python
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I\'m {age} years old'
print(name_and_age) # My name is John Doe and I'm 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
```
*Note: You don't need to convert non-string types with `str()` when using f-strings.*

---

# What is String Slicing and How Does it Work?

String slicing lets you extract a portion of a string. The basic syntax is `string[start:stop]`. The `stop` index is **non-inclusive**.

```python
my_str = 'Hello world'
print(my_str[1:4]) # ell
```

You can omit the start or stop indices, and Python will default to `0` or the end of the string, respectively:

```python
my_str = 'Hello world'
print(my_str[:7])  # Hello w
print(my_str[8:])  # rld
print(my_str[:])   # Hello world
```
*Note: Slicing a string does not modify the original string.*

## The Step Parameter
You can add an optional `step` parameter: `string[start:stop:step]`. It specifies the increment between each index.

```python
my_str = 'Hello world'
print(my_str[0:11:2]) # HloWrd
```

A helpful trick is to reverse a string by setting `step` to `-1`:

```python
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
```

---

# What are some common string methods?

A method is a function that you call on a value. To call a string method, write the string or its variable name followed by a dot and the method call.

*   **`upper()`**: Returns a new string with all characters converted to uppercase.
*   **`lower()`**: Returns a new string with all characters converted to lowercase.
*   **`strip()`**: Returns a new string with leading and trailing whitespaces removed.
*   **`replace(old, new)`**: Returns a new string with all occurrences of `old` replaced by `new`.
*   **`split(separator)`**: Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.
*   **`join()`**: Joins the strings in a collection into a single string with a separator.
*   **`startswith(prefix)`**: Returns a boolean indicating if a string starts with the specified prefix.
*   **`endswith(suffix)`**: Returns a boolean indicating if a string ends with the specified suffix.
*   **`find(substring)`**: Returns the index of the first occurrence of `substring`, or `-1` if it doesn't find one.
*   **`count(substring)`**: Returns the number of non-overlapping occurrences of a substring.
*   **`capitalize()`**: Returns a new string with the first character capitalized and the other characters lowercased.
*   **`isupper()`**: Returns `True` if the string contains at least one cased character and all cased characters are uppercase.
*   **`islower()`**: Returns `True` if the string contains at least one cased character and all cased characters are lowercase.
*   **`title()`**: Returns a new string with the first letter of each word capitalized.

### Knowledge Check
**Q: Which methods check if all letters in a string are uppercase and if all letters are lowercase?**
A: `isupper()` and `islower()`

**Q: How can you replace all occurrences of one or more parts of a string with another string?**
A: Using the `replace()` method with old and new text.

**Q: What does the `upper()` method do?**
A: Converts all characters to uppercase.