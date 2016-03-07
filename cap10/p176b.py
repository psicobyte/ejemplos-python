#!/usr/bin/python
# -*- coding: utf-8 -*-

mi_lista = ["Primera","Segunda","Tercera"]

#Abrimos el fichero en modo escritura
fichero = open("nuevo.txt","w")

fichero.writelines(mi_lista)

fichero.close()
