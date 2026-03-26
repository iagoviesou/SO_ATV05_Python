#Declaração de valores:
Ana: float = 1.10
Maria: float = 1.50
anac: float = 0.03
Mariac: float = 0.02
Contador: int = 0

#Inicio

while Maria >= Ana:
    Maria = Maria + Mariac
    Ana = Ana + anac
    Contador = Contador + 1
print("Levará ", Contador," anos até que Ana seja maior que Maria")

#Fim