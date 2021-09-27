import random
# Exercise 1: Run the program on your system and see what numbers you get.
# Run the program more than once and see what numbers you get.

# The random function is only one of many functions that handle random numbers.
# The function randint takes the parameters low and high, and returns an integer between low and high (including both).

x = random.randint(5, 10)
print(x)
x = random.randint(5, 10)
print(x)
# To choose an element from a sequence at random, you can use choice:

t = [1, 2, 3]
y = random.choice(t)
print(y)

y = random.choice(t)
print(y)
# The random module also provides functions to generate random values from continuous distributions including Gaussian,
# exponential, gamma, and a few more.

# Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions.
# Run the program and see what error message you get.
# Code: http://www.py4e.com/code3/lyrics.py
'''def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()
'''
# Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the
# definition of repeat_lyrics. What happens when you run this program?


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


repeat_lyrics()

# Exercise 4: What is the purpose of the “def” keyword in Python?

# a) It is slang that means “the following code is really cool”
# b It indicates the start of a function
# c It indicates that the following indented section of code is to be stored for later
# d b and c are both true
# e) None of the above

# Exercise 5: What will the following Python program print out?


def fred():
    print("Zap")


def jane():
    print("ABC")


jane()
fred()
jane()

# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay
# which takes two parameters (hours and rate).
hr = int(input("Enter hours: "))
rate = float(input("Enter the rate: "))
if hr > 40:
    pay = (40 * rate) + ((hr - 40) * (10.5 * 1.5))
else:
    pay = hr * rate

print(pay)

# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes
# a score as its parameter and returns a grade as a string.

score = float(input("Enter Score: "))
if score >= 0.9:
    print('Your score is A')
elif score >= 0.8:
    print('Your score is B')
elif score >= 0.7:
    print('Your score isC')
elif score >= 0.6:
    print('Your score is D')
else:
    print('Your score is F')