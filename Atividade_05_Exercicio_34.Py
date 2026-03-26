#Declaração de valores:
X: int = 0

#Inicio
X= int(input("Insira o valor a ser calculado:"))
for i in range (1, 11):
    Tabuada = X*i
    print(X,"X",i,"=",Tabuada)
#Fim
