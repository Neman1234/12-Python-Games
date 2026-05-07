import random
random_number = random.randint(1, 10)

Users_Guess = int(input('Guess a number between 1 and 10 '))



if Users_Guess == random_number:
    print('Congratulations! You Got the number correct!')
else: print('Sorry, you got the number wrong. The correct number was ' + str(random_number))