# Brian Vargas
W = input('Width:')
H = input('Height:')
iW = int(W)
iH = int(H)
Arec = iW * iH
print(iW,'*',iH,'=', Arec)
print('The area of a rectangle is:', Arec)
print('\n'*3)
B = input('Base:')
H = input('Height:')
iB = int(B)
iH = int(H)
Atri = 1/2 * iB * iH
print(1/2,'*', iB,'*', iH, '=', Atri)
print('The area of a triangle is:', Atri)
print('\n'*3)
R = input('Radius:')
iR = int(R)
import math
Acir = math.pi * (iR ** 2)
print(math.pi, '*', iR, '** 2', '=', Acir)
print('The area of a circle is:', Acir)
