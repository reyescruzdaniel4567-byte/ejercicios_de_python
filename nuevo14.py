#Ejercicio 14: Factorial de 5
Factorial = 1
Numero = 5
while True:
    if Numero <= 1:
        break
    Factorial = Factorial * Numero
    Numero = Numero - 1
print("5! =", Factorial)