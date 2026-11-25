# ==========================================
# 1. Understanding Global and Local Scope
# ==========================================
global_var = "I'm a global variable"
print(global_var)

def trial(text):
    # 'text' is a local parameter. It shadows the global 'text' variable.
    text = 'I am a ' + text
    return text

text = 'local variable'
print(f'{trial(text)}')

# ==========================================
# 2. Functions Can Read Global Variables
# ==========================================
tax_rate = 0.1 # Global variable

def calculate_tax(price):
    tax = price * tax_rate # 'tax' is local, 'tax_rate' is global
    return tax

tax = calculate_tax(50)
print(tax_rate) # 0.1 (Global variable is accessible)
print(tax)      # 5.0 (Local variable returned and saved globally)

# ==========================================
# 3. Pass by Assignment
# ==========================================
# Python does not copy the object. It just assigns the local name to the same object.
def double_number(number):
    # number is a local name pointing to the same object as 'original'
    number = number * 2
    print(number) # 20 (local number changed)

original = 10
double_number(original)
print(original) # 10 (original is unchanged because integers are immutable)

# ==========================================
# 4. More Scope Practice
# ==========================================
discount = 2 # Global variable

def apply_discount(price):
    # Note: This math will do price - (price * 2), resulting in a negative number
    amount = price * discount 
    return price - amount 

print(f'{apply_discount(discount)}') 

# ==========================================
# 5. Interactive Calculator (From previous lesson)
# ==========================================
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

print("\n--- Simple Calculator ---")
number_1_str = input('Enter first number: ')

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
                num1 = float(number_1_str)
                num2 = float(number_2_str)
                
                if operation == '+': print(f'The result is: {add(num1, num2)}')
                elif operation == '-': print(f'The result is: {subtract(num1, num2)}')
                elif operation == '*': print(f'The result is: {multiply(num1, num2)}')
                elif operation == '/': print(f'The result is: {divide(num1, num2)}')
            except ValueError:
                print('Error: Please enter valid numeric values.')
    else:
        print('Please enter a valid operation (+, -, *, /).')