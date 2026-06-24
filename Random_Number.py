import random
print('Pick a random number between 1 and 3')

Number = (random.randint(1,3))
User_Number = int(input('Enter your number '))

if User_Number == Number:
    print('Correct Number!')
else:
    print('Wrong Number, the correct number was', Number)