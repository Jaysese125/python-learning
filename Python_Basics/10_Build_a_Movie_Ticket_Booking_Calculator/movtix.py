# --- Movie Ticket Booking Calculator ---

# 1. Initial Setup
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# 2. Basic Eligibility Checks
if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# 3. Membership Discount (Truthy check and 'and' operator)
is_member = False
is_weekend = False
discount = 0

if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print(f'Discount: {discount:.2f}')

# 4. Extra Charges ('or' operator)
extra_charges = 0

if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print(f'Extra charges: {extra_charges:.2f}')

# 5. Complex Condition with Parentheses
# (age >= 18 AND not Evening) OR is_member
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
    
    # 6. Nested If Statements for Service Charges
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print(f'Service charges: {service_charges:.2f}')
    
    # 7. Final Calculation
    final_price = base_price + extra_charges + service_charges - discount
    print(f'Final price of ticket: {final_price:.2f}')
    
else:
    print('Ticket booking failed due to restrictions')
