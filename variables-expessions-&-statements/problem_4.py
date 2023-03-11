# Write a program that converts a temperature from Fahrenheit to Celsius.
# formula c/5 = (f-32)/9 => c = 5(f-32)/9

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = (5*(fahrenheit-32))/9

print(f"The temperature is {round(celsius, 2)} degree celsius") #used built-in function round() to round the digits upto 2 decimal points.