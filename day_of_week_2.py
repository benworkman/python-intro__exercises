day = int(raw_input ('Day (0-6)? '))

if day == 0:
    today = 'Sunday'
elif day == 1:
    today = 'Monday'
elif day == 2:
    today = 'Tuesday'
elif day == 3:
    today = 'Wednesday'
elif day == 4:
    today = 'Thursday'
elif day == 5:
    today = 'Friday'
else:
    today = 'Saturday'
if today == 'Saturday' or today == 'Sunday':
    print 'Sleep in.'
else:
    print 'Wake up!'
