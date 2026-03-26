#Declaração de valores:
termo: int = 0
resultado: int = 0

#inicio
for i in range (1,16):
    termo = i/(i*i)
    if i % 2 == 0:
        resultado = resultado - termo
    else:
        resultado = resultado + termo
print("O resultado é: ", resultado)
#Fim