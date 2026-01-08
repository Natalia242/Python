'''
Ejercicio Natalia:
Escribe un programa en Python que solicite al usuario una cadena de
texto y, posteriormente, una palabra a buscar dentro de esa cadena.
El programa deberá comprobar si la palabra aparece en el texto.

Si la palabra se encuentra, el programa debe imprimir el texto original
pero eliminando únicamente la primera aparición de esa palabra.

Si la palabra no se encuentra en la cadena:
    El programa debe eliminar alguna palabra existente de la cadena (puede ser la primera, la última o 	cualquier otra, según prefieras diseñarlo).
    Luego debe mostrar la cadena, sin nada delante de esa palabra.

Finalmente, debe mostrar ambas cadenas resultantes.

Luego imprime por pantalla a partir de la segunda palabra y solo las letras pares.
    (ejemplo:   "trigal."
                Imprimiría: rgl
                "Pablito un clavito."
                Imprimiría: u lvt.)
'''
import random

tupla = ("Pablito", "clavó", "un", "clavito", ".")

if "clavitos" in tupla:
    for i in range(len(tupla)):
        if tupla[i] != "clavito":
            print(tupla[i])
else:
    i = random.randrange(len(tupla))
    print(tupla[i:])