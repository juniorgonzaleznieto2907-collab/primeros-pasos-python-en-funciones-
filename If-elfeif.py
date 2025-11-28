def pedir_numero():
    return int(input("Ingrese un número: "))

def evaluar_numero(num):
    if num == 0:
        print("Fin del programa")
        return False
    elif num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
    return True

def main():
    num = 1
    while num != 0:
        num = pedir_numero()
        if not evaluar_numero(num):
            break

# Programa principal
main()
