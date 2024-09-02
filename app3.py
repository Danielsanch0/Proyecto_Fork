def promedio_notas(alumnos):
    """
    Calcula el promedio de las notas de un diccionario de alumnos y notas.
    
    :param alumnos: Diccionario con nombres de alumnos como claves y notas como valores.
    :return: Promedio de las notas.
    """
    if not alumnos:  # Verifica si el diccionario está vacío y ya.
        return 0
    
    suma_notas = 0
    cantidad_alumnos = 0

    # Recorrer las notas del diccionario
    for nota in alumnos.values():
        suma_notas += nota
        cantidad_alumnos += 1

    # Calcular el promedio
    promedio = suma_notas / cantidad_alumnos
    return promedio

def alumno_con_mejor_nota(alumnos):
    """
    Encuentra el alumno con la nota más alta en un diccionario de alumnos y notas.
    
    :param alumnos: Diccionario con nombres de alumnos como claves y notas como valores.
    :return: Nombre del alumno con la nota más alta.
    """
    if not alumnos:  # Verifica si el diccionario está vacío
        return None
    
    mejor_alumno = None
    mejor_nota = -float('inf')  # Inicializa con la menor nota posible

    for nombre, nota in alumnos.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = nombre

    return mejor_alumno

def main():
    alumnos = {}

    while True:
        nombre = input("Ingresa el nombre del alumno (o escribe 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break

        try:
            nota = float(input(f"Ingresa la nota de {nombre}: "))
            if nota < 0 or nota > 100:
                print("La nota debe estar entre 0 y 100. Inténtalo de nuevo.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido para la nota.")
            continue

        alumnos[nombre] = nota

    # Mostrar el diccionario con todos los alumnos y sus notas
    print("\nLista de alumnos y sus notas:")
    for nombre, nota in alumnos.items():
        print(f"{nombre}: {nota:.2f}")

    # Llamada a la función promedio_notas y mostrar el resultado
    promedio = promedio_notas(alumnos)
    print(f"\nEl promedio de las notas es: {promedio:.2f}")

    # Llamada a la función alumno_con_mejor_nota y mostrar el resultado
    mejor_alumno = alumno_con_mejor_nota(alumnos)
    if mejor_alumno:
        print(f"\nEl alumno con la nota más alta es: {mejor_alumno} con una nota de {alumnos[mejor_alumno]:.2f}")
    else:
        print("\nNo se ingresaron alumnos.")

if __name__ == "__main__":
    main()



# Aqui va el ejercicio de buscar palabra 
def buscar_palabra(diccionario, palabra):
    """
    Busca una palabra en el diccionario y devuelve su definición.
    
    :param diccionario: Diccionario con palabras como claves y definiciones como valores.
    :param palabra: Palabra a buscar en el diccionario.
    :return: Definición de la palabra si está en el diccionario, de lo contrario un mensaje indicando que la palabra no se encontró.
    """
    return diccionario.get(palabra, "La palabra no se encontró en el diccionario.")

def main():
    diccionario = {}

    while True:
        palabra = input("Ingresa una palabra (o escribe 'salir' para terminar): ")
        if palabra.lower() == 'salir':
            break

        definicion = input(f"Ingresa la definición de tu {palabra}: ")
        diccionario[palabra] = definicion

    # Mostrar el diccionario completo
    print("\nDiccionario de palabras y definiciones:")
    for palabra, definicion in diccionario.items():
        print(f"{palabra}: {definicion}")

    while True:
        buscar = input("\nIngresa una palabra para buscar su definición (o escribe 'salir' para terminar la búsqueda): ")
        if buscar.lower() == 'salir':
            break

        resultado = buscar_palabra(diccionario, buscar)
        print(f"Definición de '{buscar}': {resultado}")

if __name__ == "__main__":
    main()
