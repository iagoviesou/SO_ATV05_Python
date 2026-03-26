#Declaração de Valores
X: int = 0

#Inicio

X = int(input("Digite um valor inteiro:"))
if X%2 == 0 and X%3 ==0:
    print("O valor é divisível por 2 e 3")
elif X%2 == 0:
    print("O valor é divisível por 2")
elif X%3 == 0:
    print("O valor é divisível por 3")
else:
    print("O valor não é divisível por 2 ou 3")

#Fim