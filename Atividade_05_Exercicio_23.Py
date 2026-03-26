#Declaração de valores
Vlr01: float = 0
Vlr02: float = 0
Vlr03: float = 0
Vlr04: float = 0

#Inicio
Vlr01 = float(input("Digite o primeiro valor:"))
Vlr02 = float(input("Digite o segundo valor:"))
Vlr03 = float(input("Digite o terceiro valor:"))
Vlr04 = float(input("Digite o quarto valor:"))

if Vlr04 <= Vlr01:
    print(Vlr04,Vlr01,Vlr02,Vlr03)
elif Vlr04 <= Vlr02:
    print(Vlr01,Vlr04,Vlr02,Vlr03)
elif Vlr04 <= Vlr03:
    print(Vlr01,Vlr02,Vlr04,Vlr03)
else:
    print(Vlr01,Vlr02,Vlr03,Vlr04)

#Fim