meal = float(raw_input("Meal total "))

service = raw_input("How was the service? ")
people = int(raw_input("How many members are in your party "))

if service == "good":
    tip = 0.20
elif service == "fair":
    tip = 0.15
elif service == "bad":
    tip = 0.10

tip_total = meal * tip
meal_total = tip_total + meal

print "$%.2f total" % meal
print "$%.2f tip amount" % tip_total
print "$%.2f each" % (meal_total / people)
