#!/usr/bin/python
# -*- coding: utf-8 -*-

class Mensaje(object):
    """ Ejemplo de clase New Style (hereda de object)"""

    def __init__(self):
        self.texto = "Soy una clase de nuevo estilo, porque soy hija de 'object'"

    def mostrar(self):
        print self.texto


mi_objeto = Mensaje()
mi_objeto.mostrar()
