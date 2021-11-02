# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:19:11 2021

@author: Abraham
"""

import redis
r= redis.Redis(host='127.0.0.1', port=6379,db=12)

#Creamos las funciones que manipularan las bases de datos

def insertar(a,b):
    diccionario_agg = ({'Palabra_Español':a,
                        'Palabra_Slang':b})
    col.insert_one(diccionario_agg)

def mostrarDatos():
    for documentos in col.find({}):
        print(documentos)

def editarSignificado(PalabraV,SignificadoN):
    col.update_many({'Palabra_Español': PalabraV},{"$set": {"Palabra_Slang":SignificadoN}})

def eliminar(PalabraE):
    col.delete_one({'Palabra_Español': PalabraE})

def significadopalabra(palabrasig):
    for x in col.find({'Palabra_Español':palabrasig}):
        print (x)

#Una vez definidas todas las funciones le damos inicio al programa con un bucle While


print("Inicio del Programa Diccionario Slang Panameño")