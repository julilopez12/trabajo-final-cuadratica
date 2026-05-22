matriz = []
mayor = None

for i in range(3):
    fila = []
    
    for j in range(4):
        numero = int(input("Ingrese un numero: "))
        fila.append(numero)
        
        if mayor is None or numero > mayor:
            mayor = numero
    
    matriz.append(fila)

print("El elemento mayor de la matriz es:", mayor)