
def pedir_numero(msj: str) -> float:
    numero = None
    while numero is None:
        try:
            numero = float(input(msj).strip().replace(",", "."))
        except ValueError:
            print("*ERROR* El número introducido no es válido!")
        except Exception as e:
            print(f"*ERROR* Se ha producido un error: {e}")

    return numero


def dividir(num1, num2) -> float:
    if num2 == 0:
        raise ZeroDivisionError("*ERROR* No es posible la división por cero!")
    
    return num1 / num2


def main():
    print("Vamos a realizar la división de dos números...")    
    num1 = pedir_numero("Introduzca el número que desea dividir: ")
    num2 = pedir_numero("Introduzca el divisor del número anterior: ")

    try:
        resultado = dividir(num1, num2)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"*ERROR* Se ha producido un error: {e}")
    else:
        print(f"La división es: {resultado:.2f}")


if __name__ == "__main__":
    main()