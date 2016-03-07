#!/usr/bin/python
# -*- coding: utf-8 -*-

class MiClase:

    variable = 10

    @classmethod
    def metodo(cls):
        return cls.variable

objeto = MiClase

print objeto.metodo()
