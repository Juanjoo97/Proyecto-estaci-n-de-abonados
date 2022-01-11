import sys, os
from central import *
from time import *
from factura import *

central = Central()
factura=factura()
#4 numero de 6
#el numero que se seleccionado no cambie
#facturacion: sumatoria del costo de la llamada
def menu():
    print("\nBIENVENIDO, A LA MEJOR CENTRAL TELEFONICA DE NEIVA")
    print("\n¿Que desea realizar?\n")
    print("1. Hacer una llamada")
    print("2. Facturación")
    print("3. Salir \n")


reset = False
while True:
    menu()
    elegir = input()
    if (elegir == "1"):
        central.IniciandoAbonados()
        central.Llamadas()
        reset = True

    elif (elegir == "2"):
        factura.mostrarfactura()

    elif (elegir == "3"):
        sys.exit()

    else:
        print("No presionó ninguna opción del menú, intente de nuevo")
        sleep(3)

    if(reset):
        sleep(3)
        os.system("cls")
        central = Central()
        reset = False
