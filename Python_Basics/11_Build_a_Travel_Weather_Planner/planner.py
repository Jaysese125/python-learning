distance_mi = 9
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print('False')
elif distance_mi <= 1 and not is_raining:
    print('True')
elif distance_mi > 1 and distance_mi <= 6 and not is_raining and has_bike:
    print('True')
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print('True')
else:
    print('False')

    
# IMPROVED VERSION

distance_mi = 9
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    print(not is_raining)
elif distance_mi <= 6:
    print(not is_raining and has_bike)
else:
    print(has_car or has_ride_share_app)

#if not distance_mi handles zero and other falsy distances.
#elif distance_mi <= 1 handles short distances.
#elif distance_mi <= 6 handles distances between 1 and 6 miles. We don't need distance_mi > 1 because the previous branch already handled that.
#else handles everything greater than 6 miles.
#print() displays actual Boolean values instead of strings.

