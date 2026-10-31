#Ejercicio 15: Mayor número
Lista = [12, 45, 7, 89, 23, 56]
Mayor = Lista[0]
Posicion = 1
while True:
    if Posicion == len(Lista):
        break
    if Lista[Posicion] > Mayor:
        Mayor = Lista[Posicion]
    Posicion = Posicion + 1
print("El mayor número es:", Mayor)