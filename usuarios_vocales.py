# Solicita al usuario una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Inicializa el contador de vocales
contador_vocales = 0

# Inicializa un índice para recorrer la cadena
indice = 0

# Define una lista de vocales en minúsculas y mayúsculas
vocales = "aeiouAEIOU"

# Usa un bucle while para contar las vocales en la cadena
while indice < len(cadena):
    if cadena[indice] in vocales:
        contador_vocales += 1
    indice += 1

# Imprime la cantidad de vocales en la cadena
print(f"La cadena contiene {contador_vocales} vocales.")