#!/usr/bin/python
# -*- coding: utf-8 -*-
primero = 3
while primero <= 7:
    print "Tabla del " + str(primero)
    segundo = 1
    while segundo <= 10:
        print str(primero) + " X " + str(segundo) + " = " +
        str(primero * segundo)
        segundo += 1
    primero += 1
print "#################"
