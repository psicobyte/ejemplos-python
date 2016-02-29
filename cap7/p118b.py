#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ejemplo de decorador
"""
def decorador(funcion_entrada):
    def funcion_salida(param):
        if param == "Lidia":
            print "Buenos días, guapa"
        elif param == "Pablo":
            print "Buenos días, guapo"
        else:
            funcion_entrada(param)
        print "Que tengas un buen día"
            return funcion_salida

@decorador
def saludo(nombre):
    print "Hola " + nombre

saludo("Pablo")
