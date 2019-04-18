"""
Prompt the user for two things:

The total bill amount
The level of service, which can be one of the following: good, fair, or bad
Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

good -> 20%
fair -> 15%
bad -> 10%
"""

bill_total = float(input("Total bill amount?"))
service_level = (input("Level of service?"))

if service_level == "good":
    tip_percent = .20
    tip_amount = bill_total * tip_percent
    final_bill_total = bill_total + tip_amount
    print("Tip amount: $%.2f" % (tip_amount,))
    print("Total amount: $%.2f" % (final_bill_total,))
elif service_level == "fair":
    tip_percent = .15
    tip_amount = bill_total * tip_percent
    final_bill_total = bill_total + tip_amount
    print("Tip amount: $%.2f" % (tip_amount,))
    print("Total amount: $%.2f" % (final_bill_total,))    
elif service_level == "bad":
    tip_percent = .10
    tip_amount = bill_total * tip_percent
    final_bill_total = bill_total + tip_amount
    print("Tip amount: $%.2f" % (tip_amount,))
    print("Total amount: $%.2f" % (final_bill_total,))

    
