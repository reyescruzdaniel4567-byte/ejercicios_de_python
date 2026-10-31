#Ejercicio 12: Omitir cero
Valores = [4, 0, 7, 0, 0, 2, 9, 0]
Posicion = 0
while True:
    if Posicion == len(Valores):
        break
    Valor = Valores[Posicion]
    Posicion = Posicion + 1  
    if Valor == 0:
    print(Valor)
 