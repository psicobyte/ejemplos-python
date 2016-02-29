#!/usr/bin/python
# -*- coding: utf-8 -*-

datos = {"Nombre": "José", "Apellido": "Gonzalez", "Altura": "1,80"}
for concepto, valor in datos.iteritems():
    print concepto + ": " + valor
