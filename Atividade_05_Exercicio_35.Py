#Declaração de valores:
N1: int = 0
N2: int = 0
Impares: int = 0

#inicio
N1= int(input("Digite o primeiro valor:"))
N2= int (input("Digite o segundo valor:"))

if N1 < N2:
    for i in range (N1+1, N2):
        if i%2 != 0:
            Impares = Impares + i
else:
    for i in range (N2+1, N1):
        if i  % 2 != 0:
            Impares = Impares + i
print(Impares)
#Fim