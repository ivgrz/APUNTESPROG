import random
import string


def generar_contraseña():
    contraseña = []
    print("GENERADOR DE CONTRASEÑAS")

    while True:
        tipos = 0
        longitud = input(
            "Indica la longitud de tu contraseña 'minimo 8 caracteres' (s/n)")
        digits = "s"

        mayus = input("Desea incluir mayusculas?(s/n): ")
        min = input("Desea incluir minusculas?(s/n): ")
        caracteres_especiales = input(
            "Desea incluir caracteres especiales?(s/n): ")

        if int(longitud) < 8:
            raise ValueError("Longitud de 8 como minimo")

        else:
            if mayus == "s":
                tipos += 1
                contraseña.append(random.choice(string.ascii_uppercase))
            elif min == "s":
                tipos += 1
                contraseña.append(random.choice(string.ascii_lowercase))
            elif caracteres_especiales == "s":
                tipos += 1
                contraseña.append(random.choice(string.punctuation))
            elif digits == "s":
                tipos += 1
                contraseña.append(random.choice(string.digits))
        contra_final = random.shuffle(contraseña)
