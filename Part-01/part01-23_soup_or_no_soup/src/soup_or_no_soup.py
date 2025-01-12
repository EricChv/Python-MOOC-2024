# Write your solution here
name = input("Please tell me your name: ")

if name == "Jerry":
    print("Next please!")
else:
    num_portions = int(input("How many portions of soup? "))
    cost = num_portions * 5.90
    print("The total cost is " + str(cost))
    print("Next please!")
