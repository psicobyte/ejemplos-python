#!/usr/bin/python
# -*- coding: utf-8 -*-

código = """
def funcion():
    print "Aquí pasan cosas"

funcion()
"""

compilado = compile(código,"","exec")

print compilado

exec(compilado)
