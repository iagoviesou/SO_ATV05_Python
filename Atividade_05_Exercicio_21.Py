#Declaração de valores
Nota01: float = 0
Nota02: float = 0
Nota03: float = 0
Nota04: float = 0
Média: float = 0

#Inicio
Nota01 = float(input("Digite a nota do primeiro bimestre:"))
Nota02 = float(input("Digite a nota do segundo bimestre:"))
Nota03 = float(input("Digite a nota do terceiro bimestre:"))
Nota04 = float(input("Digite a nota do quarto bimestre:"))
Média = ((Nota01+Nota02+Nota03+Nota04)/4)
if Média >= 6:
    print ("APROVADO")
elif Média >= 3:
    print ("EXAME")
else:
    print ("RETIDO")
print ("A média do aluno é:",Média)

#Fim