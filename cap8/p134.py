#!/usr/bin/python
# -*- coding: utf-8 -*-
class Palabra:
    """Clase para mostrar el método __cmp__"""

    def __init__(self, contenido):
        self.contenido = contenido

    def __cmp__(self, otro):
        if self.contenido > otro.contenido:
            return 1
        elif self.contenido < otro.contenido:
            return -1
        else:
            return 0


larga = Palabra("supercalifragilisticoespialidoso")
corta = Palabra ("bah")

if (larga > corta):
    print larga.contenido + " es mayor que " + corta.contenido
else:
    print larga.contenido + " NO es mayor que " + corta.conte-
nido
