
import os


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    """
    os.system('clear' if os.name == 'posix' else 'cls')


def pausa():
    """
    Pausa la ejecución del programa hasta que se pulse ENTER.
    """
    input("\nPresione ENTER para continuar...")
    limpiar_pantalla()


def main():
    asignaturas = ["Mates", "Lengua", "Inglés", "Física", "Química", "Historia"]

    limpiar_pantalla()

    print(asignaturas)

    pausa()

    for asignatura in asignaturas:
        print(asignatura)

    pausa()

    for i in range(len(asignaturas)):
        if i < len(asignaturas) - 1:
            print(asignaturas[i], end = " - ")
        else:
            print(asignaturas[i] + ".")

    pausa()

    pos = 0
    frase = ""
    while pos < len(asignaturas):
        frase += asignaturas[pos] + ", "
        pos += 1
    print(frase[:-2] + '.')

    pausa()


if __name__ == "__main__":
    main()