#Declaração de Valores:

vlr01: int = 0
vlr02: int = 0
resultado: int = 0

#inicio

vlr01 = int(input('Insira um valor inteiro='))
vlr02 = int(input('insira outro valor inteiro='))

if vlr01 >= vlr02:
    resultado = vlr01 - vlr02
else:
    resultado = vlr02 - vlr01
print ('a diferença dos valores é=', resultado)

#Fim