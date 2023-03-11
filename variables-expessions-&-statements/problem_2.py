# Write a program that prompts the user to enter their age and tells them how old they will be in 10 years.

age = input("Enter Your Age (in years): ")
future_age = int(age)+10
message = f"You'll be {future_age} years old after 10 years" #Used string formatting here
# message = "You'll be "+str(future_age)+" years old after 10 years"
print(message)