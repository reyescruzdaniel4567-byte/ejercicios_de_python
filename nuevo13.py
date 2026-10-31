#Ejercicio 13: Pares e impares 
Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Pares = 0
Impares = 0
Posicion = 0
while True:
    if Posicion == len(Lista):
        break
    if Lista[Posicion] % 2 == 0:
        Pares = Pares + 1
    else:
        Impares = Impares + 1
    Posicion = Posicion + 1
print("Pares:", Pares)
print("Impares:", Impares)