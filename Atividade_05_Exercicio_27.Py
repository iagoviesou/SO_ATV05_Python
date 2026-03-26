#Declaração de valores
NV: int = 0
Extensão: float = 0
Duração: int = 0
Velocidade_Média: float = 0

#Inicio
NV = int(input("Digite o número de voltas do circuito:"))
Extensão = float(input("Digite a extensão do circuito:"))
Duração = int(input("Digite a duração em minutos:"))
Extensão = Extensão * NV
Velocidade_Média = ((Extensão/1000)/(Duração/60))
print("A velocidade média é:",round(Velocidade_Média, 2),"km/h")

#Fim