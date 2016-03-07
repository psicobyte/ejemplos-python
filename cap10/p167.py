#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

numero_argumentos = len(sys.argv)
print "Argumentos (" + str(numero_argumentos) + "):"

for argumento in sys.argv:
    print '- ' + argumento
