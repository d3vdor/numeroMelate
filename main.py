import os
import random
import time


def back_menu():
    time.sleep(10)
    os.system("cls")
    menu()


def par_impar(n,c):
    i = 1
    while i <= 6:
        numero_random = random.randint(1,56)
        if numero_random % 2 == c:
            no_repeat = numero_random
            if numero_random == no_repeat:
                pass
            print(f"{i}. Numero {n} --> {numero_random}")
        else:
            continue
        i += 1
    back_menu()


def no_repetir(a):
    b = random.randint(1,56)
    if a != b:
        return a
    else:
        pass


def pares():
    par_impar("par",0)

def impares():
    par_impar("impar",1)


def mixtos():
    i = 1
    while i <= 6:
        numero_random = random.randint(1,56)
        print(f"Numero {i} --> {numero_random}")
        no_repetir(numero_random)
        i += 1
    back_menu()


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
            if 4 == 4:
                break
        else:
            print("Digite una opcion correcta")


def main():
    menu()
    print("Programa finalizado")
    pass


if __name__ == "__main__":
    main()