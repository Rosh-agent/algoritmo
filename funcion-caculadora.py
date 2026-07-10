def tabla_menu():
    print("\n ===== Calculadora Basica =====")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")
    print("5.Salir")


def option():
    while True:
        op = input("Seleccione una opción del 1 al 5: ").strip()

        if op == "":
            print("Error: La opción no puede estar vacía.")

        elif op.isdigit() == False:
            print("Error: La opción debe ser numérica.")

        elif int(op) < 1 or int(op) > 5:
            print("Error: La opción debe estar entre 1 y 5.")

        else:
            return int(op)


def ingreso(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero

        except ValueError:
            print("Error: Debe ingresar un valor numérico.")


def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 == 0:
        return None
    else:
        return num1 / num2


def operacion(opcion, numero1, numero2):
    match opcion:
        case 1:
            resultado = sumar(numero1, numero2)
            print("Resultado de la suma:", resultado)

        case 2:
            resultado = restar(numero1, numero2)
            print("Resultado de la resta:", resultado)

        case 3:
            resultado = multiplicar(numero1, numero2)
            print("Resultado de la multiplicación:", resultado)

        case 4:
            resultado = dividir(numero1, numero2)

            if resultado == None:
                print("Error: No se puede realizar una división para cero.")
            else:
                print("Resultado de la división:", resultado)


def main_menu():
    while True:
        tabla_menu()
        option_vali = option()

        if option_vali == 5:
            print("\nGracias por utilizar la calculadora.")
            break

        num1 = ingreso("Ingrese el primer número: ")
        num2 = ingreso("Ingrese el segundo número: ")

        operacion(option_vali, num1, num2)


main_menu()
