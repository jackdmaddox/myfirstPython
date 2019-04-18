"""
Prompt the user for two things:

Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:


The total bill amount
The level of service, which can be one of the following: good, fair, or bad
Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

good -> 20%
fair -> 15%
bad -> 10%
"""

bill_total = float(input("Total bill amount?"))
service_level = (input("Level of service?"))
number_people = int(input("Split how many ways?"))

def tipcalc(bill_total, service_level, number_people):
    tip_amount = bill_total * tip_percent
    final_bill_total = bill_total + tip_amount
    per_person_amount = final_bill_total / number_people

    if service_level == "good":
        #tip_percent = .20
        #tip_amount = bill_total * tip_percent
        #final_bill_total = bill_total + tip_amount
        #per_person_amount = final_bill_total / number_people
        print("Tip amount: $" + (tip_amount(.20))
        print("Total amount: $" + (final_bill_total)
        print("Amount per person: $" + (per_person_amount)
    elif service_level == "fair":
        tip_percent = .15
        tip_amount = bill_total * tip_percent
        final_bill_total = bill_total + tip_amount
        per_person_amount = final_bill_total / number_people
        print("Tip amount: $%.2f" % (tip_amount,))
        print("Total amount: $%.2f" % (final_bill_total,))
        print("Amount per person: $%.2f" % (per_person_amount,))
    elif service_level == "bad":
        tip_percent = .10
        tip_amount = bill_total * tip_percent
        final_bill_total = bill_total + tip_amount
        per_person_amount = final_bill_total / number_people
        print("Tip amount: $%.2f" % (tip_amount,))
        print("Total amount: $%.2f" % (final_bill_total,))
        print("Amount per person: $%.2f" % (per_person_amount,))
        
tipcalc(bill_total, service_level, number_people)