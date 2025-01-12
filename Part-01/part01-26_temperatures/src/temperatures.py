# Write your solution here
f_temp = int(input("Please type in a temperature (F): "))

c_temp = (f_temp - 32) / (9/5)
print(f"{f_temp} degrees Fahrenheit equals {c_temp} degrees Celsius")
if c_temp < 0:
    print("Brr! It's cold in here!")