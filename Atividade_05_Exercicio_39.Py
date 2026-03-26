#Declaração de valores:
total: int = 0
graos: int = 1

#Inicio

X = int(input("Digite o número de casas: "))

for casa in range(1, X + 1):
    total = total + graos
    graos = graos * 2

print("Total de grãos:", total)