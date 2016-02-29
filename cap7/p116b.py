#!/usr/bin/python
# -*- coding: utf-8 -*-

def genera_lista(num):
    lista = []
    i = 1

    while i <= num:
        yield i
        i += 1


lista = genera_lista(5)

for i in genera_lista(5):
    print i
