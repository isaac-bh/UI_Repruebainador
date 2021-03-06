#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import sys
import os

id = sys.argv[1]
ruta_absoluta = os.getcwd()
ruta_archivo = ruta_absoluta + "/python/respuestasExamenes.txt"

def validacionExamen(id):
    # Variable auxiliar.
    aux = ""
    # Abrimos el documento de texto en modo de solo lectura.
    examenes = open(ruta_archivo, "r")
    # Bucle: por cada linea dentro del archivo txt.
    for linea in examenes.readlines():
        aux = ""
        # Bucle: por cada caracter dentro de la linea.
        for letra in linea:
            # Si la letra en curso del bucle es ":", se rompe el ciclo.
            if letra == ":":
                break
            # Si no, se suma la letra a la variable auxiliar.
            else:
                aux += letra
        
        # Si auxiliar es igual al ID deseado, se retorna True
        if aux == id:
            return "True"

print(validacionExamen(id))
sys.stdout.flush()