# Write your solution here
num_students = int(input("How many students on the course? "))
desired_size = int(input("Desired group size? "))

if num_students % desired_size == 0:
    formed_groups = num_students // desired_size
else:
    formed_groups = (num_students // desired_size) + 1

print(f"Number of groups formed: {formed_groups}")