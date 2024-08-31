# ejercicio 1
def eliminar_duplicados(lista):
    conjunto_sin_duplicados = set(lista)
    lista_sin_duplicados = list(conjunto_sin_duplicados)
    return lista_sin_duplicados

numeros = [1, 2, 3, 2, 4, 1, 5, 3]
resultado = eliminar_duplicados(numeros)
print("Lista sin duplicados:", resultado)

# ejerccio 2
import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7
adivinado = False

print("Estoy pensando en un número entre 1 y 100.")
while intentos < max_intentos and not adivinado:
    intento = int(input("Intenta adivinar el número: "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intentos.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número es mayor que", intento)
    else:
        print("El número es menor que", intento)

if not adivinado:
    print("Lo siento, no adivinaste el número en el número máximo de intentos.")
    print("El número secreto era", numero_secreto)

# ejerccio 3
cadena = input("Ingresa una frase: ")
i = 0
contador = 0
vocales = "aeiouAEIOU"

while i < len(cadena):
    if cadena[i] in vocales:
        contador += 1
    i += 1

print("La cadena tiene", contador, "vocales.")


# ejercicio 4
def calculadora():
    while True:
        
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        
        print("\nSelecciona una operación:")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Salir")
        opcion = input("Elige una opción (1/2/3/4/5): ")
        
        if opcion == '1' or opcion == '+':
            resultado = num1 + num2
            print(f"\nEl resultado de {num1} + {num2} es: {resultado}\n")
        elif opcion == '2' or opcion == '-':
            resultado = num1 - num2
            print(f"\nEl resultado de {num1} - {num2} es: {resultado}\n")
        elif opcion == '3' or opcion == '*':
            resultado = num1 * num2
            print(f"\nEl resultado de {num1} * {num2} es: {resultado}\n")
        elif opcion == '4' or opcion == '/':
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nEl resultado de {num1} / {num2} es: {resultado}\n")
            else:
                print("\nError: División por cero no permitida.\n")
        elif opcion == '5':
            print("Saliendo de la calculadora...")
            break 
        else:
            print("\nOpción no válida, por favor intenta de nuevo.\n")
calculadora()


# ejercicio 5
numeros_pares = []

contador = 1

while contador <= 100:
    if contador % 2 == 0:  
        numeros_pares.append(contador)  
    contador += 1  

print("Lista de números pares entre 1 y 100:", numeros_pares)
