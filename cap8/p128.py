#!/usr/bin/python
# -*- coding: utf-8 -*-
class Animal:
    """Clase base para mostrar la herencia"""

    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas
        def saluda(self):
            print "El animal llamado " + str(self.nombre) + " saluda"

class Perro(Animal):
    """Clase hija para mostrar la herencia"""

    def ladra(self):
        print "Guau"

mi_mascota = Perro("Rufo",4)
mi_mascota.saluda()
mi_mascota.ladra()
