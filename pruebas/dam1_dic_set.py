




def main():
    mi_lista = ["a", "b", "c"]
    mi_tupla = ("x", "y", "z")
    mi_conjunto = {"perro", "gato", "loro"}
    mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}

    print(id(mi_conjunto))

    return

    print(", ".join(mi_lista))                      # "a, b, c"
    print(" | ".join(mi_tupla))                     # "x | y | z"
    print(" - ".join(mi_conjunto))                  # "perro - gato - loro" (orden no garantizado)
    print(", ".join(mi_diccionario))                # "clave1, clave2"
    print(", ".join(f"{k}:{v}" for k, v in mi_diccionario.items()))  # "clave1:valor1, clave2:valor2"
    print(" - ".join(mi_diccionario.values()))

    return

    mi_lista = ["uno", 2, "tres"]
    resultado = ", ".join(map(str, mi_lista))
    print(resultado)

    a = set(range(1, 11))
    a.update([100, 101, 33, 4])
    print(a)

    a.add(25)
    a.add(33)

    for e in a:
        print(e, end=" ")

    print()

    while len(a) > 0:
        print(a.pop())

    return

    d = {'uno': 1, 'dos': 2, 'tres': 3}
    print(list(d))
    print(list(d.keys()))
    print(list(d.values()))
    print(list(d.items()))

    d.update([('cuatro', 4), ('cinco', 5)])
    print(list(d.items()))






if __name__ == "__main__":
    main()