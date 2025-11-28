

def pedir_numero():
    numero = int(input("Ingrese un número: "))
    return numero

def procesar_numero(numero):
    if numero > 0:
        mensaje = "El número es positivo"
    elif numero < 0:
        mensaje = "El número es negativo"
    else:
        mensaje = "El número es neutro"
    return mensaje

def imprimir_numero(mensaje_dato):
    print(mensaje_dato)

# Programa principal
dato_numero = pedir_numero()
mensaje = procesar_numero(dato_numero)
imprimir_numero(mensaje)
