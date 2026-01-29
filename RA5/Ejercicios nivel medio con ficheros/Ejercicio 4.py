try:
    palabra = input("Ingrese la palabra a reemplazar: ")
    nueva = input("Ingrese la palabra nueva: ")

    with open("datos.txt", "r") as fichero:
        lineas = fichero.read()

    lineas = lineas.replace(palabra, nueva)

    with open("datos.txt", "w") as fichero:
        fichero.write(lineas)

except FileNotFoundError:
    print("El fichero no existe")