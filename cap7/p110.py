#!/usr/bin/python
# -*- coding: utf-8 -*-

def imprime_lista(nombre_lista, *cosas):

    print "Lista de " + nombre_lista

    for cosa in cosas:
        print cosa

imprime_lista("Piezas", "tornillo", "tuerca", "otro tornillo", "cable")
