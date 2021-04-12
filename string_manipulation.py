my_str = '''Bangladesh is a small country. The population is about 190 million, about 85% of the population is Muslim. 
The 26th March and 16th December are our Independence Day and Victory Day respectively. There are 
eight divisions in Bangladesh.'''

# solution-1:
print(my_str)

# solution-2:
uppercase = my_str.upper()
lowercase = my_str.lower()

print(uppercase)
print(lowercase)

# solution-3:
str_line = 'Bangladesh is a small country'
str_list = str_line.split()
print(str_list)

# solution-4:
new_str = my_str.lower().replace('a', 'w')
print(new_str)

# in solution-4, lower method was applied to make the whole paragraph lowercase so that it's easy to replace all the 'a' with 'w', whether it's uppercase 'A' or lowercase 'a'
