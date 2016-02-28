#!/usr/bin/python
# -*- coding: utf-8 -*-
lista = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"]
lista2 = lista[1:4]
print lista2
# Mostrará "['segundo', 'tercero', 'cuarto']"
lista2[0:2] = ["otro", "Y otro"]
print lista2
# Mostrará "['otro', 'Y otro', 'cuarto']"
