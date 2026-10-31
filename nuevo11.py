#Ejercicio 11: Buscar el número 7
Numeros = [3, 9, 4, 7, 2, 8]
Posicion = 0
while True:
    if Posicion == len(Numeros):
        print("El 7 no está en la lista")
        break
    print("Revisando:", Numeros[Posicion])
    if Numeros[Posicion] == 7:
        print("¡Encontré el 7 en la posición", Posicion, "!")
        break
    Posicion = Posicion + 1