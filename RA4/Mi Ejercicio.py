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