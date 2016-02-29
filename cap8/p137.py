#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):

    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

    def muestra(self):
        print "El " + self.nombre + " tiene " + self.patas + "patas."

# Esta asignación funciona
chucho = Animal("perro", 4)
chucho.muestra()

# Pero esta fallará
error = Animal("perro", "A")
error.muestra()
