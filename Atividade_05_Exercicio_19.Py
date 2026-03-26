# Declaração de Valores:

vlr01: float = 0
vlr02: float = 0
resultado: float = 0

#inicio

vlr01 = float(input('Insira um valor real='))
vlr02 = float(input('insira outro valor real='))

if vlr01 >= vlr02:
    resultado = vlr01
else:
    resultado = vlr02
print ('o maior número inserido é=',resultado)

#Fim