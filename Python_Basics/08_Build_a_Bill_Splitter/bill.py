# --- Bill Splitter Workshop ---

# 1. Setup Variables
running_total = 0
num_of_friends = 4

# Food costs (floats)
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# 2. Calculate Total Cost
running_total += appetizers + main_courses + desserts + drinks
# Note: Wrapped in round() to fix floating-point precision issues for display
print(f'Total bill so far: {round(running_total, 2)}')

# 3. Calculate Tip (25%)
tip = running_total * 0.25
print(f'Tip amount: {round(tip, 2)}')

# 4. Add Tip to Running Total
running_total += tip
print(f'Total with tip: {round(running_total, 2)}')

# 5. Split the Bill
final_bill = running_total / num_of_friends
print(f'Bill per person: {final_bill}')

# 6. Round to Two Decimal Places
each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')