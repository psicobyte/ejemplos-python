#!/usr/bin/python
# -*- coding: utf-8 -*-

#Abrimos el fichero en modo lectura
fichero = open("lista.txt","r")

contenido = fichero.read()

print contenido

fichero.close()
