#!/usr/bin/python
# -*- coding: utf-8 -*-

#Abrimos el fichero en modo lectura
fichero = open("lista.txt","r")

lista_lineas = fichero.readlines()

print lista_lineas[1]
print lista_lineas[3]
print lista_lineas[4]

fichero.close()
