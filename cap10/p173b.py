#!/usr/bin/python
# -*- coding: utf-8 -*-

#Abrimos el fichero en modo lectura
fichero = open("lista.txt","r")

print fichero.readline()
print fichero.readline()
print fichero.readline()

fichero.close()
