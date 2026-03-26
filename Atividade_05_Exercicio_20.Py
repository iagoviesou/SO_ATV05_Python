#Declaração de valores

A: int = 0
B: int = 0
C: int = 0
Delta: int = 0
X1: int = 0
X2: int = 0

#inicio

import math
A = int(input("Insira o valor de A="))
B = int(input("Insira o valor de B="))
C = int(input("Insira o valor de C="))

if A == 0:
    print ("Não é uma equação de 2º grau;")
else:
    Delta = int((B*B)-4*A*C)
    if Delta < 0:
        print ("Não existem Raizes reais")
    elif Delta == 0:
        X1 = int((-1*B)/(2*A))
        print ("Existe uma raiz real: ","X=",X1)
    else:
        X1 = int((-1*B+math.sqrt(Delta))/(2*A))
        X2 = int((-1*B-math.sqrt(Delta))/(2*A))
        print ("Raiz X1=",X1,"Raiz X2=",X2)

#Fim