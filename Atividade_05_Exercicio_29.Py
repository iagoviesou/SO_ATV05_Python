#Declaração de valores:
Investimento: int = 0
Valor: float = 0

#Inicio
Investimento = int(input("Digite o código do tipo de investimento, para Poupança digite 1 e para Renda fixa digite 2:"))
Valor = float(input("Digite o valor do investimento:"))
if Investimento != 1 and Investimento != 2:
    print("Código de investimento divergente")
elif Investimento == 1:
    Valor = Valor * 1.03
    print("O valor corrigido após 30 dias será de R$:",round(Valor,2))
else:
    Valor = Valor * 1.05
    print("O valor corrigido após 30 dias será de R$:",round(Valor,2))
#Fim