empleados_hijos = 0
total_pagado = 0
total_bonificaciones = 0
total_iess = 0

print("\n=========== Empresa Kako S.A. =============")
print("====== Bienvenido Calculadora de sueldo ======")

while True:
    try:
        empleados = int(input("Ingrese la cantidad de empleados: "))
        if empleados == "":
            print("Ingrese un valor")
        elif empleados > 0:
            break
        else:
            print("Error: ingrese un valor positivo y entero")
    except ValueError:
        print("Error: ingrese un valor numerico y entero")
i = 1

while i <= empleados:
    print("\n================================================")

    while True:
        nombres = input("Nombre completo del empleado: ")

        if nombres == "":
            print("Error: no puede dejar el campo vacío")
        elif nombres.replace(" ", "").isalpha() == False:
            print("Error: ingrese un nombre válido")
        else:
            break

    while True:
        try:
            h_trabajado = float(
                input("Ingrese las horas trabajadas en el mes: "))
            if h_trabajado >= 0:
                break
            else:
                print("Error: ingrese horas positivas")
        except ValueError:
            print("Error: ingrese solo números")

    while True:
        try:
            t_hora = float(input("Ingrese la tarifa por hora: "))
            if t_hora >= 0:
                break
            else:
                print("Error: ingrese tarifa positiva")
        except ValueError:
            print("Error: ingrese solo números")

    if h_trabajado > 160:
        h_normal = 160
        h_extras = h_trabajado - 160
    else:
        h_normal = h_trabajado
        h_extras = 0

    salario_normal = h_normal * t_hora
    v_h_extras = h_extras * t_hora * 1.5

    while True:
        t_hijos = input("¿Tiene hijos? (SI/NO): ").upper()

        if t_hijos == "SI" or t_hijos == "NO":
            break
        else:
            print("Error: solo se admiten SI o NO")

    if t_hijos == "SI":
        while True:
            cantidad_hijos = input("Ingrese la cantidad de hijos: ")

            if cantidad_hijos.isdigit() and int(cantidad_hijos) > 0:
                cantidad_hijos = int(cantidad_hijos)
                break
            else:
                print("Error: Solo se admiten valores enteros y positivos")

        bonificacion = cantidad_hijos * 15
        empleados_hijos = empleados_hijos + 1
    else:
        cantidad_hijos = 0
        bonificacion = 0

    salario_bruto = salario_normal + v_h_extras + bonificacion
    descuento_iess = salario_bruto * 0.0945
    salario_neto = salario_bruto - descuento_iess

    print("\n================================================")
    print("...... Detalles del empleado", nombres, "........")
    print("Nombre del empleado:", nombres)
    print("Horas normales trabajadas:", h_normal)
    print("Salario por horas normales: $", round(salario_normal, 2))
    print("Horas extras trabajadas:", h_extras)
    print("Valor horas extras: $", round(v_h_extras, 2))
    print("Bonificación por hijos: $", round(bonificacion, 2))
    print("Salario bruto: $", round(salario_bruto, 2))
    print("Descuento IESS: $", round(descuento_iess, 2))
    print("Salario neto mensual: $", round(salario_neto, 2))

    total_pagado = total_pagado + salario_neto
    total_bonificaciones = total_bonificaciones + bonificacion
    total_iess = total_iess + descuento_iess

    i = i + 1

print("\n===================================================")
print(".............. Resumen Empresa Kako ...............")
print("Cantidad total de empleados procesados:", empleados)
print("Total general pagado por la empresa: $", round(total_pagado, 2))
print("Cantidad de empleados con hijos:", empleados_hijos)
print("Total pagado en bonificaciones: $", round(total_bonificaciones, 2))
print("Total descontado por IESS: $", round(total_iess, 2))
