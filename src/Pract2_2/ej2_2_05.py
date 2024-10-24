"""
Ejercicio 2.2.5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
# Formula para calcular El capital tras un año.
    amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
"""

from EjerciciosU2.Pract2_2.ej2_2_03 import borrarConsola, pedirNumeroEnteroPositivo


def comprobarFloat(entrada: str):
    return entrada.count(".") <= 1 and entrada.replace(".", "").isnumeric()


def pedirNumeroFloat(mensaje: str):
    entrada = input(mensaje).replace(" ", "")
    
    while not comprobarFloat(entrada):
        entrada = input("**ERROR**, entrada no válida\n" + mensaje).replace(" ", "")
    
    #Retornamos el número introducido convertido a float
    return float(entrada)


def rendimientoCapital(capital: float, interes: float, annios: int):

    rendimientoAnual = ""
    cont = 1

    while cont <= annios:
        capital *= 1 + interes / 100
        rendimientoAnual += "Año {:>2} => {:.2f}\n".format(cont, capital)
        cont += 1

    return rendimientoAnual

def main():
    borrarConsola()
    
    capital = pedirNumeroFloat("Introduzca el capital invertido: ")
    interes = pedirNumeroFloat("Introduzca el interés del fondo: ")
    annios = pedirNumeroEnteroPositivo("Introduzca el número de años a invertir: ")

    print(rendimientoCapital(capital, interes, annios))
    

if __name__ == "__main__":
    main()