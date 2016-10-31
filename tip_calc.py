bill = float(int(raw_input("Total Bill Amount?: ")))
service = raw_input("Level of Service? ")
people = int(raw_input("How many members are in your party "))
tip =
overall = (bill + tip)
divided= overall / people
if service == "good":
    print "tip: $%.2f " % tip
    print "total $%.2f " % overall
    print "each $%.2f " % divided
elif service == "fair":
    print "tip total: $%.2f " % tip
    print "total $%.2f " % overall
    print "each $%.2f " % divided
else:
    service == "bad"
    print "tip total: $%.2f " % tip
    print "total $%.2f " % overall
    print "each $%.2f " % divided
