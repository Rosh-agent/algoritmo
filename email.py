correo = input("\nIngrese su correo electrónico: ").lower().strip()

while "@" not in correo:
    print("\nError: el correo debe contener el símbolo '@'.")
    correo = input(
        "\nIngrese nuevamente su correo electrónico: ").lower().strip()
    break
print("\nCorreo registrado:", correo)
