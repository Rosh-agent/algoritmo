print("\n====== Bienvenido a Registro de Estudiantes ======")

while True:
    nombres = input(
        "Ingrese Nombres y Apellidos Completos del estudiantes: ").strip()
    completo_nombres = nombres.split()

    if nombres == "":
        print("Error: Nombres y apellidos vacios")
    elif nombres.replace(" ", "").isalpha() == False:
        print("El nombre solo debe contener Letras")
    elif len(completo_nombres) < 3:
        print("Error: Debe contener al menos dos nombres y un apellido")
    else:
        break
        # print("Error: Ingrese Valores Correctos  ")

while True:
    cedula = input("ingrese cedula del estudiante: ").strip().replace(" ", "")
    if cedula.isdigit() and len(cedula) == 10:
        break
    else:
        print("Error: Ingrese una cedula numerica y tenga 10 digitos.")

while True:
    correo = input("\nIngrese el correo institucional debe empezar\n"
                   "Con e, contener un @, contener live, y el dominio uleam.edu.ec: ").strip(
    ).lower().replace(" ", "")

    if (
        correo.startswith("e")
        and correo.count("@") == 1
        and correo.find("live") != -1
        and correo.endswith("uleam.edu.ec")
    ):
        break
    else:
        print("Error: correo institucional inválido.")

while True:
    codigo_carrera = input(
        "Ingres el código de carrera, Ejemplo: FCV-SOF-2026: ").strip().upper().replace(" ", "")
    partes_codigo = codigo_carrera.split("-")
    if (
        len(partes_codigo) == 3
        and partes_codigo[0].isalpha()
        and len(partes_codigo[0]) <= 3

        and partes_codigo[1].isalpha()
        and len(partes_codigo[1]) <= 3

        and partes_codigo[2].isdigit()
        and len(partes_codigo[2]) == 4
    ):
        break
    else:
        print("Error: formato correcto ejemplo FCV-SOF-2026.")
print("Codigo de Carrera es: ", partes_codigo)

iniciales = (
    completo_nombres[0][0].upper()
    + completo_nombres[1][0].upper()
    + completo_nombres[2][0].upper()
)

codigo_institucional = iniciales + "-" + \
    cedula[-4:] + "-" + codigo_carrera.replace(" ", "")
codigo_institucional = codigo_institucional.replace(" ", "")

print("\n===== RESUMEN FINAL =====")
print("Nombres Completos del Estudiantes: ", nombres.title())
print("Cedula del Estudiantes: ", cedula)
print("Correo electronico es ", correo)
print("Codigo de la Carrera es: ", codigo_carrera)
print("Codigo institucional: ", codigo_institucional)
