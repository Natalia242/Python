try:
    diccionario = dict()
    with open("datos.txt", encoding="utf-8") as leer:
        texto = leer.read()
        for palabra in texto.split():
            diccionario[palabra.lower()] = texto.count(palabra.lower())

    for palabra, frecuencia in diccionario.items():
        print(palabra + ":", frecuencia)
except FileNotFoundError:
    print("El fichero no existe")