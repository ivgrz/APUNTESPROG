from POO.EjercicioTipo.Cilindro import Cilindro
from circulo import Circulo
from punto import Punto
from persona import Persona
from Cilindro import Cilindro
p1 = Punto(2,3)
p2 = Punto (9,1)
p2.x = 2
p2.y = 3

p1 = p2
p3 = p2

p1.x = 99999
p3.x = 100


print(p1.toString())
print(p2)
print(p1 == p2)


manuel = Persona("Manuel", 53,"00000000T","Garcia Barbon,48", "Española")
manuela = Persona("Manuela", 15,"00000000T","Garcia Barbon,60", "Española")
print(manuel)
print(manuela == manuel)
print(manuela > manuel)
print(manuela < manuel)

c = Circulo(4,3,5)
print(c.Cadena())

ci = Cilindro(2,3,7,6)
print(ci.Cadena())
