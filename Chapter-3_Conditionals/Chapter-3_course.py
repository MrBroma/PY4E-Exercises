#Boolean expressions
5 == 5 #True
5 == 6 #False

type(True)
type(False)

x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y
x is y               # x is the same as y
x is not y           # x is not the same as y

#Logical operators
17 and True
#True

#Conditional execution
if x > 0 :
    print("x is positive")

if x < 0 :
    pass          # need to handle negative values!

x = 3
if x < 10:
    print('Small')
#--> Small

x = 3
if x < 10:
    print('Small')
    print('Done')
#File "<stdin>", line 3
#    print('Done')
#        ^
#SyntaxError: invalid syntax

#Alternative execution
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')

#Chained conditionals
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

#Nested conditionals
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

if 0 < x and x < 10:
    print('x is a positive single-digit number.')

