# Inicializa variables para almacenar el número mayor y menor
numero_mayor = None
numero_menor = None

# Solicita al usuario que ingrese los números
print("Ingrese una lista de números. Para finalizar, ingrese 'fin'.")
while True:
    entrada = input("Ingrese un número (o 'fin' para finalizar): ")
    
    if entrada.lower() == 'fin':
        break
    
    try:
        numero = float(entrada)
        if numero_mayor is None or numero > numero_mayor:
            numero_mayor = numero
        if numero_menor is None or numero < numero_menor:
            numero_menor = numero
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

# Verifica si se ingresaron números
if numero_mayor is not None and numero_menor is not None:
    print(f"El número mayor es: {numero_mayor}")
    print(f"El número menor es: {numero_menor}")
else:
    print("No se ingresaron números.")
