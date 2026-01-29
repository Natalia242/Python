with open("datos.txt", "r") as fichero:
    lineas = fichero.readlines()

with open("invertido.txt", "w") as invertido:
    for linea in reversed(lineas):
        invertido.write(linea)