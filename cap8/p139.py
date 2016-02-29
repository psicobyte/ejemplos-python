#!/usr/bin/python
# -*- coding: utf-8 -*-

class Descriptor(object):

    def __init__(self):
        self.var = ""

    def __set__(self, objeto, valor):
        print "Asignando un valor al atributo"
        self.var = valor

    def __get__(self, objeto, clase):
        print "Obteniendo el valor del atributo"
        return self.var

    def __delete__(self, objeto):
        print "Borrando el atributo"
        del self.var


class Mi_Clase(object):

    mi_atributo = Descriptor()

    def __init__(self, texto):
        self.mi_atributo = texto

mi_objeto = Mi_Clase("hola")

texto = mi_objeto.mi_atributo
mi_objeto.mi_atributo = "adios"
del mi_objeto.mi_atributo

print texto
