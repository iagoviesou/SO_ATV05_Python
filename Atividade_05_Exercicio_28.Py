#Declaração de valores
Mensal: int = 0
Atual: float = 0
Novo: float = 0

#Inicio
Mensal= int(input("Insira a média mensal do produto:"))
Atual= float(input("Insira o valor atual do produto:"))
if Mensal < 500 and Atual < 30:
    Novo = Atual * 1.1
elif Mensal >= 500 and Mensal < 1000 and Atual >=30 and Atual < 80:
    Novo = Atual * 1.15
elif Mensal >= 1000 and Atual >= 80:
    Novo = Atual * 0.95
else:
    Novo = Atual
print("O novo valor é de:",round(Novo,2),"R$")

#Fim