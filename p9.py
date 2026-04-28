# Brian Vargas
import math
print ('Conversion Program')

def getacres():
    aa = float(input('\nEnter the number of acres: '))
    if aa <= 0:
        print('ERROR: Acres must be greater than zero.')
        
    return aa
    
def getquarts():
    bb = float(input('\nEnter the number of quarts: '))
    if bb <= 0:
        print('ERROR: Quarts must be greater than zero.')
        
    return bb
    
def getfahrenheit():
    cc = float(input('\nEnter the number of degrees Fahrenheit: '))
    return cc

def main():
    try:
        acres = getacres()
        hectares = acres * 0.4047
        print(acres, 'converts to', hectares, 'hectares')
    except:
        print('ERROR: Invalid input. Please enter a number.')

    print('-----------------------------')
    
    try:
        quarts = getquarts()
        liters = quarts * 0.946353
        print(quarts, 'converts to', liters, 'liters')
    except:
        print('ERROR: Invalid input. Please enter a number.')   

    print('-----------------------------')

    try:
        fahrenheit = getfahrenheit()
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(fahrenheit, 'converts to', kelvin, 'kelvin')
    except:
        print('ERROR: Invalid input. Please enter a number.')

again = 'y'
while again == 'y' or again == 'Y':
    main()
    again = input('\nAgain? (y/n): ')

print('\nDone')
