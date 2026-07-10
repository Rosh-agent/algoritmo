print("====Bienvenido a la Calculadora====")

while True:
    # try:
    print("\nSeleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    try:
        opcion = int(input("\nIngrese una opción: "))
        if opcion >= 1 and opcion <= 5:
            while True:
                try:
                    numero1 = float(input("Ingrese el primer número: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número válido.")
            while True:
                try:
                    numero2 = float(input("Ingrese el segundo número: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número válido.")

            match opcion:
                case 1:
                    print("\nEl resultado de la suma es:", numero1 + numero2)
                case 2:
                    print("\nEl resultado de la resta es:",
                          numero1 - numero2)
                case 3:
                    print("\nEl resultado de la multiplicación es:",
                          numero1 * numero2)
                case 4:
                    if numero2 != 0:
                        print("\nEl resultado de la división es:",
                              numero1 / numero2)
                    else:
                        print("\nError: No se puede dividir entre cero.")
                case 5:
                    print("\nSaliendo de la calculadora...")
                case _:
                    print("\nOpción inválida.")

            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")
