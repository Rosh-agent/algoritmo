def estudiante():
    while True:
        nombre = input(
            "Ingrese Nombre de Estudiante: ").strip()
        if nombre == "":
            print("Error: Nombres no puden estar vacios.")
        elif nombre.replace(" ", "").isalpha() == False:
            print("Error: Nombres de no debe tener digitos")

        else:
            # print("Ingrese  un Nombre Valido")
            return nombre


def cedula_identidad():
    while True:
        cedula = input(
            "Ingrese cedula de identidad: ").strip().replace(" ", "")
        if cedula == "":
            print("Erro: Cedula no debe estar vacía.")
        elif cedula.isdigit() and len(cedula) == 10:
            return cedula
        else:
            print("Error: Cedula solo debe contener numeros y 10 digitos")


def codigo_block():
    while True:
        codigo = input(" Ingrese codigo Estudiantil").strip().replace(
            " ", "").upper()
        if codigo.startswith("EST") and len(codigo) == 6 and codigo.isalnum():
            return codigo
        else:
            print("Ingrese Codigo Estudiantil correcto DE incio EST")


def correo_valido():
    while True:
        correo = input(
            "Ingrese su correo electronico institucional: ").strip().replace(" ", "").lower()
        if correo.find("live") != -1 and correo.count("@") == 1 and correo.endswith(".uleam.edu.ec"):
            return correo
        else:
            print("Ingrese un correo valido Ejemplo juanito@live.uleam.edu.ec")


nombre = estudiante()
identidad = cedula_identidad()
est_codigo = codigo_block()
mail = correo_valido()


print("====== Datos del estudiante =======")
print(" Nombre: ", nombre.title())
print("Cedula: ", identidad)
print("Correo Valido: ", mail)
print("Codigo Estudiantil :", est_codigo)
