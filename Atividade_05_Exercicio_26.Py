#Declaração de valores

N1: int = 0
N2: int = 0

#Inicio

N1 = int(input("Digite o primeiro valor:"))
N2 = int(input("Digite o segundo valor:"))
if N1 >= N2:
    if N1%N2 == 0:
        print("O maior número é múltiplo do menor")
    else:
        print("O maior número não é múltiplo do menor")
else:
    if N2%N1 == 0:
        print("O maior número é múltiplo do menor")
    else:
        print("O maior número não é múltiplo do menor")

#Fim