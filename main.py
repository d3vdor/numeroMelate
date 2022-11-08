import os
import random
import time


def back_menu():
    time.sleep(10)
    os.system("cls")
    menu()


def no_repetir(a,m):
    aleatorios = random.sample(range(1,56),6)
    for i in aleatorios:
        if i % 2 == a:
            continue
    print(f"Numeros {m}: {aleatorios}")
    back_menu()

def pares():
    no_repetir(0,"Pares")
        

def impares():
    no_repetir(1,"Impares")


def mixtos():
    aleatorios = random.sample(range(1,56),6)
    print(f"Numeros Mixtos: {aleatorios}")


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