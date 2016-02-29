#!/usr/bin/python
# -*- coding: utf-8 -*-

resultado = 3 == 2

print resultado
# 3 no es igual a 2, por lo que es falso

print True and True
# algo que es "cierto y cierto" es cierto

print True and resultado
# algo que es "cierto y falso" es falso

print not True
# "no cierto" es falso

print False or resultado
# algo que es "falso o falso" es falso
