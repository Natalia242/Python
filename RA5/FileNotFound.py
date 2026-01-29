try:
    with open("datos.txt", "r") as fichero:
        print(fichero.read())
except FileNotFoundError:
    print("El fichero no existe")