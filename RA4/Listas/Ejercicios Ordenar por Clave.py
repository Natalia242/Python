'''
Ejercicio que ordene una lista según una clave:
    Se dispone de una lista de números enteros llamada lista.

    lista = [60, 3, 12, 7, 55]

    Se pide escribir un programa en Python que ordene la lista
    utilizando una función personalizada como clave de ordenamiento,
    cumpliendo las siguientes reglas:
        Si el número es par, su valor de comparación será la mitad del número.
        Si el número es impar, su valor de comparación será el doble del número.

    Consigna:
    Define una función que reciba un número entero y devuelva el valor que se usará como criterio para ordenar.
    Utiliza dicha función como argumento key del método_ sort() para ordenar la lista.
    Muestra la lista ordenada por pantalla.

    Nota: El ordenamiento debe basarse únicamente en el valor devuelto por la función clave, no en el valor original del número.
'''

def ordenar(n):
    if n % 2 == 0:
        return n / 2
    else:
        return n * 2

lista = [60, 3, 12, 7, 55]

lista.sort(key = ordenar)
print(lista)

'''
Ejercicio Ignacio:
    Tienes una lista de productos.
    Cada producto es una tupla con esta estructura:
    
    (nombre, precio, stock)
    
    Datos iniciales:
    productos = [
        ("Portatil", 1200, 5),
        ("Raton", 25, 50),
        ("Teclado", 80, 2),
        ("Monitor", 300, 10),
        ("USB", 10, 100)
    ]
    
    1. Ordena los productos por precio (de menor a mayor).
    2. Ordena los productos por stock (de mayor a menor).
    3. Ordena los productos por nombre alfabéticamente.
    
    Pista: puedes usar lambda o itemgetter en el key
'''

productos = [
    ("Portatil", 1200, 5),
    ("Raton", 25, 50),
    ("Teclado", 80, 2),
    ("Monitor", 300, 10),
    ("USB", 10, 100)
]

productos.sort(key = lambda x: x[1])
print(productos)
productos.sort(key = lambda x: x[2], reverse = True)
print(productos)
productos.sort(key = lambda x: x[0])
print(productos)

'''
Otro ejercicio con diccionarios:
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "promedio": 8.5},
        {"nombre": "Luis", "edad": 22, "promedio": 7.2},
        {"nombre": "María", "edad": 19, "promedio": 9.1},
        {"nombre": "Pedro", "edad": 21, "promedio": 8.0}
    ]
    
    estudiantes.sort(key = lambda x: x["edad"], reverse = True)
    print(estudiantes)
'''