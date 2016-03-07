#!/usr/bin/python
# -*- coding: utf-8 -*-

def filtra(dato):
    if dato > 5:
        return True
    else:
        return False

salida = filter(filtra,[1,7,9,3,5,9,10,3,1,4,11])

print salida
