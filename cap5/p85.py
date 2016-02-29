#!/usr/bin/python
# -*- coding: utf-8 -*-

variable1 = "Hola"
variable2 = variable1
variable3 = "Adiós"
print id(variable1)
print id(variable2)
# la id de variable1 y variable2 serán la misma
print id(variable3)
# la id de variable3 es distinta
