def pedir_cantidad():
    return int(input("Digite la cantidad de números que desea sumar: "))

def sumar_numeros(cantidad):
    suma = 0
    for i in range(cantidad):
        numero = int(input(f"Digite el número {i + 1}: "))
        suma += numero
    return suma

def mostrar_resultado(suma):
    print("La suma total es:", suma)

def main():
    cantidad = pedir_cantidad()
    total = sumar_numeros(cantidad)
    mostrar_resultado(total)

# Programa principal
main()

