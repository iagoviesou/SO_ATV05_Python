#Declaração de valores:
N1: int = 0
N2: int = 0
Primos: int = 0
Divisores: int = 0

#inicio

N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
if N1 > N2:
    N1, N2 = N2,N1

print("Os números primos entre eles são: ")

for Primos in range(N1, N2 + 1):
    if Primos >= 2:
        Divisores = 0

        for i in range(2, Primos):
            if Primos % i == 0:
                Divisores = Divisores + 1

        if Divisores == 0:
            print(Primos)