from CalculadoraBinaria import  CalculadoraBinaria

if __name__ == '__main__':
    Calculadora1 = CalculadoraBinaria(12,13)
print(Calculadora1.operacion(1))
print(Calculadora1.operacion(2))
print(Calculadora1.operacion(3))
print(Calculadora1.operacion(4))
c2 = CalculadoraBinaria(13,0)
try:
    print(c2.operacion(4))
except ZeroDivisionError:
    print("Cuidado: Division indeterminada")
finally:
    print("Fin del programa")