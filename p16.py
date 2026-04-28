# Brian Vargas P16 Recursion
import sys
sys.setrecursionlimit(5000)
    
def add(n):
    if n < 0:
        print('Error: negative number')
        return 0
    elif n == 0:
        return 0
    else:
        return n + add(n-1)
    
def main():
    ans = 'y'
    while(ans == 'y'):
        try:
            numb = int(input('\nEnter a number: '))
            print('the sum of the numbers from 1 to', numb, 'is', add(numb))
        except ValueError:
            print('Error: Please enter a valid integer.')
        ans = input('\nAgain? (y/n): ')
    print('\n---Program Done---')

main()