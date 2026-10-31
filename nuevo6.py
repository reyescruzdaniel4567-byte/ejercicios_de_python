#Ejercicio 6: Suma acumulada 
Suma = 0
Numero = 1
while True:
    Suma = Suma + Numero
    Numero = Numero + 1
    if Numero > 10:
        print("La suma del 1 al 10 es:", Suma)
        break