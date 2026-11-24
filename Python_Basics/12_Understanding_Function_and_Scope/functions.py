# --- Understanding Functions and Scope ---

# 1. Define custom functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# 2. Interactive Calculator
print("--- Simple Calculator ---")

number_1_str = input('Enter first number: ')

# Check if the user typed nothing (empty string is falsy)
if not number_1_str:
    print('Please enter a number.')
else:
    operation = input('Enter Operation (+, -, *, /): ')
    
    if operation in ['+', '-', '*', '/']:
        number_2_str = input('Enter second number: ')
        
        if not number_2_str:
            print('Please enter a second number.')
        else:
            try:
                # Convert strings to floats so we can do math
                num1 = float(number_1_str)
                num2 = float(number_2_str)
                
                if operation == '+':
                    print(f'The result is: {add(num1, num2)}')
                elif operation == '-':
                    print(f'The result is: {subtract(num1, num2)}')
                elif operation == '*':
                    print(f'The result is: {multiply(num1, num2)}')
                elif operation == '/':
                    print(f'The result is: {divide(num1, num2)}')
            except ValueError:
                print('Error: Please enter valid numeric values.')
    else:
        print('Please enter a valid operation (+, -, *, /).')

# --- Returning Values Example ---
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(f"\nReturn test: calculate_sum(3, 1) = {my_sum}")