#Ejercicio 10: Contador de vocales
Frase = input("Ingrese una frase: ").lower()
Vocales = 0
Posicion = 0
while True:
    if Posicion == len(Frase):
        break
    Letra = Frase[Posicion]
    if Letra == "a" or Letra == "e" or Letra == "i" or Letra == "o" or Letra == "u":
        Vocales = Vocales + 1
    elif Letra == "á" or Letra == "é" or Letra == "í" or Letra == "ó" or Letra == "ú":
        Vocales = Vocales + 1
    Posicion = Posicion + 1
print("La frase tiene", Vocales, "vocales")