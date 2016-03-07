#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
usando el paquete de ejemplo "matematicas", con alias
"""

import matematicas.constantes as cons, matematicas.operaciones as ope

radio = 14

radio_cuadrado = ope.cuadrado(radio)
circunferencia = ope.multiplica(cons.pi, radio_cuadrado)

print circunferencia
