try:
    with open("datos.txt", encoding="utf-8") as leer:
        print("El fichero tiene", len(leer.read().split()), "palabras")
except FileNotFoundError:
    print("El fichero no existe")