# Write a program that takes two integers as input and returns the larger number.

int_1 = int(input("Enter the first integer: "))
int_2 = int(input("Enter the second integer: "))

if int_1>int_2:
    print(f"The largest integer is {int_1}")
elif int_1 == int_2:
    print(f"The both integers are equal")
else: 
    print(f"The largest integer is {int_2}")