
def pedir_pass() -> str:
    return input("Introduzca la contraseña: ").lower()    


def comprobar_pass(pass_usuario, pass_secreta) -> bool:
    if pass_usuario == pass_secreta:
        return True
    else:
        return False


def main():
    passwd_secreta = "contraseña"

    passwd_usuario = pedir_pass()

    if comprobar_pass(passwd_usuario, passwd_secreta) == True:
        print("Contraseña correcta!")
    else:
        print("ERROR")



if __name__ == "__main__":
    main()
