# Brian Vargas
import time
import math

# burning 4.33 calories per min
# starting min is always 5


print('Calorie Table Program')

again = 'y'
while (again == 'y' or again == 'Y'):
    rmin = input('\nEnter running minutes:')
    if rmin.isalpha():
            print('Error: Selection cannot contain letters')
    elif rmin == '':
        print('Error: Minutes cannot be blank')
    else:
        runmins = int(rmin)

        if runmins <= 5:
            print('Error: Minutes entered must be greater than 5')
        else:
            startmins = 5

            while startmins <= runmins:
                cal = startmins * 4.33
                print('Minutes:', startmins, 'Calories:', cal)
                startmins += 5

    again = input('\nAgain y/n: ')


print('\nProgram Complete')
