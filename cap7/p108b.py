#!/usr/bin/python
# -*- coding: utf-8 -*-
def saluda(nombre, sexo):
    print "Hola " + nombre
    if sexo == "M" or sexo == "m":
        print "¿Cómo te va, hombre?"
    elif sexo == "F" or sexo == "f":
        print "¿Cómo te va, mujer?"
    else:
        print "¿Cómo te va?"

saluda("Paco", "M")
