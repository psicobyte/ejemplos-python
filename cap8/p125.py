#!/usr/bin/python
# -*- coding: utf-8 -*-

class Producto:
    """ Ejemplo de clase con la cantidad y el precio de un producto"""

    def __init__(self,producto,precio,unidades):
        self.producto = producto
        self.precio = precio
        self.unidades = unidades126 PYTHON

    def __costo_total(self):
        costo = self.precio * self.unidades
        return costo

    def nuevo_precio(self,precio):
        self.precio = precio

    def agrega(self,cantidad):
        self.unidades = self.unidades + cantidad

    def saca(self,cantidad):
        if cantidad <= self.unidades:
            self.unidades = self.unidades - cantidad
        else:
            print "No hay suficientes"

    def informe(self):
        print "Producto: " + self.producto
        print "Precio: " + str(self.precio)
        print "Unidades: " + str(self.unidades)
        print "Precio Total: " + str(self.__costo_total())

mi_producto1 = Producto("Pantalón",100,6)

mi_producto2 = Producto("Camiseta",50,5)

print mi_producto1.precio
print mi_producto2.unidades

mi_producto2.agrega(5)
print mi_producto2.unidades

mi_producto2.informe()
