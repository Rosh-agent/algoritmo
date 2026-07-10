n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 == n2 and n1 == n3:
    print("Los tres números son iguales.")

elif n1 == n2 or n1 == n3 or n2 == n3:
    print("Hay dos números iguales.")

elif n1 >= n2 and n2 >= n3:
    print(n1, "Mayor")
    print(n2, "Mediano")
    print(n3, "Menor")

elif n1 >= n3 and n3 >= n2:
    print(n1, "Mayor")
    print(n3, "Mediano")
    print(n2, "Menor")

elif n2 >= n1 and n1 >= n3:
    print(n2, "Mayor")
    print(n1, "Mediano")
    print(n3, "Menor")

elif n2 >= n3 and n3 >= n1:
    print(n2, "Mayor")
    print(n3, "Mediano")
    print(n1, "Menor")

elif n3 >= n1 and n1 >= n2:
    print(n3, "Mayor")
    print(n1, "Mediano")
    print(n2, "Menor")

else:
    print(n3, "Mayor")
    print(n2, "Mediano")
    print(n1, "Menor")
