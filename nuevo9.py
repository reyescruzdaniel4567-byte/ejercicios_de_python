 #Ejercicio 9: Filtrar aprobados 
Notas = [2.5, 3.0, 4.2, 1.8, 3.5, 5.0, 2.9]
Posicion = 0
while True:
    if Posicion == len(Notas):
        break
    if Notas[Posicion] >= 3.0:
        print("Aprobada:", Notas[Posicion])
    Posicion = Posicion + 1