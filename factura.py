import datetime
from time import sleep
class factura:
    def tarifa(self):
        self.valor = self.duracion*self.costo
        print("El valor de su llamada fue de: $" + str(self.valor))



    def factura(self):
        fecha = datetime.datetime.today()
        fecha= fecha.strftime("%m/%d/%Y  %H:%M:%S")
        file = open("facturacion.txt", "r+")
        file.seek(0, 2)
        file.write(str(fecha) + "       " + self.numerollamante + "         " + self.numerollamado)
        file.write("           " + str(self.duracion) + "            " + str(self.valor)+"\n")
        file.seek(0, 0)
        file.close()
    
    def mostrarfactura(self):
        self.numerofacturado = input("\nPor favor ingrese el número a facturar: ")
        print("\n")
        file = open("facturacion.txt", "r")
        self.contador = 0
        
        for line in file:
            self.campo = line[27:34]# identifico el campo
            self.campo1= line[74:79]# identifico el total
            if (self.numerofacturado in self.campo):
                self.contador=self.contador+1
        file.close()
        if (self.contador >= 2):
            file = open("facturacion.txt", "r")
            for line in file:
                self.campo = line[27:34]# identifico el campo
                self.campo1= line[74:79]# identifico el total
                if (self.numerofacturado in self.campo):
                    print(str(line))    
            total.totall(self)
        else:
            print("El numero de llamadas es "+ str(self.contador)+", por lo tanto no se puede facturar.")
            
        
        file.close()

        sleep(10)

class total:
        
    def totall(self):
        file = open("facturacion.txt", "r")
        suma=0
        for line in file:
         self.campo = line[27:34]# identifico el campo
         self.campo1= line[74:79]# identifico el total
         if (self.numerofacturado in self.campo): 
            lista=float(self.campo1)
            suma=suma+lista
            
        suma=str(round(suma, 2))
        print("\nel valor total es:  "+ suma)