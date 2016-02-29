#!/usr/bin/python
# -*- coding: utf-8 -*-
class Producto:
    """ Ejemplo de clase con la cantidad y el precio de un producto"""

    def __init__(self,producto,precio,unidades):
        self.producto = producto
        self.precio = precio
        self.unidades = unidades

    def costo_total(self):
        costo = self.precio * self.unidades
        return costo


mi_objeto_producto = Producto("corbata",35,67)

print mi_objeto_producto.producto
print mi_objeto_producto.precio
print mi_objeto_producto.unidades
print mi_objeto_producto.costo_total()
