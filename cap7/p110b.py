#!/usr/bin/python
# -*- coding: utf-8 -*-

def imprime_datos(nombre, **datos):
    print "Datos de " + nombre
    for clave in datos:
        print clave + ": " + datos[clave]

imprime_datos("Pablo", edad = "mucha", estado = "enloquecido", guapo = "no")
