# Solicita al usuario un número
numero = int(input("Ingrese un número: "))

# Inicializa un contador
contador = 1

# Usa un bucle while para mostrar la tabla de potencias
while contador <= 10:
    resultado = numero ** contador
    print(f"{numero} elevado a la {contador} es igual a {resultado}")
    contador += 1