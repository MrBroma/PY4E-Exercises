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

#