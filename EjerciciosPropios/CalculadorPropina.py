def calcular_propina():
    importe_total = (
        input("Dame el importe total de la comida y el numero de comensales en formato ('importe-numero'): "))
    importe, numero = importe_total.split('-')
    propina_diez = int(importe) * (10/100)
    propina_quince = int(importe) * (15/100)
    propina_veinte = int(importe) * (20/100)
    print(f"Para tu mesa de {numero} comensales deberian aportar una propina de {propina_diez:2.f} si es al 10%, de {propina_quince:.2f} si es al 15% y de {propina_veinte:.2f} al 20%")


if __name__ == "__main__":
    calcular_propina()
