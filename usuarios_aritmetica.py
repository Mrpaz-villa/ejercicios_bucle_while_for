# Solicita al usuario que ingrese una lista de números. Para finalizar, ingrese 'fin'.
print("Ingrese una lista de números para calcular la media aritmética.")
print("Cuando termine, escriba 'fin'.")
numeros = []
while True:
    entrada = input("Ingrese un número (o 'fin' para finalizar): ")
    
    if entrada.lower() == 'fin':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

# Calcula la media aritmética
if numeros:
    suma = sum(numeros)
    media = suma / len(numeros)
    print(f"La media aritmética de los números ingresados es: {media}")
else:
    print("No se ingresaron números para calcular la media.")