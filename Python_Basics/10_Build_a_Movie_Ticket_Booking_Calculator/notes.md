# Build a Movie Ticket Booking Calculator

In this workshop, we practiced using booleans, comparison operators, and conditional statements to build a movie ticket booking calculator.

## 1. Basic Setup and Eligibility
We start by defining the base price, user age, seat type, and show time.
*   The `>` (greater than) operator checks if the user is older than 17.
*   The `>=` (greater than or equal to) operator checks if the user is 21 or older.
*   The `else` clause handles the case when the `if` condition is `False`.

```python
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')
```

## 2. Truthy Values and Membership Discount
In Python, `if` conditions rely on the **truthiness** of values. Non-zero numbers, non-empty strings, and `True` are truthy.
We use the `and` operator to ensure the user is a member **and** 21 or older to get a discount. We format the final discount using the `.2f` f-string specification.

```python
is_member = False
is_weekend = False
discount = 0

if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

print(f'Discount: {discount:.2f}')
```

## 3. Extra Charges and the `or` Operator
The `or` operator checks if at least one condition is true. We apply extra charges if the show is in the evening **or** if it is the weekend.

```python
extra_charges = 0

if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print(f'Extra charges: {extra_charges:.2f}')
```

## 4. Complex Conditions and Precedence
When combining `and` and `or`, `and` has higher precedence (it is evaluated first). You can use parentheses `()` to change how conditions are grouped.

```python
# In this condition, (show_time != 'Evening' or is_member) is evaluated first.
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
```

## 5. Nested `if` Statements and `elif`
We can place an `if` statement inside another `if` statement. This is called a **nested** `if`. We use this to calculate service charges based on the seat type.

```python
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
        
    print(f'Service charges: {service_charges:.2f}')
```

## 6. Final Calculation
Finally, we calculate the final ticket price by adding extra charges and service charges to the base price, and subtracting the discount.

```python
    final_price = base_price + extra_charges + service_charges - discount
    print(f'Final price of ticket: {final_price:.2f}')

else:
    print('Ticket booking failed due to restrictions')
```