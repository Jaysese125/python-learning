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