#!/usr/bin/python
# -*- coding: utf-8 -*-

# Abrimos el fichero en modo escritura
# Si el archivo ya existe, se borrará el contenido
fichero = open("nuevo.txt","w")

fichero.write("1234567890")

# movemos el puntero a 5 bytes
# desde el principio del fichero
fichero.seek(5)

fichero.write("XXX")

fichero.close()
