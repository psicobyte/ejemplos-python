#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importamos los módulos
import primero, segundo

variable = "Estoy en el cuerpo principal"

def funcion_ejemplo():
    """ Función que muestra un texto """
    print variable

print "Llamamos a la función de este mismo módulo:"
funcion_ejemplo()

print 'Llamamos a la función del módulo "primero":'
primero.funcion_ejemplo()

print 'Llamamos a la función del módulo "segundo":'
segundo.funcion_ejemplo()

print "También podemos acceder a las variables:"

print variable
print primero.variable
print segundo.variable
