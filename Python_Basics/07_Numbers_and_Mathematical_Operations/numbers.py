# --- Integer Arithmetic ---
add_int_1 = 69
add_int_2 = 67
print('Integer Addition:', add_int_1 + add_int_2)

sub_int_1 = 69
sub_int_2 = 67
print('Integer Subtraction:', sub_int_1 - sub_int_2)

mul_int_1 = 69
mul_int_2 = 67
print('Integer Multiplication:', mul_int_1 * mul_int_2)

div_int_1 = 69
div_int_2 = 67
print('Integer Division:', div_int_1 / div_int_2)

print('-------------------------------------')

# --- Float Arithmetic ---
sum_float_1 = 12.5
sum_float_2 = 9.11
print('Float Addition:', sum_float_1 + sum_float_2)

sub_float_1 = 12.5
sub_float_2 = 9.11
print('Float Subtraction:', sub_float_1 - sub_float_2)

mul_float_1 = 12.5
mul_float_2 = 9.11
print('Float Multiplication:', mul_float_1 * mul_float_2)

div_float_1 = 12.5
div_float_2 = 9.11
print('Float Division:', div_float_1 / div_float_2)

print('-------------------------------------')

# --- Mixing Integers and Floats ---
my_int = 67
my_float = 9.11
sum_int_float = my_int + my_float
print('Mixed Addition:', sum_int_float)
print('Mixed Type:', type(sum_int_float))

print('-------------------------------------')

# --- Complex Arithmetic Operations ---
mod_int_1 = 67
mod_int_2 = 69
mod_floats_1 = 12.5
mod_floats_2 = 9.11
print('Integer Modulo:', mod_int_1 % mod_int_2)
print('Float Modulo:', mod_floats_1 % mod_floats_2)

floor_int_1 = 69
floor_int_2 = 67
floor_float_1 = 12.5
floor_float_2 = 9.11
print('Integer Floor:', floor_int_1 // floor_int_2)
print('Float Floor:', floor_float_1 // floor_float_2)

exp_int_1 = 6
exp_int_2 = 7
exp_float_1 = 12.5
exp_float_2 = 9.11
print('Integer Exponentiation:', exp_int_1 ** exp_int_2)
print('Float Exponentiation:', exp_float_1 ** exp_float_2)

print('-------------------------------------')

# --- Type Conversions ---
int_to_float = 9
print('Int to Float:', float(int_to_float), type(float(int_to_float)))

float_to_int = 9.11
print('Float to Int:', int(float_to_int), type(int(float_to_int)))

string_to_int = '67'
string_to_float = '69.69'
print('String to Int:', int(string_to_int), type(int(string_to_int)))
print('String to Float:', float(string_to_float), type(float(string_to_float)))

print('-------------------------------------')

# --- Other Functions ---
infinity = float('inf')
print('Infinity:', infinity, type(infinity))

round_num = 9.6969
print('Rounded:', round(round_num, 2))

abs_num = -67
print('Absolute Value:', abs(abs_num))

# pow(base, exp, mod) -> (base**exp) % mod
print('Power with Modulo:', pow(6, 7, 9))

print('-------------------------------------')

# --- Augmented Assignments ---
aug_var = 5
aug_var += 5
print(f'Add: {aug_var}')

aug_var -= 5
print(f'Subtract: {aug_var}')

aug_var *= 2
print(f'Multiply: {aug_var}')

aug_var /= 2
# Note: Division always creates a float, so we cast it to int for cleaner display
print(f'Divide: {int(aug_var)}') 

aug_var = 69 # Resetting the variable to an integer for the next operations

aug_var %= 12
print(f'Modulo: {aug_var}')

aug_var //= 2
print(f'Floor: {aug_var}')

aug_var **= 2
print(f'Exponent: {aug_var}')

print(f'Rounded: {round(aug_var, 2)}')

print('-------------------------------------')

# --- F-String Number Formatting ---
# Formatting is useful for displaying trailing zeros (e.g., for prices)
to_round = 9.10101

# Using round() returns a float (no trailing zeros)
round_format = round(to_round, 2)
print('Using round():', round_format) # Prints 9.1

# Using f-string formatting displays exactly 2 decimal places
# Note: f-string formatting returns a STRING. We wrap it in float() 
# so we can still use it in calculations if needed.
fstring_display = f'{to_round:.2f}'
fstring_format = float(fstring_display) 

print('Using f-string:', fstring_format, type(fstring_format)) # Prints 9.1 (as a float)
print('Value unchanged:', to_round) # Value doesn't change
