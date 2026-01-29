with open("nuevo.txt", "w") as fichero:
    print("Escribe una línea (o 'fin' para terminar): ")
    while True:
        linea = input()
        if linea.lower() == "fin":
            break
        fichero.write(linea + "\n")