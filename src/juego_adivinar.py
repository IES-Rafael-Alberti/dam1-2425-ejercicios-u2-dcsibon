import random
 
def no_has_adivinado(num_user,numero_pc):
        if num_user != numero_pc:
                print("FALLASTE")
        main()

def adivino_ese_numero(num_user, numero_pc):
        contador = 1
        fin = 0
        while not num_user == numero_pc:
                fin += contador
                if num_user < numero_pc:
                        num_user = int(input("MÁS:  "))
                        print(f"Vas por el {fin} intento de 5")
                else: 
                        num_user =int(input("MENOS: "))
                        print(f"Vas por el {fin} intento de 5")
                if fin == 5:
                        no_has_adivinado(num_user,numero_pc)
        return("LO CONSEGUISTE")

    
    
def main():
numero_pc = random.randint(1,100)
num_user = int(input("Introduce un número del 1 al 100: "))
adivino_ese_numero(num_user,numero_pc)
print (adivino_ese_numero(num_user,numero_pc))


if __name__ == "__main__":
    main()