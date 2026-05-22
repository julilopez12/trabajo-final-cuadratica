matriz =[]
for i in range(3):
    fila = []
    for j in range(3):
        numero =int(input("ingrese numero: "))
        fila.append(numero)
        matriz.append(fila)
        print("matriz:")
        for fila in matriz:
            print(fila)
