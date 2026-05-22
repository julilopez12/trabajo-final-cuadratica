matriz = []
suma = 0

for i in range(4):
    fila = []
    
    for j in range(4):
        numero = int(input("Ingrese un numero: "))
        fila.append(numero)
        suma = suma + numero
    
    matriz.append(fila)

print("La suma total es:", suma)