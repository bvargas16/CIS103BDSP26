# Brian Vargas P17 Random
import random

powerball = '1'
megamillions = '2'
lucky_day_lottos = '3'
lotto = '4'

def main():
    print("Welcome to the Illinois Lottery random number generator!")
    print("Please select a game:")
    print("\n1. Powerball")
    print("2. Mega Millions")
    print("3. Lucky Day Lotto")
    print("4. Lotto")
    game = input("\nEnter the number corresponding to your game: ")
    
    if game == powerball:
        numbers = random.sample(range(1, 70), 5)
        numbers.sort()
        print("\nYour Powerball numbers are: ", numbers)
        
    elif game == megamillions:
        numbers = random.sample(range(1, 71), 5)
        numbers.sort()
        print("\nYour Mega Millions numbers are: ", numbers,)
        
    elif game == lucky_day_lottos:
        numbers = random.sample(range(1, 46), 5)
        numbers.sort()
        print("\nYour Lucky Day Lotto numbers are: ", numbers)
        
    elif game == lotto:
        numbers = random.sample(range(1, 53), 6)
        numbers.sort()
        print("\nYour Lotto numbers are: ", numbers)
        
    else:
        print("\nInvalid selection. Please try again.")
    
    ans = input("\nDo you want to generate another set of numbers? (y/n): ")
    if ans.lower() == 'y':
        print('-'*50)
        main()
    elif ans.lower() == 'n':
        print("\nThank you for using the Illinois Lottery random number generator!")
    else:
        print("\nInvalid input. Please try again.")
        print('-'*50)
        main()
main()
