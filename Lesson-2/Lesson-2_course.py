# Variables, expressions, and statements

# Values and types
print(4)

type('Hello, World!')
type(17)
type(3.2)

# What about values like “17” and “3.2”? They look like numbers, but they are in quotation marks like strings.

type('17')
type('3.2')

# Variables
message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931

print(n)
print(pi)

# The type of a variable is the type of the value it refers to.

type(message)
type(n)
type(pi)

# Variable names and keywords

# >>> 76trombones = 'big parade'
# SyntaxError: invalid syntax
# >>> more@ = 1000000
# SyntaxError: invalid syntax
# >>> class = 'Advanced Theoretical Zymurgy'
# SyntaxError: invalid syntax

# Statements
print(1)
x = 2
print(x)

# Operators and operands
# The operators +, -, *, /, and ** perform addition, subtraction, multiplication, division, and exponentiation,
# as in the following examples:

# 20+32
# hour-1
# hour*60+minute
# minute/60
# 5**2
# (5+9)*(15-7)

# Expressions
# An expression is a combination of values, variables, and operators.
# A value all by itself is considered an expression, and so is a variable,
# so the following are all legal expressions (assuming that
# the variable x has been assigned a value):

# Order or operations
# When more than one operator appears in an expression, the order of evaluation depends on the rules of precedence.
# For mathematical operators, Python follows mathematical convention.
# The acronym PEMDAS is a useful way to remember the rules:

# Modulus operator
quotient = 7 // 3
print(quotient)

remainder = 7 % 3
print(remainder)

## String operations
# The + operator works with strings, but it is not addition in the mathematical sense. Instead it performs concatenation, which means joining the strings by linking them end to end. For example:
first = 10
second = 15
print(first+second)

first = '100'
second = '150'
print(first + second)

# The * operator also works with strings by multiplying the content of a string by an integer. For example:
first = 'Test '
second = 3
print(first * second)

# Asking the user for input
np = input()
print(inp)

name = input('What is your name?\n')
print(name)

prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)
int(speed)
int(speed) + 5

# But if the user types something other than a string of digits, you get an error:

speed = input(prompt)
# What...is the airspeed velocity of an unladen swallow?
# What do you mean, an African or a European swallow?
int(speed)
# --> ValueError: invalid literal for int() with base 10:

# ==> Choosing mnemonic variable names

# Debugging

