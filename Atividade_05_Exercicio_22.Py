#Declaração de valores
vlr01: int = 0
vlr02: int = 0

#Inicio
vlr01 = int(input("Digite um valor inteiro:"))
vlr02 = int(input("Digite um valor inteiro:"))
if vlr01 == vlr02:
    print ("O valores são iguais")
elif vlr01 < vlr02:
    print ("Valores em ordem crescente:",vlr01,vlr02)
else:
    print ("Valores em ordem crescente:",vlr02,vlr01)

#Fim