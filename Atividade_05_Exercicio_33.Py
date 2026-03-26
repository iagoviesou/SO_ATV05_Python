#Declaração de valores:
from fractions import Fraction
X: int = 0
Aumento = Fraction(0,1)

#Inicio
X = int(input("Digite um valor inteiro:"))
if X <= 0:
    print("Digite um valor maior que 0")
else:
    for i in range (1,X + 1):
        Aumento = Aumento + Fraction(1,i)
print("Resultado:",Aumento)
print(f"Forma decimal:{float(Aumento):.2f}")

#Fim