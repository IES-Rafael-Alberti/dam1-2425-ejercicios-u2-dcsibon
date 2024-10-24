
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
    resultado = None
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        print("*ERROR* No es posible la división por cero!")
    except Exception as e:
        print(f"*ERROR* Se ha producido un error: {e}")
    
    return resultado


def main():
    print("Vamos a realizar la división de dos números...")    
    num1 = pedir_numero("Introduzca el número que desea dividir: ")
    num2 = pedir_numero("Introduzca el divisor del número anterior: ")

    resultado = dividir(num1, num2)

    if resultado is not None:
        print("La división es {:.2f}".format(resultado))


if __name__ == "__main__":
    main()