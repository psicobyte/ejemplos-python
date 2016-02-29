#!/usr/bin/python
# -*- coding: utf-8 -*-
class Animal:
    """Clase base para mostrar la herencia"""

    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

    def saluda(self):
        print "El animal llamado " + str(self.nombre) + " saluda"


class Amigo:
    """Clase base para mostrar la herencia"""

    def __init__(self, nombre):
        self.nombre = nombre

    def salir(self, num):
        if num == 0:
            print "Vamos a pasear"
        elif num == 1:
            print "Vamos a jugar"
        else:
            print "Vamos al parque"

class Perro(Animal,Amigo):
    """Clase hija para mostrar la herencia"""

    def ladra(self):
        print "Guau"

mi_mascota = Perro("Rufo",4)
mi_mascota.saluda()
mi_mascota.salir(1)
