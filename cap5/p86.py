#!/usr/bin/python
# -*- coding: utf-8 -*-

lista = ["Hola","mundo","palabra"]

print id(lista)

lista[2] = "cosa"

print id(lista)
# El id no ha cambiado
