"""
Ejercicio 2.1.10

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

    - Ingredientes vegetarianos: Pimiento y tofu.
    - Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

import os


def preguntarTipoPizza():
    """
    Pedir el tipo de la pizza.

    Retorna
    -------
    int     un entero con el valor del tipo de pizza => 1: vegetariana / 2: no vegetariana
    """
    tipo = -1
    while tipo != 1 and tipo != 2:
        tipo = pedirNumero("Elija el tipo de pizza (1. vegetariana / 2. NO vegetariana) => ", 1, 2)
        if tipo == -1:
            print("**ERROR** tipo de pizza no válido...")

    return tipo


def obtenerListaIngredientes(tipo):
    """
    Obtener los ingredientes según el tipo de pizza.
    
    Params
    ----------
    int     tipo de pizza => 1 = vegetariana / 2 = no vegetariana
    
    Retorna
    -------
    str     una cadena de caracteres con los ingredientes de cada pizza.
    """
    if tipo == 1:
        # pizza vegetariana
        lista = ["pimiento", "tofu"]
    elif tipo == 2:
        # pizza no vegetariana
        lista = ["peperoni", "salmón", "jamón"]
    else:
        # error, pizza no válida
        lista = []
    return lista


def muestraIngredientes(listaIngredientes):
    resultadoPantalla = ""
    cont = 1
    for ingrediente in listaIngredientes:
        resultadoPantalla += str(cont) + " - " + ingrediente + "\n"
        cont += 1
    return resultadoPantalla


def eligeIngrediente(listaIngredientes):
    print("\nIngredientes disponibles para esta pizza")
    print("----------------------------------------")
    print(muestraIngredientes(listaIngredientes))

    ingredienteExtra = -1
    while ingredienteExtra == -1:
        ingredienteExtra = pedirNumero("Elige el ingrediente extra de tu pizza: ", 1, len(listaIngredientes))
        if ingredienteExtra == -1:
            print("**Error** elige un número válido de la lista...")
    return ingredienteExtra


def pedirNumero(mensaje, min, max):
    entrada = input(mensaje)
    if entrada.isnumeric() and min <= int(entrada) <= max:
        return int(entrada)
    else:
        return -1


def mostrarPizza(tipo, listaIngredientes, ingrediente):
    frase = "\nHas elegido una pizza "
    if tipo == 1:
        frase += "vegetariana con tomate, mozzarella y "
    else:
        frase += "no vegetariana con tomate, mozzarella y "
    frase += listaIngredientes[ingrediente - 1] + ".\n"
    return frase


def borrarConsola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def main():
    borrarConsola()

    print("\nBienvenido a la pizzería Bella Napoli...\n")
    
    tipo = preguntarTipoPizza()

    listaIngredientes = obtenerListaIngredientes(tipo)

    if len(listaIngredientes) > 0:
        ingrediente = eligeIngrediente(listaIngredientes)

    print(mostrarPizza(tipo, listaIngredientes, ingrediente))


if __name__ == "__main__":
    main()