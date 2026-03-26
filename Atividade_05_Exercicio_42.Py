#Declaração de valores
from fractions import Fraction
Sm = Fraction(0,1)
denominador: int = 1

#Inicio

for i in range (1, 51):
    Sm = Sm + Fraction(i, denominador)
    denominador= denominador + 2
print ("O resultado da série é:",Sm)

#Fim