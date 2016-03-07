#!/usr/bin/python
# -*- coding: utf-8 -*-

un_texto = "Hola mundo"
otro_texto = "Adiós mundo"

# Abrimos el fichero en modo escritura
# Si el archivo ya existe, se borrará el contenido
fichero = open("nuevo.txt","w")

fichero.write(un_texto)
fichero.write(otro_texto)

fichero.close()
