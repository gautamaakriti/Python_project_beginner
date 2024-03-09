print ("Welcome to the tip calculator") 
#What was the total bill? $124.56
bill = float(input( "What was the total bill? "))
#What percentage tip would you like to give? 10, 12, or 15? 12
tip = int(input ("What percentage tip would you like to give? 10, 12, or 15? "))
#How many people to split the bill? 7
people = int(input ("How many people to split the bill? "))
#Each person should pay: $19.93
tip_percentage = tip / 100
print(tip_percentage)
total_tip_amount = bill * tip_percentage
print(total_tip_amount)
total_bill = bill + total_tip_amount
print(total_bill)
bill_per_person = total_bill / people 
print(bill_per_person)
total_per_person = round(bill_per_person, 2)

print(f"Each person should pay: {total_per_person}")

