#!/usr/bin/python
# -*- coding: utf-8 -*-

variable= "fuera de la función"
def una_funcion():
    global variable
    variable = "dentro de la función"
    print variable

una_funcion()
print variable
