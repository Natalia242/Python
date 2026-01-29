palabra = input("Introduce la palabra a buscar: ")

with open("datos.txt", "r") as fichero:
    print(fichero.read().lower().split().count(palabra.lower()))