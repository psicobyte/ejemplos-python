#!/usr/bin/python
# -*- coding: utf-8 -*-
class Viejo_Estilo:
    """ Ejemplo de clase Old Style"""

    def __init__(self,cadena):
        self.texto = cadena

    def mostrar(self):
        return self.texto


class Nuevo_Estilo(object):
    """ Ejemplo de clase New Style (hereda de object)"""

    def __init__(self,cadena):
        self.texto = cadena
        def mostrar(self):
        return self.texto


vieja = Viejo_Estilo("hola")

nueva = Nuevo_Estilo("hola")

print type(vieja)
# Mostrará "<type 'instance'>"

print type(nueva)
# Mostrará <class '__main__.Nuevo_Estilo'>
