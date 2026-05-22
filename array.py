tabla = [ ]
for K in range(10):
    tabla.append([ 0 ]*10)
for i in range (0,10,1):
    for K in range(0,10,1):
        tabla[i ][ K]=i*K
for i in range(0,10,1):
    print(tabla[i ])