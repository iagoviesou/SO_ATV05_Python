#Declaração de valores
d1: int = 1
d2: int = 0

#Inicio

print("As possibilidades para cada dado são respectivamente: ")

while d1 <= 6:
    d2 = 1
    while d2 <= 6:
        if d1 + d2 == 7:
            print(d1,d2)
        d2 = d2 +1
    d1 = d1 +1