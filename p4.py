# Brian Vargas
import math
name = input('Enter name:')
aa = len(name)
if len(name) == 0 or name.isspace():
    nmsg = ('\nName cannot be blank')
elif aa < 3:
    nmsg = ('\nName is too short')
elif name.isnumeric():
    nmsg =('\nName must be alphabetic')
else:
    nmsg = 'valid'

anum = input('\nEnter account number:')
if len(anum) == 0 or anum.isspace():
    amsg = ('\nAccount number cannot be blank')
elif anum.isalpha():
    amsg = ('\nAccount number must be numeric')
elif len(anum) != 9:
    amsg = ('\nAccount number must be 9 digits')
else:
    amsg = 'valid'

pymt = input('\nEnter payment amount:')
cc = len(pymt)
if pymt.isspace():
    pmsg = ('\nPayment cannot be blank')
elif cc == 0:
    pmsg = ('\nPayment cannot be zero')
else:
    pamt = float(pymt)
    if pamt <= 0:
        pmsg = ('\nPayment cannot be negative or zero')
    else:
        pmsg = 'valid'
        
    
print('\nName:', name, nmsg)
print('Account number:', anum, amsg)
print('Payment amount:', pymt, pmsg)
