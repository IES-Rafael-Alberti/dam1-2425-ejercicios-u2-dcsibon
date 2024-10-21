"""
Ej 2.3.1 - Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
Extra1: Lanzar excepciones con mensajes específicos si la edad es negativa, igual a 0 o superior a 125 años.
Extra2: Evita mostrar un mensaje en inglés.
"""

def pedir_edad() -> int:
    edad = None
    while edad is None:
        try:
            edad = int(input("Introduce tu edad: "))
            if not (1 <= edad <= 125):
                if edad < 1:
                    raise ValueError("La edad debe ser un número positivo.")
                if edad == 0:
                    raise ValueError("La edad debe ser un número positivo mayor que cero.")
                if edad > 125:
                    raise ValueError("La edad debe ser un número inferior o igual a 125.")
                edad = None
        except ValueError as e:
            if edad is None:
                print(f"*ERROR* El número introducido no es un entero válido. Inténtalo de nuevo.")
            else:
                print(f"*ERROR* {e}. Inténtalo de nuevo.")
    return edad


def mostrar_anios_cumplidos(edad: int):
    for i in range(1, edad + 1):
        print(i)


def main():
    edad = pedir_edad()
    print(f"Has cumplido los siguientes años:")
    mostrar_anios_cumplidos(edad)


if __name__ == "__main__":
    main()
