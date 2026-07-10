print("\n======= SISTEMA DE BIENESTAR UNIVERSITARIO =======")
print("1. Atención médica")
print("2. Apoyo psicológico")
print("3. Solicitud de beca")
print("4. Consumo alimentario")
print("5. Salir")

opcion = int(input("Seleccione una opción: "))

# opcion 1 atencion medica

match opcion:
    case 1:
        print("\n--- ATENCIÓN MÉDICA ---")

        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre == "":
            print("Error: debe ingresar un nombre.")
        else:

            edad = int(input("Ingrese la edad del estudiante: "))

            if edad <= 0:
                print("Error: la edad debe ser mayor a 0.")
            else:
                tipo_atencion = input(
                    "Ingrese el tipo de atención (Medicina General / Fisioterapia / Nutrición): ").lower()

                if tipo_atencion == "medicina general":
                    resultado = "Puede ser atendido en medicina general."

                elif tipo_atencion == "fisioterapia":
                    derivacion = input(
                        "¿Tiene derivación médica? (si/no): ").lower()

                    if derivacion == "si":
                        resultado = "Puede agendar cita de fisioterapia."
                    elif derivacion == "no":
                        resultado = "Primero debe pasar por medicina general."
                    else:
                        resultado = "Respuesta no válida en derivación médica."

                elif tipo_atencion == "nutrición" or tipo_atencion == "nutricion":
                    tipo_solicitud = input(
                        "¿Tiene recomendación médica o solicitud personal? ").lower()

                    if tipo_solicitud == "recomendación médica" or tipo_solicitud == "recomendacion medica":
                        resultado = "Atención prioritaria."

                    elif tipo_solicitud == "solicitud personal":
                        resultado = "Atención normal."
                    else:
                        resultado = "Tipo de solicitud no válido."

                else:
                    resultado = "Tipo de atención no válido."

                print("\n=== RESULTADO DE ATENCIÓN MÉDICA ===")
                print("Estudiante:", nombre)
                print("Edad:", edad)
                print("Resultado:", resultado)

    # opcion 2 de ayuda psicologica
    case 2:
        print("\n=== APOYO PSICOLÓGICO ===")

        nombre = input("Ingrese el nombre del estudiante: ")
        motivo = input("Ingrese el motivo de consulta: ")

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
        elif motivo == "":
            print("Error: el motivo de consulta no puede estar vacío.")
        else:
            urgencia = input(
                "Ingrese el nivel de urgencia (Bajo / Medio / Alto): ").lower()

            if urgencia == "bajo":
                atencion = "Agendar cita regular"
            elif urgencia == "medio":
                atencion = "Agendar cita prioritaria"
            elif urgencia == "alto":
                atencion = "Derivar a atención inmediata"
            else:
                atencion = "Nivel de urgencia no válido"

            print("\n=== RESULTADO DE APOYO PSICOLÓGICO ===")
            print("Estudiante:", nombre)
            print("Motivo:", motivo)
            print("Atención asignada:", atencion)

    # opcion 3 de solicitud de beca

    case 3:
        print("\n=== SOLICITUD DE BECA ===")

        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
        else:

            promedio = float(input("Ingrese el promedio académico: "))

            if promedio < 0 or promedio > 10:
                print("Error: el promedio debe estar entre 0 y 10.")
            else:
                situacion = input(
                    "Ingrese la situación socioeconómica (Alta / Media / Baja): "
                ).lower()

                documentos = input(
                    "¿Tiene documentos completos? (si/no): ").lower()

                if documentos == "si":
                    if promedio >= 9 and situacion == "baja":
                        estado = "Candidato prioritario para beca."
                    elif promedio >= 8 and (situacion == "media" or situacion == "baja"):
                        estado = "Candidato elegible para revisión."
                    elif promedio < 8:
                        estado = "No cumple el promedio mínimo sugerido."
                    else:
                        estado = "No cumple con los criterios para beca."

                elif documentos == "no":
                    estado = "Tiene que completar la documentación."

                else:
                    estado = "Su respuesta no es válida."

                print("\n=== RESULTADO DE LA SOLICITUD DE BECA ===")
                print("Estudiante:", nombre)
                print("Promedio académico:", promedio)
                print("Estado:", estado)

    # opcion 4 de consumo alimentario

    case 4:
        print("\n=== CONSUMO ALIMENTARIO ===")

        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
        else:
            tipo_beneficiario = input(
                "Ingrese el tipo de beneficiario (Becado / Funcionario / Invitado): ").lower()

            saldo = float(input("Ingrese el saldo disponible: "))

            if saldo < 0:
                print("Error: el saldo no puede ser negativo.")
            else:
                if tipo_beneficiario == "becado":
                    if saldo > 0:
                        resultado = "Puede registrar consumo."
                    else:
                        resultado = "No cuenta con saldo disponible."

                elif tipo_beneficiario == "funcionario":
                    if saldo > 0:
                        resultado = "Puede consumir con cargo a su saldo."
                    else:
                        resultado = "Debe realizar pago directo."

                elif tipo_beneficiario == "invitado":
                    resultado = "Debe realizar pago directo."

                else:
                    resultado = "Tipo de beneficiario no válido."

                print("\n=== RESULTADO DE CONSUMO ALIMENTARIO ===")
                print("Beneficiario:", nombre)
                print("Tipo:", tipo_beneficiario)
                print("Saldo disponible:", saldo)
                print("Resultado:", resultado)

    case 5:
        print("\nGracias por usar el Sistema de Bienestar Universitario.")

    case _:
        print("\nOpción no válida. Intente nuevamente.")
