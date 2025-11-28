def pedir_numero():
    return int(input("Digite un número del 1 al 12: "))

def mostrar_mes(num):
    match num:
        case 1:
            print("Enero")
        case 2:
            print("Febrero")
        case 3:
            print("Marzo")
        case 4:
            print("Abril")
        case 5:
            print("Mayo")
        case 6:
            print("Junio")
        case 7:
            print("Julio")
        case 8:
            print("Agosto")
        case 9:
            print("Septiembre")
        case 10:
            print("Octubre")
        case 11:
            print("Noviembre")
        case 12:
            print("Diciembre")
        case _:
            print("Número fuera del rango (1 al 12)")

def main():
    num = pedir_numero()
    mostrar_mes(num)

# Programa principal
main()
