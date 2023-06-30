# Tip Calculator, use it the split the bills accurately

print("Welcome to the Tip Calculator!!")
Bill = float(input("Total Bill: Rs "))
percentage = int(input("Percentage of Tip(10, 12 or 15): "))
no_of_people = int(input("How many people are splitting the bill? "))

Total = Bill + (percentage / 100) * Bill
Split_bill = round(Total / no_of_people, 2)
# Split_bill = float("{:.2f}".format(Total/no_of_people))
print(f"Each Person should pay: Rs {Split_bill}")
