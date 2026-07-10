txt = input("Ingrese su texto: ").strip().lower()
txt = txt.replace(" ", "")

if txt == "":
    print("Error: ingrese un texto valido")
elif txt == txt[::-1]:
    print("El texto ingresado es un palíndromo")
else:
    print("El texto no es un palíndromo")
