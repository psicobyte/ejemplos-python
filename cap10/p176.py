#!/usr/bin/python
# -*- coding: utf-8 -*-

# Abrimos el fichero en modo escritura
# Si el archivo ya existe, se borrará el contenido
fichero = open("nuevo.txt","w")

for i in range(1,5):
    texto = "Línea %i\n" % i
    fichero.write(texto)

fichero.close()
