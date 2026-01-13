'''
Método al que se le pase un diccionario y se asegure de que python esté aprobada. Si es menor se pone un 5.
'''

estudiantes = {
    "estudiante1": {
        "nombre": "Natalia",
        "apellido": "Viñé",
        "modulos": {
            "Python": 4,
            "Acceso a Datos": 5,
            "Empresa": 6,
            "Sostenibilidad": 7,
            "PSP": 8,
            "Interfaces": 9,
            "SGE": 10,
            "Inglés": 9,
            "Programación Móvil": 8,
            "Digitalización": 7
        }
    },
    "estudiante2": {
        "nombre": "Ignacio",
        "apellido": "Sanz",
        "modulos": {
            "Python": 5,
            "Acceso a Datos": 5,
            "Sostenibilidad": 7,
            "PSP": 8,
            "Interfaces": 9,
            "SGE": 10,
            "Digitalización": 7
            }
    },
    "estudiante3": {
        "nombre": "Francisco",
        "apellido": "Fernandez",
        "modulos": {
            "Python": 4,
            "Acceso a Datos": 5,
            "Empresa": 6,
            "Sostenibilidad": 7,
            "PSP": 8,
            "Interfaces": 9,
            "SGE": 10,
            "Inglés": 9,
            "Programación Móvil": 8,
            "Digitalización": 7
        }
    },
    "estudiante4": {
        "nombre": "Ricardo",
        "apellido": "del Rio",
        "modulos": {
            "Python": 4,
            "Acceso a Datos": 5,
            "Sostenibilidad": 7,
            "PSP": 8,
            "Interfaces": 9,
            "SGE": 10,
            "Programación Móvil": 8,
            "Digitalización": 7
        }
    }
}

for clave, estudiante in estudiantes.items():
    print(clave)
    print(estudiante["nombre"], estudiante["apellido"], ":")
    for modulo, nota in estudiante["modulos"].items():
        print("\t" + modulo, ":", nota)