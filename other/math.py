import math

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Función para calcular la potencia
def potencia(base, exponente):
    return base ** exponente

# Función para calcular la raíz cuadrada
def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: Raíz cuadrada de un número negativo"
    return math.sqrt(numero)

def main():
    print("Calculadora Básica")

    # Solicitar los números al usuario
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    # Realizar cálculos
    print(f"{num1} + {num2} = {sumar(num1, num2)}")
    print(f"{num1} - {num2} = {restar(num1, num2)}")
    print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    print(f"{num1} / {num2} = {dividir(num1, num2)}")
    print(f"{num1} ^ {num2} = {potencia(num1, num2)}")
    print(f"Raíz cuadrada de {num1} = {raiz_cuadrada(num1)}")
    print(f"Raíz cuadrada de {num2} = {raiz_cuadrada(num2)}")
