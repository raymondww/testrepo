import math
import random

flag = True
while flag:
    s = input('\nEnter a number between 0 and 10:\n')
    guess = int(s)

    rand = random.randint(0,10)
    dif = math.fabs(rand - guess)

    print('guess :' + str(guess))
    print('rand :'+str(rand))

    if dif <= 2:
        flag = False
        print('You win!')
    else:
        print('You loose!!')