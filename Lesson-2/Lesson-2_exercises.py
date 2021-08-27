# Exercise 1: Type the following statements in the Python interpreter to see what they do:
5
x = 5
x + 1

# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
name = input("What is your name? ")
print("Hello ", name)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = round((hours * rate), 2)
print("Your rate is $", pay)

# Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
print(type(width // 2))
print(type(width / 2.0))
print(type(height / 3))
print(type(1 + 2 * 5))

# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to
# Fahrenheit, and print out the converted temperature.
temp_F = int(input("Enter a temperature in Farhenheit: "))
temp_C = (temp_F - 32) * (5 / 9)
round_temp_C = round(temp_C, 2)
print(temp_F, "fahrenheit degrees is", round_temp_C, "in Celsius degrees")
