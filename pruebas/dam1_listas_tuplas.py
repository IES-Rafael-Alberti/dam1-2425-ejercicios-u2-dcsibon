
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
    limpiar_pantalla()

    a = 7

    print(f"{a:04d}")

    return

    mi_lista1 = [1, 2, (1, 2), 4]

    mi_lista1[2].append(22)

    res = ""
    cont = 0
    while cont < len(mi_lista1):
        res += f"{mi_lista1[cont]}, "
        cont += 1
    print(res[:-2])


    print(mi_lista1)





    return


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