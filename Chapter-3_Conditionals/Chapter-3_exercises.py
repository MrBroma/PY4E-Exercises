# Exercise 1: Rewrite your pay computation to give
# the employee 1.5 times the hourly rate for hours worked above 40 hours.
hr = int(input("Enter hours: "))
rate = float(input("Enter the rate: "))
if hr > 40:
    pay = (40 * rate) + ((hr - 40) * (10.5 * 1.5))
else:
    pay = hr * rate

print(pay)

# Exercise 2: Rewrite your pay program using try and except so
# that your program handles non-numeric input gracefully by printing
# a message and exiting the program. The following shows two executions of the program:
hour2 = input("Enter hours: ")
rate2 = input("Enter the rate: ")
try:
    hr = int(hour2)
    r = float(rate2)
except:
    print("Please enter a numeric number")

if hr > 40:
    pay = (40 * r) + ((hr - 40) * (10.5 * 1.5))
else:
    pay = hr * r

print("Your pay is pay is ", pay)

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score
# is out of range, print an error message. If the score is between 0.0 and 1.0, print
# a grade using the following table:

score = float(input("Enter Score: "))
if score >= 0.9:
    print('TYour score is A')
elif score >= 0.8:
    print('Your score is B')
elif score >= 0.7:
    print('Your score isC')
elif score >= 0.6:
    print('Your score is D')
else:
    print('Your score is F')
