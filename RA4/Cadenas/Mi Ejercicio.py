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

def encontrar_palabra(palabras1 = "clavó", palabras2 = "un"):
    if palabras1 in a:
        a2 = a.replace(palabras1, "\b")
    else:
        a2 = a.replace(palabras2 + " ", f"{"\b" * (len(a) - len(palabras2))}")

    if palabras1 in b:
        b2 = b.replace(palabras1, "\b")
    else:
        b2 = b.replace(palabras2 + " ", f"{"\b" * (len(b) - len(palabras2))}")

    print(a2)
    print(b2)
    print(a2[a2.find(" ") + 1::2])
    print(b2[b2.find(" ") + 1::2])

a = "Pablito clavó un clavito."
b = "Tres tristes tigres comían trigo en un trigal."

palabra1 = input("Introduce la palabra principal a buscar: ")
palabra2 = input("Introduce la palabra secundaria a buscar: ")

if palabra1 and palabra2:
    encontrar_palabra(palabra1, palabra2)
elif palabra1 and not palabra2:
    encontrar_palabra(palabra1)
elif palabra2 and not palabra1:
    encontrar_palabra(palabra2)
else:
    encontrar_palabra()