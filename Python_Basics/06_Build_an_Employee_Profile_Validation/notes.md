# Build an Employee Profile Validator

## Overview

This workshop practices Python string methods for inspecting, cleaning, and formatting employee information.

You will work with:

- f-strings
- `.find()`
- string slicing
- the `in` keyword
- `.title()`, `.strip()`, `.lower()`, and `.upper()`
- `.replace()`
- `.split()` and `.join()`
- `.startswith()` and `.endswith()`
- `.count()`

---

## 1. Create an email variable

A string is text enclosed in quotes. Create a variable named `email`:

```python
email = 'alice.johnson@company.com'
```

## 2. Display a variable with an f-string

An f-string lets you insert a variable into a string. Put `f` before the opening quote and place the variable inside curly braces `{}`.

```python
name = 'Alice'
print(f'Hello, {name}')  # Hello, Alice

print(f'Email: {email}')  # Email: alice.johnson@company.com
```

## 3. Find a character with `.find()`

The `.find()` method returns the index of the first occurrence of a substring. Python uses zero-based indexing, so the first character is at index `0`.

```python
text = 'hello'
print(text.find('e'))  # 1
```

Find the position of `@` in the email:

```python
at_position = email.find('@')
print(f'Position of @: {at_position}')  # Position of @: 13
```

**Important:** `.find()` returns `-1` if the substring is not found.

## 4. Extract text with slicing

Slicing gets part of a string. The syntax `string[:end]` returns everything from the beginning up to, but not including, `end`.

```python
text = 'hello world'
print(text[:5])  # hello
```

Use the position of `@` to extract the email username:

```python
username = email[:at_position]
print(f'Username: {username}')  # Username: alice.johnson
```

## 5. Check whether text exists with `in`

The `in` keyword checks whether a substring exists in a string. It returns `True` or `False`.

```python
sentence = 'I love Python'

print('Python' in sentence)  # True
print('Java' in sentence)    # False
```

Check whether the email contains `@`:

```python
has_at = '@' in email
print(f'Has @ symbol: {has_at}')  # Has @ symbol: True
```

## 6. Check for a domain ending

Check whether `.com` appears in the email:

```python
has_com = '.com' in email
print(f'Has .com: {has_com}')  # Has .com: True
```

This checks whether `.com` appears anywhere in the string. To check whether the email specifically ends in `.com`, use `.endswith()` (covered in Step 18).

## 7. Create a messy name

Real-world data may contain extra spaces and inconsistent capitalization.

```python
messy_name = '  sARaH dAVis  '
```

There are two spaces before and after the name.

## 8. Display the original name

Putting quotes around the value makes the extra spaces easier to see:

```python
print(f"Original name: '{messy_name}'")
# Original name: '  sARaH dAVis  '
```

## 9. Capitalize each word with `.title()`

The `.title()` method capitalizes the first letter of each word.

```python
lowercase = 'hello world'
title_case = lowercase.title()
print(title_case)  # Hello World
```

Apply it to the name:

```python
clean_name = messy_name.title()
```

At this point, the leading and trailing spaces are still present.

## 10. Remove surrounding whitespace with `.strip()`

The `.strip()` method removes whitespace from the beginning and end of a string. You can chain it with `.title()`:

```python
messy = '  hello world  '
clean = messy.strip().title()
print(clean)  # Hello World
```

Clean and display the employee name:

```python
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")
# Cleaned name: 'Sarah Davis'
```

## 11. Normalize an email with `.lower()`

The `.lower()` method converts all letters in a string to lowercase. It can also be chained with `.strip()`.

```python
messy = '  HELLO WORLD  '
clean = messy.strip().lower()
print(clean)  # hello world
```

Create and clean an email address:

```python
messy_email = '  SARAH.DAVIS@COMPANY.COM  '
clean_email = messy_email.strip().lower()

print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")
```

Output:

```text
Original email: '  SARAH.DAVIS@COMPANY.COM  '
Cleaned email: 'sarah.davis@company.com'
```

## 12. Convert text to uppercase with `.upper()`

The `.upper()` method converts all letters to uppercase. This can be useful for name badges or headings.

```python
name = 'sarah davis'
badge = name.upper()
print(badge)  # SARAH DAVIS
```

Create a name badge from the cleaned name:

```python
name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')  # Name badge: SARAH DAVIS
```

## 13. Find and extract the username from the cleaned email

Use `.find()` to locate `@`, then use slicing to get everything before it.

```python
at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]

print(f'Email: {clean_email}')
print(f'Username: {email_user}')
```

Output:

```text
Email: sarah.davis@company.com
Username: sarah.davis
```

## 14. Replace characters with `.replace()`

The `.replace(old, new)` method replaces every occurrence of `old` with `new`.

```python
text = 'john.doe'
name = text.replace('.', ' ').title()
print(name)  # John Doe
```

Replace the dot in the email username with a space, then capitalize each word:

```python
display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')  # Display name: Sarah Davis
```

## 15. Remove unwanted characters with `.replace()`

Replacing a character with an empty string (`''`) removes it.

```python
phone = '123-456-7890'
phone_clean = phone.replace('-', '')

print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')
```

Output:

```text
Phone with dashes: 123-456-7890
Phone without dashes: 1234567890
```

## 16. Split a string into a list with `.split()`

The `.split(separator)` method divides a string wherever the separator appears and returns a list.

```python
fruits = 'apple, banana, cherry'
parts = fruits.split(', ')
print(parts)  # ['apple', 'banana', 'cherry']
```

Split an address at each comma followed by a space:

```python
full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')
```

Output:

```text
Address parts: ['123 Main Street', 'Springfield', 'IL']
```

## 17. Join list items into a string with `.join()`

The `.join()` method combines strings from an iterable, using the string before `.join()` as the separator.

```python
parts = ['apple', 'banana', 'cherry']
joined = ' - '.join(parts)
print(joined)  # apple - banana - cherry
```

Join the address parts with ` | `:

```python
rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')
# Rejoined: 123 Main Street | Springfield | IL
```

## 18. Check the beginning of a string with `.startswith()`

The `.startswith(prefix)` method returns `True` if a string begins with the specified prefix.

```python
code = 'EMP-001'
print(code.startswith('EMP'))  # True
print(code.startswith('001'))  # False
```

Check the employee code:

```python
employee_code = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')
```

## 19. Check the end of a string with `.endswith()`

The `.endswith(suffix)` method returns `True` if a string ends with the specified suffix.

```python
code = 'EMP-001'
print(code.endswith('EMP'))  # False
print(code.endswith('001'))  # True
```

Check whether the cleaned email ends in `.com`:

```python
ends_with_com = clean_email.endswith('.com')
```

## 20. Display the employee code and email checks

```python
print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')
```

Output:

```text
Code: EMP-2024-SD
Starts with EMP: True
Clean email: sarah.davis@company.com
Ends with .com: True
```

## 21. Count characters with `.count()`

The `.count(substring)` method returns the number of non-overlapping occurrences of a substring.

```python
text = 'banana'
print(text.count('a'))  # 3
```

Count the dots in the email and the dashes in the employee code:

```python
dot_count = clean_email.count('.')
dash_count = employee_code.count('-')
```

## 22. Display the counts

```python
print(f'Dots in email: {dot_count}')
print(f'Dashes in code: {dash_count}')
```

Output:

```text
Dots in email: 2
Dashes in code: 2
```

---

## Complete working example

This is the consolidated version of the workshop code. It runs from top to bottom without repeating earlier code blocks.

```python
# Email inspection
email = 'alice.johnson@company.com'
print(f'Email: {email}')

at_position = email.find('@')
print(f'Position of @: {at_position}')

username = email[:at_position]
print(f'Username: {username}')

has_at = '@' in email
print(f'Has @ symbol: {has_at}')

has_com = '.com' in email
print(f'Has .com: {has_com}')

# Name cleanup
messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

# Email cleanup
messy_email = '  SARAH.DAVIS@COMPANY.COM  '
clean_email = messy_email.strip().lower()

print(f"Original email: '{messy_email}'")
print(f"Cleaned email: '{clean_email}'")

# Name badge
name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')

# Extract email username and create display name
at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]

print(f'Email: {clean_email}')
print(f'Username: {email_user}')

display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')

# Clean a phone number
phone = '123-456-7890'
phone_clean = phone.replace('-', '')

print(f'Phone with dashes: {phone}')
print(f'Phone without dashes: {phone_clean}')

# Split and rejoin an address
full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')

rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

# Employee code and email checks
employee_code = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')
ends_with_com = clean_email.endswith('.com')

print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')

# Count punctuation
dot_count = clean_email.count('.')
dash_count = employee_code.count('-')

print(f'Dots in email: {dot_count}')
print(f'Dashes in code: {dash_count}')
```

## Quick reference

| Method / operator | What it does | Example |
|---|---|---|
| `f'...'` | Inserts variable values into a string | `f'Hello, {name}'` |
| `.find(x)` | Finds the first position of `x`; returns `-1` if absent | `email.find('@')` |
| `text[start:end]` | Extracts a slice of a string | `email[:at_position]` |
| `x in text` | Checks whether `x` exists in `text` | `'@' in email` |
| `.title()` | Capitalizes the first letter of each word | `name.title()` |
| `.strip()` | Removes whitespace from both ends | `name.strip()` |
| `.lower()` | Converts letters to lowercase | `email.lower()` |
| `.upper()` | Converts letters to uppercase | `name.upper()` |
| `.replace(old, new)` | Replaces occurrences of one substring with another | `phone.replace('-', '')` |
| `.split(separator)` | Splits a string into a list | `address.split(', ')` |
| `.join(items)` | Joins strings using a separator | `' | '.join(parts)` |
| `.startswith(x)` | Checks whether a string begins with `x` | `code.startswith('EMP')` |
| `.endswith(x)` | Checks whether a string ends with `x` | `email.endswith('.com')` |
| `.count(x)` | Counts non-overlapping occurrences of `x` | `email.count('.')` |

**Workshop complete:** You used Python string operations to inspect, clean, format, split, join, and validate basic employee profile data.
