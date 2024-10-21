"""
Ej 2.3.2 - Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
def pedir_numero_positivo() -> int:
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                numero = None
                raise ValueError("El número debe ser positivo.")
        except ValueError as e:
            print(f"*ERROR* {e}. Inténtalo de nuevo.")
    return numero


def obtener_impares(numero: int) -> str:
    impares = ""
    for i in range(1, numero + 1, 2):
        impares += f"{i}, "
    
    return impares[:-2]


def main():
    numero = pedir_numero_positivo()
    print(f"Números impares desde 1 hasta {numero}:")
    print(obtener_impares(numero))


if __name__ == "__main__":
    main()
