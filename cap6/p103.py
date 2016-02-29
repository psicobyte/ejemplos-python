#!/usr/bin/python
# -*- coding: utf-8 -*-

dividendo = "A"
divisor = 2

try:
    resultado = dividendo/divisor

except ZeroDivisionError:
    if divisor == 0:
        print "No puedes dividir por cero, animal"

except TypeError:
    print "Hay que ser bruto: eso no es un número"

else:
    print "La división resulta: ", resultado
