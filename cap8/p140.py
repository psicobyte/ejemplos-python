#!/usr/bin/python
# -*- coding: utf-8 -*-
class Patas(object):

    def __init__(self):
        self.patas = 0

    def __get__(self, objeto, owner):
        return self.patas

    def __set__(self, objeto, value):
        try:
            self.patas = int(value)
        except ValueError:
            print("No es un entero")

    def __delete__(self, objeto):
        del self.patas


class Animal(object):

    patas = Patas()

    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas
        def muestra(self):
        print "El " + self.nombre + " tiene " + str(self.patas) + " patas."

chucho = Animal("perro", "A")
chucho.muestra()
