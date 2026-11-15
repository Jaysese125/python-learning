# You can use either single or double quotes for strings
my_str_1 = 'Single'
my_str_2 = "Double"

# You can use triple single or double quotes for multiline strings
my_str_3 = '''Multiline Using
Triple Single Quotes'''
my_str_4 = """Multiline Using
Triple Double Quotes"""

# You can use the opposite kind of quotes if a string contains single or double quotes.
my_str_5 = 'I use Single Quotes for this string so that I can use "Double Quotes" inside it'
my_str_6 = "I use Double Quotes for this string so that I can use 'Single Quotes' inside it"

# You can use a backslash (\) so that you can use either single or double quotes inside a string.
my_str_7 = 'Single Quote string but I can use \' Single Quotes\' inside it using backslash'
my_str_8 = "Double Quote string but I can use \" Double Quotes\" inside it using backslash"

# You can combine a backslash with other characters to create an escape sequence.
my_str_9 = 'I can use \n to create a new line'
# I can use
# to create a new line

my_str_10 = "I can use \t to create a tab space"
# I can use 	 to create a tab space

my_str_11 = 'I can use \\ to create a backslash'
# I can use \ to create a backslash

# You can check if a string contains one or more characters using the in operator.
my_str_12 = 'Hello World'
print('Hello' in my_str_12)  # Output: True
print('Python' in my_str_12)  # Output: False
print('Hello' not in my_str_12)  # Output: False
print('Python' not in my_str_12)  # Output: True
print('World' in my_str_12)  # Output: True
print('world' in my_str_12)  # Output: False
print('!' in my_str_12)  # Output: False
print('!' not in my_str_12)  # Output: True
# It is case-sensitive, so 'World' is different from 'world'.

# You can use the len() function to get the length of a string.
print(len(my_str_12))  # Output: 11
# Because Python uses zero-based indexing, meaning the first character of a string is at index 0, the last character is at index len(string) - 1.
# H = 0
# e = 1
# l = 2
# l = 3
# o = 4
#   = 5 (space is at index 5)
# W = 6
# o = 7
# r = 8
# l = 9
# d = 10

# You can use indexing to access individual characters in a string.
print(my_str_12[0])  # Output: H
print(my_str_12[6])  # Output: W

# You can use negative indexing to access characters from the end of a string.
print(my_str_12[-1])  # Output: d
print(my_str_12[-2])  # Output: l

# You cannot change individual characters in a string because a string is an immutable data type.
# my_str_12[0] = 'H' Will result in an Error
# TypeError: 'str' object does not support item assignment

# You can concatenate strings using the + operator. 
my_str_13 = 'Hello'
my_str_14 = 'World'
my_str_15 = my_str_13 + ' ' + my_str_14
print(my_str_15)  # Output: Hello World

# You can repeat strings using the * operator.
my_str_16 = 'Hello '
my_str_17 = my_str_16 * 3
print(my_str_17)  # Output: Hello Hello Hello

# You can only concatenate strings with other strings. You cannot concatenate a string with a number or any other data type.
# my_str_18 = 'Hello' + 5 Will result in an Error
# TypeError: can only concatenate str (not "int") to str

# You can use the str() function to convert a number to a string so that you can concatenate it with other strings.
my_str_19 = 'Hello' + str(5)

# You can use augmented assignment operators to concatenate and repeat strings.
my_str_20 = 'Hello'
my_str_20 += ' World'  # Equivalent to my_str_20 = my_str_20 + ' World'
print(my_str_20)  # Output: Hello World

my_str_21 = 'Hello '
my_str_21 *= 3  # Equivalent to my_str_21 = my_str_21 * 3
print(my_str_21)  # Output: Hello Hello Hello

# You can insert variables into strings using f-strings (formatted string literals).
name = 'John'
age = 30
message = f'Hello, my name is {name} and I am {age} years old.'
print(message)  # Output: Hello, my name is John and I am 30 years old.

# You can also perform calculations inside f-strings without needing to convert numbers to strings.
num1 = 10
num2 = 20
result = f'The sum of {num1} and {num2} is {num1 + num2}.'
print(result)  # Output: The sum of 10 and 20 is 30.

# You can slice a string to get a substring using the syntax string[start:end], where start is the index of the first character you want to include and end is the index of the first character you want to exclude.
my_str_22 = 'Hello World'
print(my_str_22[0:5])  # Output: Hello
# Start:
# 0 = H
# 1 = e
# 2 = l
# 3 = l
# 4 = o
# End:
# 5 = (space) is excluded

# You can omit the start index to slice from the beginning of the string, and you can omit the end index to slice to the end of the string.
print(my_str_22[:5])  # Output: Hello
print(my_str_22[6:])  # Output: World
print(my_str_22[0:11])  # Output: Hello World

# You can also use step parameter in slicing to skip characters in the string. The syntax is string[start:end:step].
print(my_str_22[0:11:2])  # Output: HloWrd

# You can reverse a string using slicing with a negative step.
print(my_str_22[::-1])  # Output: dlroW olleH

# You can use a method called upper() to convert a string to uppercase.
my_str_23 = 'Hello World'
print(my_str_23.upper())  # Output: HELLO WORLD

# You can use a method called lower() to convert a string to lowercase.
print(my_str_23.lower())  # Output: hello world

# You can use a method called strip() to remove whitespace from the beginning and end of a string.
my_str_24 = '   Hello World   '
print(my_str_24.strip())  # Output: Hello World

# You can use a method called replace() to replace a substring with another substring in a string.
my_str_25 = 'Hello World'
print(my_str_25.replace('World', 'Python'))  # Output: Hello Python 

# You can use a method called split() to split a string into a list of substrings based on a delimiter.
my_str_26 = 'Hello,World,Python'
print(my_str_26.split(','))  # Output: ['Hello', 'World', 'Python']

# You can use a method called join() to join a list of strings into a single string with a specified delimiter.
my_list = ['Hello', 'World', 'Python'] 
print(','.join(my_list))  # Output: Hello,World,Python

# You can use a method called startswith() to check if a string starts with a specified substring.
my_str_27 = 'Hello World'
print(my_str_27.startswith('Hello'))  # Output: True
print(my_str_27.startswith('World'))  # Output: False

# You can use a method called endswith() to check if a string ends with a specified substring.
print(my_str_27.endswith('World'))  # Output: True
print(my_str_27.endswith('Hello'))  # Output: False

# You can use a method called find() to find the index of the first occurrence of a specified substring in a string. If the substring is not found, it returns -1.
print(my_str_27.find('World'))  # Output: 6
print(my_str_27.find('Python'))  # Output: -1

# You can use a method called count() to count the number of occurrences of a specified substring in a string.
my_str_28 = 'Hello World, Hello Python'
print(my_str_28.count('Hello'))  # Output: 2
print(my_str_28.count('World'))  # Output: 1

# You can use a method called capitalize() to capitalize the first character of a string and make all other characters lowercase.
my_str_29 = 'hello world'
print(my_str_29.capitalize())  # Output: Hello world

# You can use a method called isupper() to check if all characters in a string are uppercase.
my_str_30 = 'HELLO WORLD'
print(my_str_30.isupper())  # Output: True

# You can use a method called islower() to check if all characters in a string are lowercase.
my_str_31 = 'hello world'
print(my_str_31.islower())  # Output: True

# You can use a method called title() to capitalize the first character of each word in a string.
my_str_32 = 'hello world'
print(my_str_32.title())  # Output: Hello World