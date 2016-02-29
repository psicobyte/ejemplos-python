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


class Gato(Animal):
        """Clase hija para mostrar la herencia"""

    def maulla(self):
        print "Miau miau"

mi_mascota = Perro("Rufo",4)
mi_mascota.saluda()
mi_mascota.ladra()

mi_otra_mascota = Gato("Azrael",4)
mi_otra_mascota.saluda()
mi_otra_mascota.maulla()
