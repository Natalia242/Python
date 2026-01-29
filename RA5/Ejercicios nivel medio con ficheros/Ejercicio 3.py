try:
    palabra = input("Ingrese la palabra clave: ").lower()
    with open("datos.txt", encoding="utf-8") as fichero:
        lineas = fichero.readlines()
        for linea in lineas:
            if palabra in linea.lower():
                print(linea, end="")
except FileNotFoundError:
    print("El fichero no existe")