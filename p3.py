# Brian Vargas
import math
price_per_pound = 0.99
pounds = float(input('Enter number of pounds:'))
if pounds <= 0:
    print('\nPounds cannot be zero or negative')
else:
    print('\nUse discount percentage')
if pounds < 10:
    disc_per = 0.0
elif pounds < 100:
    disc_per = 0.10
elif pounds < 1000:
    disc_per =  0.20
elif pounds < 10000:
    disc_per = 0.30
else:
    disc_per = 0.40

gsales = pounds * price_per_pound
damount = gsales * disc_per
famount = gsales - damount

print('\nNumber of pounds:', pounds)
print('Gross sales:', gsales)
print('Discount:', damount)
print('Final Amount:', famount)
