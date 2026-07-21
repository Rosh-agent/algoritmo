# caculadora de parqueo y registro del mismo

def tabla():
    print("\n===== Parquedero Vehicular =====")
    print("1.Ingreso Vehiculo")
    print("2.Resumen de registro")
    print("3.salir")


def op():
    while True:
        opcion = input("\ningrese su Opción: ")

        if opcion == "":
            print("Error: Valores Vacios.")

        elif opcion.isdigit() == False:
            print("Error: Los valores deben ser numericos.")

        elif int(opcion) < 1 or int(opcion) > 3:
            print("Error: Opciones 1 al 3.")

        else:
            return int(opcion)


def registro_placa():
    while True:
        placa = input("Ingrese placa: ").upper().strip().replace(" ", "")

        if placa == "":
            print("Error: Datos de Placa Vacia.")

        elif len(placa) != 8:
            print("Error: La placa debe tener 8 carácteres \nEjemplo: AAA-0000")

        elif placa[:3].isalpha() == False:
            print("Error: 3 primeros carácteres deben ser Letras ")

        elif placa[3] != "-":
            print("Error: Despues de la letras debe ir el guion.")

        elif placa[4:].isdigit() == False:
            print("Error: 4 utlimos carácteres deben ser númericos ")

        else:
            return placa


def registro_propietario():
    while True:
        nombres = input("Ingresa Nombres y Apellidos: ").strip()
        p_nombres = nombres.split()

        if nombres == "":
            print("Error: Datos Vacios: ")

        elif len(p_nombres) < 2:
            print("Error: Ingrese al menos un nombre y apellido")

        elif nombres.replace(" ", "").isalpha() == False:
            print("Error: No debe contener numeros.")

        else:
            return nombres.title()


def ingreso_horas():
    while True:
        try:
            horas = float(input("Ingrese Horas del Vehiculo: "))

            if horas <= 0:
                print("Error: Valores no beben ser cero")
            else:
                return horas
        except ValueError:
            print("Error: Debe ingresar valores numericos.")


def calculo_horas(horas):
    tarifa = 1.50
    total_tarifa = tarifa * horas
    return total_tarifa


def estancia(horas):
    if horas < 2:
        return "Estancia Corta"
    elif horas <= 4:
        return "Estancia Media"
    else:
        return "Estancia Larga"


def resumen(vehiculo_total, recaudado, est_larga, est_media, est_corta):

    print("\n=== Resumen ===")
    print("Vehiculos Registrados", vehiculo_total)
    print(f"Total Recaudado: ${recaudado:.2f}")
    print("Estancias largas: ", est_larga)
    print("Estancias Medias: ", est_media)
    print("Estancias cortas: ", est_corta)

    if vehiculo_total > 0:
        promedio = recaudado / vehiculo_total
        print(f"Promedio recaudado por vehículo: ${promedio:.2f}")
    else:
        print("Promedio recaudado por vehículo: $0.00")


def menu_main():
    vehiculo_total = 0
    recaudado = 0
    est_larga = 0
    est_media = 0
    est_corta = 0
    numero_ticket = 1

    while True:
        tabla()
        opcion_vali = op()

        match opcion_vali:

            case 1:
                print("\n=== Ingrese Datos del Parqueo ===")
                placa_p = registro_placa()
                nombres_p = registro_propietario()
                horas_p = ingreso_horas()

                valor_p = calculo_horas(horas_p)
                estancia_p = estancia(horas_p)

                vehiculo_total += 1
                recaudado += valor_p

                if estancia_p == "Estancia Corta":
                    est_corta += 1

                elif estancia_p == "Estancia Media":
                    est_media += 1

                else:
                    est_larga += 1

                ticket = f"TKT{numero_ticket:03d}"
                numero_ticket += 1

                print("\n======= Datos Vehicular =======")
                print("Ticket:", ticket)
                print("Placa del Vehicualo: ", placa_p)
                print("Propietario del Vehiculo: ", nombres_p)
                print("Horas Parqueadero Vehiculo: ", horas_p, " horas")
                print("Tipo de Estacia Registras es: ", estancia_p)
                print(f"Recuerde: Tarifa por Horas es de: $1.50")
                print(f"Su valor total a pagar es: $ {valor_p:.2f}")

            case 2:
                resumen(vehiculo_total, recaudado,
                        est_larga, est_media, est_corta)

            case 3:
                print("Gracias por usar el Sistema")
                break


menu_main()
