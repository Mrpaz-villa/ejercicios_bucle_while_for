# Solicita al usuario un número
numero = int(input("Ingrese un número: "))

# Inicializa la suma
suma_pares = 0

# Inicializa un contador
contador = 1

# Usa un bucle while para encontrar los números pares y calcular la suma
while contador <= numero:
    if contador % 2 == 0:
        suma_pares += contador
    contador += 1

# Imprime la suma de los números pares
print(f"La suma de los números pares entre 1 y {numero} es: {suma_pares}")