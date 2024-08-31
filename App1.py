print("Ejercicios de Listas con For en Python")

print("Sumar todos los elementos de una lista:")

def suma_elementos(lista):
    suma = 0 
    for numero in lista: 
        suma += numero  
    return suma  

numeros = [1, 2, 3, 4, 5]
resultado = suma_elementos(numeros)
print(resultado)  


print("Sumar todos los elementos de una lista:")

def contar_pares(lista):
    contador = 0  
    for numero in lista:  
        if numero % 2 == 0: 
            contador += 1 
    return contador 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = contar_pares(numeros)
print(resultado)

print("Encontrar el elemento más grande de una lista:")
 
def elemento_mas_grande(lista):
    if not lista:  
        return None  
    
    maximo = lista[0]  
    for numero in lista:  
        if numero > maximo:  
            maximo = numero  
    return maximo  


numeros = [3, 7, 2, 9, 5]
resultado = elemento_mas_grande(numeros)
print(resultado) 


print("Crear una nueva lista con los elementos de otra lista multiplicados por 2:")

def multiplicar_elementos(lista):
    nueva_lista = [] 
    for numero in lista:  
        nueva_lista.append(numero * 2) 
    return nueva_lista  #
numeros = [1, 2, 3, 4, 5]
resultado = multiplicar_elementos(numeros)
print(resultado)  


print("Invertir una lista:")

def invertir_lista(lista):
    lista_invertida = []  
    for i in range(len(lista) - 1, -1, -1):  
        lista_invertida.append(lista[i])  
    return lista_invertida  

numeros = [1, 2, 3, 4, 5]
resultado = invertir_lista(numeros)
print(resultado)  


