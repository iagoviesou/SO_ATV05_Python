#Declaração de valores:
Contador: int = 0
X: int = 0
Menor: int = 0
Maior: int = 0

#Inicio
while Contador < 100:
    X=int(input("Insira um valor inteiro positivo:"))
    if X <= 0:
        print("O valor inserido é invalido")
    else:
        if Contador == 0:
            Menor = X
            Maior = X
        else:
            if X < Menor:
                Menor = X
            if X > Maior:
                Maior = X
        Contador=Contador+1
print("O número maior é:",Maior," O número menor é:", Menor)
#Fim