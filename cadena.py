cadena = input("Ingrese una cadena: ")

contador = 0

for letra in cadena:
    if letra.lower() in "aeiou":
        contador = contador + 1

print("La cantidad de vocales es:", contador)