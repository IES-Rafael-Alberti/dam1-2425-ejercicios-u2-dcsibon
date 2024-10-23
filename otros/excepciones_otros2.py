
def validar_edad(edad: int):
    if edad < 0:
        raise ValueError("*ERROR* La edad no puede ser negativa.")
    elif edad > 120:
        raise ValueError("*ERROR* La edad no puede ser mayor a 120.")
    return edad


def main():
    try:
        edad = int(input("Introduce tu edad: "))
        validar_edad(edad)
        print(f"Tu edad es: {edad}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()