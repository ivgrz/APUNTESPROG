from Bombilla import Bombilla

if __name__ == '__main__':
    print("=== Creando bombillas ===")
    bombilla1 = Bombilla("rojo", "Y784238")
    bombilla2 = Bombilla("azul", "Y43587")
    bombilla3 = Bombilla("verde", "Y987654")

    # print("\n=== Estado inicial (interruptor general apagado) ===")
    # bombilla1.enciende()
    # bombilla2.conmuta()
    # bombilla3.enciende()

    # print(bombilla1)
    # print(bombilla2)
    # print(bombilla3)

    # print("=== Encendiendo interruptor general ===")
    # Bombilla.cambiar_interruptor_general(True)

    # print(bombilla1)
    # print(bombilla2)
    # print(bombilla3)

    # print("=== Apagando bombilla1 individualmente ===")
    # bombilla1.apaga()
    # print(bombilla1)
    # print(f"¿Bombilla1 está realmente encendida? {bombilla1.esta_encendida()}")

    # print("\n=== Apagando interruptor general ===")
    # Bombilla.cambiar_interruptor_general(False)
    # print(bombilla1)
    # print(bombilla2)
    # print(bombilla3)

    # print(
    #     f"Estado del interruptor general: {Bombilla.obtener_interruptor_general()}")

bombilla1.interruptor_general = True
print(str(bombilla1.interruptor_general))
print(bombilla1)
