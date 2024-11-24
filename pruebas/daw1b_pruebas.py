import os


def borrar_consola():
    os.system ("cls")


def pausar(salto_antes = True, limpiar_despues = True):
    if salto_antes: 
        print()
    
    os.system("pause")
    
    if limpiar_despues:
        borrar_consola()


def producto_escalar(vector1, vector2) -> int:
    producto = 0
    for i in range(len(vector1)):
        producto += vector1[i] * vector2[i]


    producto = 0
    cont = 0
    for elemento in vector1:
        producto += elemento * vector2[cont]
        cont += 1


def main():
    borrar_consola()

    vector1 = (1, 2, 3)
    vector2 = (-1, 0, 2)

    resultado = producto_escalar(vector1, vector2)



if __name__ == "__main__":
    main()