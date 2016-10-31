# now we have to try to make the program decide wether we should
# work or sleep in
# these are the days of the week labeled "week"
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# these are the numbers that the user will input
# the user will input 0-6 to represent the array
# which represents the days within a week
dayofweek = int(raw_input('Day (0-6?) '))
today = week[dayofweek]
if today == (0, 6):
    print ('Sleep in!.')
elif today == (1, 2, 3, 4, 5):
    print ('Wake up!.')
