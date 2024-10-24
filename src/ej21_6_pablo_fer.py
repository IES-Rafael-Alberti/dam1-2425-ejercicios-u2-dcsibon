# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

ABECEDARIO = "abcdefghijklmnñopqrstuvwxyz"


# DCS: Vamos a ser un poco más estricto a la hora de dar nombre a la función
# es más coherente mostrar_grupo(), también te cambio el primer parámetro ya
# que estamos comprobando la inicial solo
def mostrar_grupo(inicial: str, sexo: str):
    # DCS... sobra, ya son str y no hay que volver a convertirlas
    #nombre = str(nombre)
    #sexo = str(sexo)

    # DCS: La condición también era errónea...
    if (inicial < "m" and sexo == "F") or (inicial > "n" and sexo == "M"):
        return print("Perteneces el grupo A")
    else:
        return print("Perteneces al grupo B")


def validar_datos(nombre, sexo): 
    # FIX ME [ HAY QUE HACER QUE NO ME PERMITA ENVIAR DATOS QUE SEAN NÚMEROS ENTEROS O DECIMALES ] [SI ESTA FUNCION SE COMENTA, EL CÓDIGO HACE SU FUNCION PERO PERMITE NÚMEROS]

    # DCS... no tiene sentido hacer esto, nombre y sexo son de tipo str, esa comparación no es correcta.
    # NO puedes retornar ValueError... en todo caso lanzas la excepción!
    # Lo correcto es: raise ValueError("Descripción del error")
    while nombre.isdigit() and sexo.isdigit():
        try:
            if nombre == int or nombre == float:
                return ValueError("El nombre ha de ser una letra del abecedario!")
            elif sexo == int or sexo == float:
                return ValueError("El sexo debe ser o masculino o femenino!")

        except:
            return nombre, sexo
        

# DCS: Si quieres validar... hazlo por separado:
def pedir_nombre() -> str:
    nombre_correcto = False
    while not nombre_correcto:
        nombre = input("Introduzca su nombre: ").strip().lower()
        try:
            # Comprobar si la primera posición es una letra del abecedario.
            if nombre[:1] not in ABECEDARIO:
                raise ValueError("El nombre debe comenzar por una letra.")
            
            nombre_correcto = True
        except ValueError as e:
            print(f"*ERROR* {e}")

    return nombre


# DCS: Suena a otra cosa ehhh :-P
def pedir_sexo() -> str:
    sexo_correcto = False # DCS: Sin comentarios :-)
    while not sexo_correcto:
        sexo = input("Introduzca con que genero se identifica\nM | F: ").strip().upper()
        try:
            # Comprobar si la primera posición es una letra del abecedario.
            if len(sexo) != 1 or sexo not in "MF":
                raise ValueError("El sexo debe ser M o F!")
            
            sexo_correcto = True
        except ValueError as e:
            print(f"*ERROR* {e}")

    return sexo


def main():
    # DCS: Corregido

    nombre = pedir_nombre()
    sexo = pedir_sexo()
    mostrar_grupo(nombre[:1], sexo)

    return


    # DCS... es una función y debes poner los paréntesis => lower()
    # y ya puesto quitamos espacios a los lados para evitar confusiones
    nombre = input("Introduzca su nombre: ").strip().lower()
    
    # DCS... el sexo también deberíamos de ceonvertirlo a mayúsculas!
    # y ya puesto quitamos espacios a los lados para evitar confusiones
    sexo = input("Introduzca con que genero se identefica\nM | F: ").strip().upper()

    validar_datos(nombre, sexo)
    asignar_grupo(nombre, sexo)


if __name__ == "__main__":
    main()


""" 
pertenece al grupo A si tiene un nombre anterior a la M(L) y es mujer 

posterior a la N(R) y es hombre,

SINO el resto pertenecera al grupo B """