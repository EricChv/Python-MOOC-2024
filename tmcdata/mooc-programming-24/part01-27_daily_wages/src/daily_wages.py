# Write your solution here
Hourly_wage = float(input("Hourly wage: "))
Hours_worked = int(input("Hours worked: "))
Day_of_week = input("Day of the week: ")

if Day_of_week == "Sunday":
    daily_wage = (Hourly_wage * Hours_worked) * 2
else:
    daily_wage = Hourly_wage * Hours_worked

print(f"Daily wages: {daily_wage} euros")



