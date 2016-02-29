#!/usr/bin/python
# -*- coding: utf-8 -*-

def genera_lista(num):
    lista = []
    i = 1
    while i <= num:
        lista.append(i)
        i += 1
    return lista
for i in genera_lista(5):
    print i
