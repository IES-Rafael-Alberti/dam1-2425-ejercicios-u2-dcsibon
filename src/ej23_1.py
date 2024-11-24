"""
Ej 2.3.1 - Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

Sencillo: El programa muestra error y finaliza o muestra los años y finaliza.

Extra 1:
    def pedir_edad() -> int:
    def mostrar_anios_cumplidos(edad: int):
Extra2: Lanzar excepciones con mensajes específicos si la edad es negativa, igual a 0 o superior a 125 años.
Extra3: Evita mostrar un mensaje en inglés.
Extra4: Usar también otra función validar_edad(edad: int):
"""

def pedir_edad() -> int:
    edad_correcta = False
    while not edad_correcta:
        try:
            edad = None
            edad = int(input("Introduce tu edad: "))
            if edad < 1:
                raise ValueError("La edad debe ser un número positivo.")
            if edad == 0:
                raise ValueError("La edad debe ser un número positivo mayor que cero.")
            if edad > 125:
                raise ValueError("La edad debe ser un número inferior o igual a 125.")
            edad_correcta = True
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
