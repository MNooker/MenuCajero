def cajero():
    saldo = 10000
    menu = (
        "\n--- Menú Cajero ---\n"
        "1. Consultar saldo\n"
        "2. Retirar saldo\n"
        "3. Ingresar saldo\n"
        "4. Salir\n"
    )
    while True:
        opcion = input(menu + "Seleccione una opción: ")
        if opcion == "1":
            print(f"Su saldo actual es: ${saldo}")
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            if monto > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= monto
                print(f"Ha retirado ${monto}. Saldo actual: ${saldo}")
        elif opcion == "3":
            monto = float(input("Ingrese el monto a depositar: "))
            saldo += monto
            print(f"Ha ingresado ${monto}. Saldo actual: ${saldo}")
        elif opcion == "4":
            print("Gracias por usar el cajero. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

cajero()