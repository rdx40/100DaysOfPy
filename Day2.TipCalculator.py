print("Welcome to the tip calculator.\n")
amt=float(input("What was the total bill?\n"))
tip=int(input("How much percentage tip would you like to give? 10, 12, or 15?\n"))
people=int(input("How many people to split the bill?\n"))   
total=amt+(amt*tip/100)
total_per_person=total/people   
total_per_person_round=round(total_per_person,2)
print("Each person should pay : $",total_per_person_round)


