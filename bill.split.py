print("Welcome to the tip calculator!!!")
bill = float(input("what was the total bill ?$ "))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15 ? "))
people = int(input("how many people to split the bill ? "))
bill_with_tip = bill * (1 + tip /100)
bill_per_person = bill_with_tip / people

print(f"Each person should pay: {bill_per_person}")
