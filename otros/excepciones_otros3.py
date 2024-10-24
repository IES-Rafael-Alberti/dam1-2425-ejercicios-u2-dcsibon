
class MiError(Exception):
    """Excepción personalizada para errores específicos."""
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def comprobar_valor(valor):
    if valor < 0:
        raise MiError("El valor no puede ser negativo.")
    else:
        print("El valor es válido:", valor)


def main():
    try:
        numero = int(input("Introduce un número: "))
        comprobar_valor(numero)
    except MiError as e:
        print(f"*ERROR* {e}")
    except ValueError:
        print("*ERROR* El valor debe ser un número entero.")


if __name__ == "__main__":
    main()
