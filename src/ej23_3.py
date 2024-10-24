"""
Ej 2.3.3 - Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
Extra: usa el parámetro "end" en "print" para mostrar la cuenta atrás, directamente sin usar una cadena de caracteres, en la función mostrar_cuenta_atras(numero: int)
"""

def pedir_numero_positivo() -> int:
    numero = None
    while numero is None:
        try:
            valor = int(input("Introduce un número entero positivo: "))
            if valor <= 0:
                raise ValueError("El número debe ser positivo.")
            numero = valor
        except ValueError as e:
            print(f"*ERROR* {e}. Inténtalo de nuevo.")
    return numero


def mostrar_cuenta_atras(numero: int):
    primero = True
    for i in range(numero, -1, -1):
        if primero:
            print(i, end="")
            primero = False
        else:
            print(f", {i}", end="")


def main():
    numero = pedir_numero_positivo()
    print(f"Cuenta atrás desde {numero} hasta cero:")
    mostrar_cuenta_atras(numero)


if __name__ == "__main__":
    main()
