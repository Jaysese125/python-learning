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