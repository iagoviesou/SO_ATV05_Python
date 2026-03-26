#Declaração de valores:
X: int = 0 #X
Y: int = 1 #B
Fibonacci: int = 0 #A
Proximo_Num: int = 0 #Proximo
Contador: int = 0

#Inicio
X = int(input("Digite a quantidade de números desejados:"))
while Contador < X:
    print (Fibonacci)
    Proximo_Num = Fibonacci + Y
    Fibonacci = Y
    Y = Proximo_Num
    Contador = Contador+1
#Fim