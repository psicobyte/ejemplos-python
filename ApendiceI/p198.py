#!/usr/bin/python
# -*- coding: utf-8 -*-

def concatena(a, b):
    return a + "-" + b

salida = reduce(concatena,["1","2","3","4","5"])

print salida
