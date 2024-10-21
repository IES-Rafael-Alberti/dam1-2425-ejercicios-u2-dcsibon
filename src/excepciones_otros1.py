
def dividir(num1: float, num2: float) -> float:
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print("*ERROR* No se puede dividir por cero.")
    finally:
        print("Finalizando la operación de división.")


def main():
    num1 = 10
    num2 = 0
    resultado = dividir(num1, num2)
    if resultado is not None:
        print(f"El resultado de la división es: {resultado}")


if __name__ == "__main__":
    main()