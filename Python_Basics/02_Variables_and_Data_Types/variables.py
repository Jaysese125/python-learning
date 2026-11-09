# Define variables using snake_case
first_name = 'Jay'
last_name = 'Sese'
age = 22

# Variable names cannot start with numbers. Strings are used with single quotes.

# ----- Print function -----
print('Hello world!')
print('My name is', 'Christian', 'Jay', 'Sese')

# ----- Common Data types -----
str_var = 'string'
int_var = 123
float_var = 3.14
bool_var = True

# The value of the variable dictates what kind of data type the variable holds. 
# This is called a dynamically typed programming language.

# ----- type() Function -----
# The type() function checks what kind of data type the variable holds

print(type(str_var))   # Output: <class 'str'>
print(type(int_var))   # Output: <class 'int'>
print(type(float_var)) # Output: <class 'float'>
print(type(bool_var))  # Output: <class 'bool'>

print("-" * 20) # This just prints a line of dashes to separate the output

# ----- isinstance() Function -----
# The isinstance() function is used to check if the variable is a specific data type.
# It returns True or False.

print(isinstance(str_var, str))
print(isinstance(str_var, (str, bool))) # If you want to check two data types in one go

print(isinstance(int_var, int))
print(isinstance(int_var, (int, bool))) 

print(isinstance(float_var, float))
print(isinstance(float_var, (int, float))) 

print(isinstance(bool_var, bool))
print(isinstance(bool_var, (bool, int)))