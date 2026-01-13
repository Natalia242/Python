'''
Ejercicio 1: Crea una función calcular_estadisticas(numeros) que reciba una lista de
números y devuelva una tupla con:
● El valor mínimo.
● El valor máximo.
● La media aritmética.
'''
def calcular_estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)
'''
Ejercicio 2: Crea una función distancia(p1, p2) que reciba dos tuplas representando
puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula:
'''
def distancia(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
'''
Ejercicio 3: Crea una función analizar_texto(texto) que devuelva una tupla con:
● Número total de caracteres.
● Número de palabras.
● Primera palabra del texto.
'''
def analizar_texto(texto):
    return len(texto), len(texto.split()), texto.split()[0]
'''
Ejercicio 4: Crea una función convertir_temperatura(celsius) que reciba una
temperatura en grados Celsius y devuelva una tupla con:
● La temperatura en Fahrenheit.
● La temperatura en Kelvin.
'''
def convertir_temperatura(celsius):
    return (celsius * 9 / 5) + 32, (celsius + 273.15)
'''
Ejercicio 5: Crea una función analizar_numeros(numeros) que reciba una lista de
enteros y devuelva una tupla con:
● El número de elementos pares.
● El número de elementos impares.
● La suma total.
'''
def analizar_numeros(numeros):
    pares, impares = 0, 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares, sum(numeros)
'''
Ejercicio 6: Crea una función procesar_cadena(cadena) que devuelva una tupla con:
● La cadena en mayúsculas.
● La cadena en minúsculas.
● La longitud de la cadena.
'''
def procesar_cadena(cadena):
    return cadena.upper(), cadena.lower(), len(cadena)

print(calcular_estadisticas((1,2,3,4,5,6,7,8,9,10)))
print(distancia((1, 2), (4, 6)))
print(analizar_texto("Hola y adios"))
print(convertir_temperatura(5))
print(analizar_numeros((1,2,3,4,5,6,7,8,9,10)))
print(procesar_cadena("Hola y adios"))