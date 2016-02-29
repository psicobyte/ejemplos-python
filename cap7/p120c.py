#!/usr/bin/python
# -*- coding: utf-8 -*-

cuadrado = lambda x: x**2
suma= lambda x, y: x + y
resultado= cuadrado(suma(cuadrado(2),5))
print resultado
