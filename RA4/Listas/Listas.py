cadena = "navidad"
#cadena[2] = 'o' # No se puede modificar.

lista = [1, "feliz", "feliz", "navidad", 4.6, [33,66]] # Está ordenada por orden de inserción.
print(lista) # No se puede ordenar al tener int y strings.

lista[2] = "2026" # Se puede modificar el valor en una posición de la lista.
print(lista)

print(list(range(2, 20, 2))) # Crea una nueva lista directamente que incluya los números de ese rango.
line = "Hay muchos          espacios."
cont = 0
for i in line:
    if i == " ":
        cont += 1
    elif cont > 1 and cont % 2 == 0:
        line = line.replace("   ", "")
    elif cont > 1 and cont % 2 == 1:
        line = line.replace("  ", "")
    else:
        cont = 0

print(line)