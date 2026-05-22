opcion = 0
saldo = 10000
datos = 500

while opcion != 5:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Ver promociones")
    print("3. Recargar saldo")
    print("4. consumir datos")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
     print("\nSu saldo actual es: $", saldo)
     print("datos disponibles:",datos, "MB")

    elif opcion == 2:
        print("\nPromociones disponibles:")
        print("- 2x1 en recargas")
        print("- 30% de descuento en datos móviles")

    elif opcion == 3:
        monto = int(input("Ingrese monto a recargar: "))
        saldo = saldo + monto
        print("Recarga exitosa. Nuevo saldo: $", saldo)

    elif opcion == 4:
        consumo =int(input("ingrese datos consumidos(MB): "))
        if consumo <= datos:
            datos = datos - consumo
            print("consumo realizado. Datos restantes:", datos, "MB")
        print("\nGracias por comunicarse. ¡Hasta luego!")

    else:
        print("No tiene suficientes datos disponibles")
elif opcion == 5: 