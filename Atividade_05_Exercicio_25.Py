#Declaraçãode valores
HH: int = 0
MM: int = 0
HHf: int = 0
MMf: int = 0

#Inicio
HH = int(input("Digite a hora inicial do jogo:"))
MM = int(input("Digite o minuto inicial do jogo:"))
HHf = int(input("Digite o horário final do jogo:"))
MMf = int(input("Digite o minuto final do Jogo:"))
Inicio = int((HH*60) + MM)
Fim = int((HHf*60) + MMf)

if Fim >= Inicio:
    Duração = int(Fim - Inicio)
else:
    Duração = int((24*60) - Inicio + Fim)

HHd = Duração // 60
MMd = Duração % 60

print("Duração do jogo:",HHd, "horas e ",MMd," minutos")

#Fim