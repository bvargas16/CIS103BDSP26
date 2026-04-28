# Brian Vargas P7
import math
def getmiles():
    aa = float(input("Enter the number of miles: "))
    return aa 

def getfahrenheit():
    bb = float(input("Enter the temperature in Fahrenheit: "))
    return bb

def getpounds():
    cc = float(input("Enter the weight in pounds: "))
    return cc

def main():
    miles = getmiles()
    fahrenheit = getfahrenheit()
    pounds = getpounds()

    kilometers = miles * 1.60934
    celsius = (fahrenheit - 32) * 5.0/9.0
    kilograms = pounds * 0.45359237

    print('\n'*2)
    print(miles, "miles is equal to", kilometers, "kilometers.")
    print(fahrenheit, "degrees Fahrenheit is equal to", celsius, "degrees Celsius.")
    print(pounds, "pounds is equal to", kilograms, "kilograms.")

main()
