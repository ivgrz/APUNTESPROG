from Persona2 import Persona2
from nussError import nussError
from Dnierror import Dnierror

if __name__ == '__main__':

    personas_pruebas = [
        ("Alvaro",15,"12345678Z","12/3456789012/34"),
        ("Juana_nl",40,"12345678Z","123456789012345"),
        ("Nuss-pos",20,"12345678Z","12-3456789012-34"),
        ("NussNone",50,"12345678Z",None),
        ("Dni_invalido", 30, "ABC", "12/3456789012/34")

    ]

    for nombre, edad, dni, nuss in personas_pruebas:
        try:
            persona = Persona2(nombre, edad, dni, nuss)
            print(f"creado: {persona}")
        except nussError as e:
            print(f"Error al crear al usuario {nombre}: {e}")
        except Dnierror as e:
            print(f"Error al crear al usuario {nombre}: {e}")
        except Exception as e:
            print(f"Error al crear al usuario {nombre}: {e}")