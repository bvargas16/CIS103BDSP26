# Brian Vargas
import math
print('\nProgram Start')
print('Table Codes: A = add, S = subtract, M = multiply, D = divide')
    
tcode = input('\nSelect table code: ')
num = input('Enter number for table: ')

print('\nChosen table code:', tcode)
print('Chosen number:', num)

if tcode.isspace() or tcode == '':
    print('Error: Table code cannot be blank.')
elif tcode.isnumeric():
    print('Error: Table code must cannot be a number.')
elif num.isspace() or num == '':
    print('Error: Number cannot be blank.')
elif num.isalpha():
    print('Error: Number cannot contain letters.')
else:
    dnum = float(num)

    for x in range(1, 11):
        if tcode == 'A' or tcode == 'a':
            print(num, '+', x, '=', dnum + x)
        elif tcode == 'S' or tcode == 's':
            print(num, '-', x, '=', dnum - x)
        elif tcode == 'M' or tcode == 'm':
            print(num, '*', x, '=', dnum * x)
        elif tcode == 'D' or tcode == 'd':
            if x == 0:
                print(num, '/', x, '= Error: Division by zero')
            else:
                print(num, '/', x, '=', dnum / x)
        else:
            print('Invalid table code entered.')
            break

print('\nProgram End')
