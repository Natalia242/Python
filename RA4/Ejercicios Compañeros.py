import unicodedata

x = 3

match x:
    case 0:
        '''
        Ejercicio Natalia:
        Escribe un programa en Python que solicite al usuario una cadena de
        texto y, posteriormente, una palabra a buscar dentro de esa cadena.
        El programa deberá comprobar si la palabra aparece en el texto.

        Si la palabra se encuentra, el programa debe imprimir el texto original
        pero eliminando únicamente la primera aparición de esa palabra.

        Si la palabra no se encuentra en la cadena:
	        El programa debe eliminar alguna palabra existente de la cadena (puede ser la primera, la última o 	cualquier otra, según prefieras diseñarlo).
	        Luego debe mostrar la cadena, sin nada delante de esa palabra.

        Finalmente, debe mostrar ambas cadenas resultantes.

        Luego imprime por pantalla a partir de la segunda palabra y solo las letras pares.
            (ejemplo:   "trigal."
                        Imprimiría: rgl
                        "Pablito un clavito."
                        Imprimiría: u lvt.)
        '''
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
    case 1:
        import itertools

        def calcular_distancia(ciudades, distancias):
            """ Calcula la distancia total de un recorrido """
            distancia_total = 0
            for i in range(len(ciudades) - 1):
                distancia_total += distancias[ciudades[i]][ciudades[i + 1]]
            # Añadimos la distancia de regreso al punto de inicio
            distancia_total += distancias[ciudades[-1]][ciudades[0]]
            return distancia_total


        def tsp_fuerza_bruta(distancias):
            """ Resuelve el TSP con fuerza bruta """
            n = len(distancias)
            ciudades = list(range(n))  # Generamos una lista de ciudades numeradas
            min_distancia = float('inf')
            mejor_recorrido = None

            # Generamos todas las permutaciones posibles de las ciudades
            for perm in itertools.permutations(ciudades):
                # Calculamos la distancia total del recorrido
                distancia = calcular_distancia(perm, distancias)
                # Si encontramos una ruta más corta, la guardamos
                if distancia < min_distancia:
                    min_distancia = distancia
                    mejor_recorrido = perm

            return mejor_recorrido, min_distancia


        # Ejemplo de uso:
        # Matriz de distancias entre ciudades (simétrica, donde la distancia de i a j es la misma que de j a i)
        distancias = [
            [0, 10, 15, 20, 25],
            [10, 0, 35, 25, 30],
            [15, 35, 0, 30, 5],
            [20, 25, 30, 0, 15],
            [25, 30, 5, 15, 0]
        ]

        mejor_recorrido, min_distancia = tsp_fuerza_bruta(distancias)
        print(f"Mejor recorrido: {mejor_recorrido}")
        print(f"Distancia mínima: {min_distancia}")
    case 2:
        '''
        Ejercicio(Jojo): Hacer una función a la que se le introduce
        strings y devuelve una cadena con los datos introducidos usando .format()
        '''


        def jojo(nombre, calificacion, asignatura):
            frase = "{name} va a sacar un {nota} en {asignatura}"
            return frase.format(name=nombre, nota=calificacion, asignatura=asignatura)


        nombre = input("Introduce el nombre: ")
        calificacion = input("Introduce la calificacion: ")
        asignatura = input("Introduce la asignatura: ")

        print(jojo("Natalia", 10, "Python"))
    case 3:
        '''
        Ejercicio 8 (Diego Scott): Dado un array de correos introduce
        en una lista los nombres de los correos siguientes:
        correos =[ "barack.obama@nagger.com", "angela.merkel@pretzel.com",
        "emmanuel.macron@gabacho.com", "justin.trudeau@pokemon.com",
        "gorgefluidos@air.lkc" ]

        Para eso crearás el método:  correos_nombres(lista_correos)
        '''


        def correos_nombres(lista_correos):
            nombres = []
            dominios = []

            for correo in lista_correos:
                nombres.append(correo[:correo.find("@")])
                dominios.append(correo[correo.find("@")+1:])

            print(nombres)
            print(dominios)


        correos = ["barack.obama@nagger.com",
                   "angela.merkel@pretzel.com",
                   "emmanuel.macron@gabacho.com",
                   "justin.trudeau@pokemon.com",
                   "gorgefluidos@air.lkc"]

        correos_nombres(correos)
    case 4:
        '''
        Invertir las palabras que tengan más de 5 letras (Mario Sáez)
        '''
        frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"

        for palabra in frase.split():
            if len(palabra) > 5:
                print(palabra[::-1], end=" ")
            else:
                print(palabra, end=" ")
    case 5:
        '''
        Ejercicio (Tobias) {
        # Haz un metodo que reemplace cada palabra con la primera
        letra en mayuscula y cuenta cuantas ‘e’ hay.
        # frase = "Tres tristes tigres, tragaban trigo en un trigal,
        en tres tristes trastos, tragaban trigo tres tristes tigres"}
        '''


        def primeraMayuscula(frase):
            for palabra in frase.split():
                print(palabra.capitalize(), end=" ")


        def contarE(frase):
            cont = 0
            for letra in frase:
                if letra in "e": cont += 1
            return cont


        frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"

        primeraMayuscula(frase)
        print("Hay", contarE(frase), "e")
    case 6:
        '''
        Ejercicio(Javier Jaén) Anagrama
        Ejercicio(Daniel Lillo) Comprueba que una cadena sea un anagrama. Debes tener en cuenta mayúsculas y espacios.
        '''
        def anagrama(a, b):
            a = a.replace(' ', '').lower()
            b = b.replace(' ', '').lower()

            a = unicodedata.normalize('NFD', a)
            a = a.encode('ascii', 'ignore')

            b = unicodedata.normalize('NFD', b)
            b = b.encode('ascii', 'ignore')

            return sorted(a) == sorted(b)

        a = "Tom Marvolo Riddle"
        b = "I am Lord Voldemort"

        if anagrama(a, b):
            print("BIEN")
        else:
            print("MAL")
    case 7:
        '''
        Ejercicio (Ricardo)
        Pedir al usuario una frase y que se muestre la frase en minúsculas, mayúsculas, el numero
        de palabras que tiene, las palabras en orden inverso y la cantidad de veces que aparece la letra “a”.
        '''
        # frase = input("Ingrese una frase: ")
        frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"

        e = 0

        print(frase.lower())
        print(frase.upper())
        print(len(frase.split()))

        for palabra in frase.split():
            print(palabra[::-1], end=' ')

        print()

        for i in range(len(frase.split()), 0, -1):
            lista = frase.split()
            print(lista[i - 1], end=' ')

        for letra in frase:
            if letra in "a": e += 1

        print()
        print(e)
    case 8:
        '''
        Ejercicio (Ignacio)
        Desarrolla un sistema de login sencillo. El programa deberá pedir por teclado un nombre
        de usuario y una contraseña. Ambos valores se convertirán a minúsculas y se guardarán
        concatenados en una única cadena, separados por un carácter especial (por ejemplo, :).

        Después, implementa un método llamado unirCredenciales(), que reciba dos cadenas:
        un nombre de usuario y una contraseña. El método deberá unirlas del mismo modo
        (en minúsculas y separadas por “:” ) y compararlas con la cadena almacenada inicialmente.

        El método debe devolver:
        "Sesión iniciada" → si las credenciales coinciden exactamente.
        "Credenciales inválidas" → si no coinciden.
        '''


        def unirCredenciales(cadena1, cadena2):
            cadenaUnida = cadena1.lower() + ":" + cadena2.lower()
            return "Sesión iniciada" if cadenaUnida == cadena else "Credenciales inválidas"


        nombre = input("Ingrese su nombre de usuario: ")
        contrasenna = input("Ingrese su contraseña: ")

        cadena = nombre.lower() + ":" + contrasenna.lower()

        print(unirCredenciales("natalia", "1234"))
    case 9:
        '''
        Ejercicio(Francisco Fernández):
        En el programa el usuario debe introducir un nombre y que quiere hacer
        con ello, las opciones son: "Poner el nombre el primero de una lista",
        "Buscar si la lista contiene el nombre y devolver su posición", "Añadirlo
        de la lista" y "Contar cuantas veces sale el nombre en la lista".
        '''
        cont = 0
        lista = ["Pepe", "Juan", "Natalia", "Pablo"]
        nombre = input("Ingrese su nombre: ")

        opcion = input("""Opciones:
            \t1) Poner el nombre el primero de una lista
            \t2) Buscar si la lista contiene el nombre y devolver su posición
            \t3) Añadirlo de la lista
            \t4) Contar cuantas veces sale el nombre en la lista
            """)

        match opcion:
            case "1":
                lista.insert(0, nombre)
                print(lista)
            case "2":
                print("Posición (0-X):", lista.index(nombre))
            case "3":
                lista.append(nombre)
                print(lista)
            case "4":
                for i in lista:
                    if nombre == i:
                        cont += 1
                print("Cantidad de veces que sale el nombre:", cont)
            case _:
                print("Opcion invalida")
    case 10:
        '''
        Ejercicio(Bryan): Crear una función que cuente las vocales de una cadena
        '''


        def contarVocales(cadena):
            cont = 0
            for letra in cadena.lower():
                if letra in "aeiou": cont += 1
            return cont


        cadena = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"
        print(contarVocales(cadena))
    case 11:
        '''
        (Ejer Jaime) Buscar una letra, en una cadena cualquiera pedida por teclado y pasarla a mayúscula
        '''
        cadena = input("Introduce una cadena: ")
        letra = input("Introduce una letra: ")

        cadena = cadena.replace(letra.lower(), letra.upper())
        print(cadena)
    case 12:
        '''
        Ejercicio(Oscar Pérez): Crea una función que al pasarle una frase
        cuente el numero de vocales que tiene en total y que pregunte por
        que otra vocal quiere cambiar todas las vocales de la frase, que
        retorne la frase cambiada y el numero de vocales de la frase antes de cambiarlas.
        '''


        def vocales(frase):
            cont = 0
            vocal = "x"

            while vocal not in "aeiou":
                vocal = input("¿Por qué vocal quieres cambiar las vocales?: ")

            for letra in frase:
                if letra in "aeiou": cont += 1

            for letra in frase:
                if letra in "aeiouAEIOUáéíóúÁÉÍÓÚ":
                    frase = frase.replace(letra, vocal)

            #return cont, frase
            return f"Hay {cont} vocales\n{frase}"


        frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"
        print(vocales(frase))
        #vocales, fraseCambiada = vocales(frase)

        #print("Hay", vocales, "vocales")
        #print(fraseCambiada)
    case 13:
        '''
        Ejercicio(Mohamed Achouragh):
        Crear una función que reciba una frase y cuente cuántas palabras tiene en total.
        Guarde todas las palabras en una lista. Pregunte al usuario por una palabra de
        la frase que quiera reemplazar y por la nueva palabra que desea poner en su lugar.
        Retorne la lista de palabras modificada y el número de palabras que tenía la frase
        antes del cambio.
        '''


        def palabras(frase):
            palabras = frase.split(" ")
            cantPalabras = len(palabras)
            palabraReemplazar = input("Introduce la palabra a reemplazar: ")
            palabraNueva = input("Introduce la palabra nueva a reemplazar: ")
            frase = frase.replace(palabraReemplazar, palabraNueva)
            return cantPalabras, frase.split()


        frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"

        cant, lista = palabras(frase)
        print("Había", cant, "palabras")
        print(lista)
    case 14:
        '''
        Palindromos
        '''
        def esPalindromo(palindromo):
            '''
            palindromo = (palindromo.replace(' ', '').lower()
                          .replace("á", "a")
                          .replace("é", "e")
                          .replace("í", "i")
                          .replace("ó", "o")
                          .replace("ú", "u"))
            '''
            palindromo = palindromo.replace(' ', '').lower()
            palindromo = unicodedata.normalize('NFD', palindromo)
            palindromo = palindromo.encode('ascii', 'ignore')
            return palindromo == palindromo[::-1]

        palindromo = "Dábale arroz a la zorra el abad"
        #palindromo = "Anita lava la tina"
        #palindromo = "Somos o no somos"
        #palindromo = "La ruta natural"

        if esPalindromo(palindromo):
            print("BIEN")
        else:
            print("MAL")
    case _:
        frase = "Pablito clavito"
        print(frase[::2])