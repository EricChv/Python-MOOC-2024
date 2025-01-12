# Write your solution here
weekly_consumption = int(input("How many times a week do you eat at the student cafeteria?" ))
lunch_expenditure = float(input("The price of a typical student lunch? "))
groceries_expenditure = float(input("How much money do you spend on groceries in a week? "))

weekly = (lunch_expenditure * weekly_consumption) + (groceries_expenditure)
daily = weekly / 7

print("\nAverage food expediture:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")