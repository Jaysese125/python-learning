# Build an Employee Profile Generator

In this workshop, we practiced string manipulation, type conversion, f-strings, and slicing by building an employee profile generator.

## 1. String Concatenation
You can combine strings using the `+` operator. If you need a space between them, you must explicitly add a space string `' '`.

```python
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name) # Output: John Doe
```

## 2. Augmented Assignment (`+=`)
To add text to the end of an existing string variable, you can use the `+=` operator. This is shorthand for `var = var + 'new text'`. Remember that strings are immutable, so this creates a new string and reassigns it.

```python
address = '123 Main Street'
address += ', Apartment 4B'
print(address) # Output: 123 Main Street, Apartment 4B
```

## 3. Type Conversion (`str()`) and `TypeError`
You cannot concatenate a string and a number (integer) directly. If you try, Python raises a `TypeError`. To fix this, you must convert the number to a string using the `str()` function.

```python
employee_age = 28
# employee_info = full_name + ' is ' + employee_age # This causes a TypeError!
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info) # Output: John Doe is 28 years old
```

## 4. F-Strings (String Interpolation)
To avoid messy string concatenation and `str()` conversions, Python 3.6 introduced **f-strings**. By adding an `f` before the quotes, you can embed variables directly inside curly braces `{}`.

```python
position = 'Data Analyst'
salary = 75000

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
# Output: Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
```

## 5. String Slicing
Slicing extracts a portion of a string using `string[start:stop]`. 
*   `start` is inclusive.
*   `stop` is exclusive (it stops *before* that index).

```python
employee_code = 'DEV-2026-JD-001'

# Positive Slicing
department = employee_code[0:3]  # Output: DEV
year_code = employee_code[4:8]   # Output: 2026
initials = employee_code[9:11]   # Output: JD

# Negative Slicing (extracts from the end)
last_three = employee_code[-3:]  # Output: 001
```

---

## Final Code:

```python
# 1. Basic String creation and concatenation
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

# 2. Augmented assignment
address = '123 Main Street'
address += ', Apartment 4B'

# 3. Type conversion and String Concatenation
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# 4. F-strings
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# 5. String Slicing
employee_code = 'DEV-2026-JD-001'

# Slicing the department
department = employee_code[0:3]
print(department)

# Slicing the year and initials
year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)

# Negative slicing for the last three characters
last_three = employee_code[-3:]
print(last_three)
```
