def pares():
    pass


def impares():
    pass


def mixtos():
    pass


def menu():
    while True:
        print("""
            Menu
        1. Numeros pares
        2. Numeros impares
        3. Numeros mixtos
        4. Salir    
        """)
        opc = int(input("Seleccione una opcion: "))
        if opc == 1:
            pares()
        elif opc == 2:
            impares()
        elif opc == 3:
            mixtos()
        elif opc == 4:
            break
        else:
            print("Digite una opcion correcta")


def main():
    menu()
    print("Programa finalizado")
    pass


if __name__ == "__main__":
    main()