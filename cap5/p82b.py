#!/usr/bin/python
# -*- coding: utf-8 -*-
diccionario = {"animal": "gato", "cosa": "piedra", "planta": "lechuga"}
print diccionario
# Mostrará {'planta': 'lechuga', 'cosa': 'piedra', 'animal': 'gato'}
print diccionario["animal"]
# Mostrará "gato"
print diccionario["planta"]
# Mostrará "lechuga"
diccionario["planta"] = "coliflor"
print diccionario["planta"]
# Ahora mostrará "coliflor"
