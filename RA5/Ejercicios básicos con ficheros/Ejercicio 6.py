with open("datos.txt", "r") as leer:
    with open("copia.txt", "w") as escribir:
        escribir.write(leer.read())