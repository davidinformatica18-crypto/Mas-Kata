import pytest

def validar_password(password): # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    if len(password) < 8:
        return False

    numero = False

    for caracter1 in password: # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
        if caracter1.isdigit():
            numero = True

    if not numero:
        return False

    especial = False

    for caracter2 in password: # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
        if not caracter2.isalnum():
            especial = True

    if not especial:
        return False

    return True


password = input("Introduce contraseña: ") # _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

try:
    if validar_password(password):
        print("Contraseña Correcta valgame dios que fiera")
    else:
        print("Cariño es demasiado corta")

except Exception:
    print("Ha ocurrido un error llama a Jacobo")
