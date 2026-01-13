'''
Ejercicio 2:
Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase
de personaje jugable. Partiendo que la estadistica base es 2, debes cumplir las siguientes
condiciones:
    ● El caballerpo tiene el doble de vida y defensa que un guerrero.
    ● El guerrero tiene el doble de ataque y alcance que un caballero.
    ● El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance
    ● Muestra como quedan las propiedades de los 3 personajes
'''
base = 2

clases = {
    "Caballero": {},
    "Guerrero": {
        "Vida": base,
        "Defensa": base,
        "Ataque": base,
        "Alcance": base
    },
    "Arquero": {}
}

clases["Caballero"] = {
    "Vida": clases["Guerrero"]["Vida"] * 2,
    "Defensa": clases["Guerrero"]["Defensa"] * 2,
    "Ataque": clases["Guerrero"]["Ataque"] / 2,
    "Alcance": clases["Guerrero"]["Alcance"] / 2
}

clases["Arquero"] = {
    "Vida": clases["Guerrero"]["Vida"],
    "Defensa": clases["Guerrero"]["Defensa"] / 2,
    "Ataque": clases["Guerrero"]["Ataque"],
    "Alcance": clases["Guerrero"]["Alcance"] * 2
}

for personaje, estadisticas in clases.items():
    print(personaje)
    for tipo, numero in estadisticas.items():
        print("\t" + tipo, numero)