# --- Comparison Operators ---
num_1 = 911
num_2 = 67

print(num_1 == num_2)  # False
print(num_1 != num_2)  # True
print(num_1 > num_2)   # True
print(num_1 < num_2)   # False
print(num_1 >= num_2)  # True
print(num_1 <= num_2)  # False

print("\n--- Simple Calculator ---")
# Simple Calculator
input_1 = 5
input_2 = 2
selected_operation = 'operation_times'

if selected_operation == 'operation_add':
    print(f'The Sum of {input_1} and {input_2} is {input_1 + input_2}')
elif selected_operation == 'operation_minus':
    print(f'The Difference of {input_1} and {input_2} is {input_1 - input_2}')
elif selected_operation == 'operation_times':
    print(f'The Product of {input_1} and {input_2} is {input_1 * input_2}')
elif selected_operation == 'operation_divide':
    print(f'The Quotient of {input_1} and {input_2} is {input_1 / input_2}')
else:
    print('Please Select an Operation')

print("\n--- Boolean Operators ---")
# Boolean Operators
age = 22
employed = False
have_license = True
have_car = False

if have_license and have_car:
    print('You can drive your own car')
elif employed or have_car:
    print('Find a job and save some money for a car')
elif not have_license:
    print('You can\'t drive')
else:
    print('No future')

print("\n--- Identity Operators ---")
# Checking for None
response = None
print(response == None)      # True (Works, but not recommended)
print(response is None)      # True (Recommended)
print(response != None)      # False
print(response is not None)  # False
print(bool(response))        # False

# Comparing a string 'None' to the actual None object
response = 'None'
print(bool(response))        # True (It's a non-empty string)

response = None
if response is not None:
    print('An answer was given')
else:
    print('No answer yet')   # This will print because response is None

# Checking for True and False
response = True
print(response == True)     # True
print(response is True)     # True
print(response == False)    # False
print(response is False)    # False
print(response != True)     # False
print(response is not True) # False
print(response != False)    # True
print(response is not False) # True

# *Note: == checks the value inside the variable. 
# is checks if they refer to the exact same object in memory.

# A practical use case for identity operators:
response = None
if response is True:
    print('yes')
elif response is False:
    print('no')
elif response is None:
    print('no answer')
else:
    print('something is wrong')