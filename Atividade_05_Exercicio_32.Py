#Declaração de valores:
X: int = 0
Fatorial: int = 1

#Inicio
X = int(input("Digite um valor inteiro:"))
if X < 0:
    print("O valor não possui fatorial")
else:
    for i in range (1,X+1):
        Fatorial = Fatorial * i
    print("Fatorial:", Fatorial)
#Fim