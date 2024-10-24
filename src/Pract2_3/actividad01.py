"""
Actividad 1: 
    Escribe un programa que capture la excepción división entre cero. Tendrá que mostar el mensaje del error capturado.
"""

def dividir(num1: float, num2: float = 1) -> float:
    """Realiza la división de dos números

    Args:
        num1 (float): número que vamos a dividir.
        num2 (float): número que será el divisor.
            (por defecto es 1)

    Returns:
        float: división redondeada a 2 decimales o None si se genera una excepción.
    """
    
    # Inicializar a None para no retornar un número si se produjo un error
    resultado = None

    resultado = num1 / num2
    
    resultado = round(resultado, 2)

    return resultado


def pedirNumero(msj: str) -> float:
    """Solicita un número

    Args:
        msj (str): mensaje que se muestra en consola para solicitar el número.
    
    Returns:
        float: número introducido por el usuario.
    """

    # Inicializar a None para no retornar un número si se produjo un error
    numero = None

    try:
        numero = float(input(msj))
    except:
       print("**Error** Número introducido no válido")

    return numero


def main():

    dividendo = pedirNumero("Introduzca el dividendo: ")
    
    # Para continuar comprobamos que se retornó un número en el dividendo
    if dividendo != None:
        divisor = pedirNumero("Introduzca el divisor: ")

        # Para continuar comprobamos que se retornó un número en el divisor
        if divisor != None:
            # Capturo la excepción fuera del método para comprobar la excepción en el test
            try:
                resultado = dividir(dividendo, divisor)
            except ZeroDivisionError:
                print("**Error** No es posible realizar la división por cero.")
            except:
                print("**Error** Se produjo un error y no es posible realizar la división.")

            # Solo mostrar el resultado si se retornó un número
            # Sino ya habrá mostrado un mensaje de error anteriormente
            if resultado != None:
                print(f"El resultado es {resultado}")


if __name__ == "__main__":
    main()