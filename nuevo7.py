#Ejercicio 7: Deletreo de palabra 
Palabra = input("Ingrese una palabra: ")
Posicion = 0
while True:
    if Posicion == len(Palabra):
        break
    print(Palabra[Posicion])
    Posicion = Posicion + 1