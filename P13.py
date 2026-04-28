#P13 Roman Numeral Translator
# Brian Vargas
def main():
    # set up dictionary
    dt01 = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
        11: 'XI',12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII', 18: 'XVIII',
        19: 'XIX', 20: 'XX', 21: 'XXI', 22: 'XXII', 23: 'XXIII', 24: 'XXIV',}
    
    ans = 'y'
    
    print('Dictionary Example:', dt01)

    while (ans.lower() == 'y'):
        try: 
            num = int(input('\nEnter a number: '))
        
            if num <= 0:
                print('\nERROR: Number cannot be zero or negative.')
                break

            if num in dt01:
                print('\nThe Roman numeral for', num, 'is', dt01[num])
            else:
                add = input('\nNumber not found. Do you want to add it to the dictionary? (y/n): ')
                            
                if add.lower() == 'y':
                    roman = input('\nEnter the Roman numeral: ')
                    
                    if roman.isalpha():
                        dt01[num] = roman
                        print('\nAdded to dictionary')
                    else:
                        print('\nError: Roman numeral must be alphabetic.')

            ans = input('\nAgain? (y/n): ')

        except ValueError:
            print('Error: Please enter a valid integer.')

    print('\nUpdated Dictionary:', dt01)
main()
