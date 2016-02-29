#!/usr/bin/python
# -*- coding: utf-8 -*-

lista = ["Hola","mundo","palabra"]
lista2 = list(lista)
print id(lista)
print id(lista2)
# Los id son distintos
diccionario = {"nombre": "Pablo", "Apellido": "Hinojosa"}
diccionario2 = dict(diccionario)
print id(diccionario)
print id(diccionario2)
# Los id son distintos
