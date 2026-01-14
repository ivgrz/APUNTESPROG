from CalculadoraBinaria import  CalculadoraBinaria
from Persona2 import Persona2
from RegistroPersonas import RegistroPersonas
if __name__ == '__main__':
    Calculadora1 = CalculadoraBinaria(12,13)
print(Calculadora1.operacion(1))
print(Calculadora1.operacion(2))
print(Calculadora1.operacion(3))
print(Calculadora1.operacion(4))
c2 = CalculadoraBinaria(13,4)
try:
    print(c2.operacion(4))
except ZeroDivisionError as e:
    print("-_-: Division indeterminada")
finally:
    print("Fin del programa")

c3 = CalculadoraBinaria(12,4)
try:
    print(c3.operacion(1))
except TypeError as e:
    print(f"El dato no tiene un tipo valido")

p1 = Persona2("Juan",edad=23,dni="8327432Y")

p2 = Persona2("Ana",edad=30,dni="8327432Y")

registro = RegistroPersonas()
registro.agregar_personas(p1)
registro.agregar_personas(p2)
print(registro.mostrar_registro())
