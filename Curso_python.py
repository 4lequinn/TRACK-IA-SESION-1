#//EXTRA//
#0)Instalación VSCODE, Python 3.8 o Anaconda. EXPLICACIÓN
#https://www.python.org/downloads/
#https://code.visualstudio.com
#https://docs.conda.io/en/latest/miniconda.html
#https://www.anaconda.com


#///CONTENIDOS///
#1)Tipos de datos
#2)Instanciar variables
#3)Operar variables
#4)Capturar datos, imprimir datos, concatenar datos
#5)Validaciones
#6)Operadores lógicos, aritméticos, identidad etc
#7)Ciclos for y while
#8)Try catch, control de errores
#9)Listas y métodos de listas (append, remove, pop, index, count, etc)
#10)Diccionarios
#11)Métodos y uso de métodos/funciones
#12)Importar archivo de funciones y so
#13)Instalar librerias en python (puede ser mediante anaconda o directo en la versión de python/cmd)
#14)Importar librerias
#15)Trabajar con comandos de librerias, numpy(matrices/arreglos, rand, mean, sqrt), statistics, math, pandas, etc.















#12, 14) Importar archivo funciones, so y librerias
import os
import numpy as np
import statistics as stats
import pandas as pd
import math as mt
import random as rd
import funciones as fn
os.system("cls")




#1 y 2) Tipos de datos: string, double/float, int, boolean, char.
VarString = "Soy Texto"
VarFlotante = 4.5 #Soy flotante/decimal
VarInt = 1 #Soy un número entero
VarBooleanT = True #Soy un boolean Verdadero
VarBooleanF = False #Soy un boolean Falso
VarChar = "F" #Soy un caracter 


#3 y 4) Operar variables, capturar datos, imprimir datos, concatenar datos.
num1 = 35
num2 = 9
suma = num1+num2
resta = num1-num2
multipli = num1*num2
division = num1/num2
potencia = num1**num2
restodiv = num1%num2
raizcuadradan1 = (num1**(0.5))
raizcuadradan2 = (num2**(0.5))
ordenarOperacion = (    (   (  (suma/resta) *   (num1**restodiv) )+raizcuadradan1)**(0.5)   )
#impresión
print(" (1) Suma")
print(suma)
input()
print(" (2) Resta")
print(resta)
input()
print(" (3) Multiplicación")
print(multipli)
input()
print(" (4) División")
print(division)
input()
print(" (5) Potencia")
print(potencia)
input()
print(" (6) Resto división")
print(restodiv)
input()
print(" (7) Raíz primer número")
print(raizcuadradan1)
input()
print(" (8) Raíz segundo número")
print(raizcuadradan2)
input()
print(" (9) Operación y orden")
print(ordenarOperacion)
input()
#Capturar datos y concatenar
input("Escribe: ") #capturo un dato
Texto = input() #capturo un dato y se lo asigno a variable texto
print(Texto)
Nombre = input("Ingrese su nombre: ") #Agrego caracteres dentro del método input
print('Su nombre es ', Nombre) #Forma 1 de concatenar valores, usando la <<,>>.
print('Hola Sr ', Nombre, ' ¿Desea aprender python?') #Forma 1 de concatenar valores, usando la <<,>>.
print(f'Hola Sr {Nombre} esta es la segunda forma de concatenamiento en python.') #Forma 2 de concatenar valores, usando la estructura (f'text {variable} text')
NumEnt = int(input("Ingrese un entero: "))
NumFloat = float(input("Ingrese un decimal: "))
print(f'El número entero es: {NumEnt} y el número decimal es: {NumFloat}')

#5) Validaciones if, elif, else.
validador = int(input("Ingrese un número del 1 al 3 entero: "))
if (validador==1):
    print("Su número es mayor que 0 y menor que 2.")
elif(validador==2):
    print("Su número es mayor que 1 y menor que 3.")
elif(validador==3):
    print("Su número es mayor que 2 y menor que 4.")
else:
    print("Su número no está entre 1 y 3.")

input()
parimpar = int(input("Ingrese un número entero: "))
if(parimpar%2==0):
    print(f'El número {parimpar} es par.')
else:
    print(f'El número {parimpar} es impar.')

#6) Operadores básicos de python.
#https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/

#7) Ciclos for y while
#ciclo for: recorrer o parar hasta llegar al límite.
input()
print("Ciclo for: Empieza en 0, llega hasta 20, y va de uno en uno, imprimimos el indice(i)")
for i in range(0,20,1):
    print(i)

input()
print("Ciclo for: Usando variables y validaciones.")
varlimite = 100
varsubida = 5
for indice in range(0, varlimite, varsubida): #empieza en 0, tiene que llegar a 100 y va aumentando de 5 en 5.
    print(f'Tenemos que llegar hasta {varlimite} y vamos en {indice}. \n')
    decision = int(input("¿Deseas abrir otro for? 1(si)/2(no): \n"))
    if(decision == 1):
        limite = int(input("Ingrese nuevo límite: "))
        comienzo = int(input("Ingrese dónde empieza: \n"))
        if(comienzo<limite):
            for x in range(comienzo, limite, 1):
                print(f"El for nuevo va en: {x}")
        else:
            print("Debes poner un inicio menor al límite.\n")
    else:
        print("Okey no abriremos otro for...\n")
#ciclo while: hasta que la condición no se cumpla.
input()
print("Ciclo while: Mientras que algo suceda se ejecutará.")
varmientras = 0
while varmientras == 0:
    print("Quiero detenerme!!")
    detencion = int(input("¿Me dejas detenerme? 1(si)/2(no): "))
    if(detencion == 1):
        print("Gracias por dejar detenerme. :)")
        varmientras = 1 #se deja cumplir la condición del <<mientras>> por lo tanto se cierra el ciclo
    else:
        print("Noooo!!")
input()
varmientras = True
while varmientras == True:
    print("Quiero detenerme!!")
    detencion = int(input("¿Me dejas detenerme? 1(si)/2(no): "))
    if(detencion == 1):
        print("Gracias por dejar detenerme. :)")
        varmientras = False #se deja cumplir la condición del <<mientras>> por lo tanto se cierra el ciclo
    else:
        print("Noooo!!")
input()
varmientras = True        
while varmientras == True:
    print("Quiero detenerme!!")
    detencion = int(input("¿Me dejas detenerme? 1(si)/2(no): "))
    if(detencion == 1):
        print("Gracias por dejar detenerme. :)")
        break #Los ciclos también se pueden cerrar con la palabra reservada break
    else:
        print("Noooo!!")
input()
#8) Control de errores: Try Catch
print("Control de errores Try Catch:")
while VarBooleanF == False:
    try:
        VarInt = int(input("Ingrese un número: "))
        if(VarInt == 1):
            print("Listo.")
            VarBooleanF = True
        else:
            print("Otra vez.")
    except:
        print("Caracter inválido, inténtelo otra vez.")

#9) Listas en python, y sus métodos
#crear listas
input()
listanumeros = [1, 2, 3, 4, 5, 6, 7, 8]
listatextos = ['Dexter','Gotham','Breaking Bad','Arrow','Lucifer']
listaproductos = ['Tetera', 'Hervidor', 'Cocina', 'Plancha', 'Lavadora', 'Olla Presión', 'Cucharón', 'Cuchillo carnicero', 'Lavaloza', 'Esponja']
#imprimir posiciones/indices de listas
print('Pocisión 3 lista números: ',listanumeros[3])
input()
print('Pocisión 2 lista textos: ',listatextos[2])
#ciclar lista con for
input()
print("//Ciclar lista con for//")
for indice in range(0, len(listanumeros), 1):
    print(listanumeros[indice])
#ciclar lista con while
input()
print("//Ciclar lista con while//")
indice = 0
while (indice < len(listanumeros)):        
    print(listanumeros[indice])
    indice = indice+1
#usando métodos básicos de listas de python
#pd también se pueden agregar elementos a listas vacias: 
# ListaVacia = []
# ListaVacia.append("algo") 
print("Append:")
listatextos.append("Flash")
print(listatextos)
input()
print("Pop:")
listatextos.pop()
print(listatextos)
input()
print("Extend:")
listatextos.extend("Flash")
print(listatextos)
input()
print("Remove:")
listatextos.remove("Arrow")
print(listatextos)
input()
print("Index:")
print(listatextos.index("Breaking Bad"))
input()
print("Count:")
print(listatextos.count("Arrow"))
input()
print("Reverse:")
listatextos.reverse()
print(listatextos)
input()
print("Min:")
print(min(listanumeros))
input()
print("Max:")
print(max(listanumeros))
input()
#ejemplo práctico con listas:
vTrue= True
while(vTrue==True):
    try:
        print("Ingrese una opción: ")
        print("1)Ingresar producto")
        print("2)Ver productos")
        print("3)Salir.")
        try:
            decision = int(input("Opción: "))
            if decision==1: 
                nuevoproducto = input("Ingrese nuevo producto: ")
                listaproductos.append(nuevoproducto)    
            elif decision==2:
                vFalse = False
                while vFalse == False:
                    try:
                        print("Ingrese una opción: ")
                        print("1)Ver producto")
                        print("2)Salir")
                        des1 = int(input("Opción: "))
                        if des1 == 1:
                            busqueda = input("Ingrese el nombre del producto que busca: ")
                            for x in range(0, len(listaproductos), 1):
                                if listaproductos[x]==busqueda:
                                    print(f"Se ha encontrado el producto que busca: {listaproductos[x]} y cuesta tanto...")
                                    break
                                elif (x<len(listaproductos)):
                                    print("Buscando en la bd...")
                                elif (listaproductos[x]!=listaproductos[-1]):
                                    print("No se encontró su producto.")
                        elif des1 == 2:
                            print("Volviendo al menú anterior...")
                            vFalse = True
                        else:
                            print("Ingresa opción válida.")
                    except:
                        print("Ingresa caracter válido.")
            else: 
                vTrue= False
        except:
            print("Ingresa caracter válido.")
    except:
        print('Antes debes ingresar alguna cosa en la lista vacia.')
input()
#10) Diccionario 
# Diccionario de teléfonos
#llaves: nombres de personas (string)
#valores: números de teléfono asociados a cada nombre (int)
print("Seleccionando un elemento del diccionario: ")
telefonos = {'Jaimito':5551428, 'Yayita': 5550012, 'Pepito':5552437}
#mostrar por pantalla el telefono de Pepito
print(telefonos['Pepito'])
input()
#Se pueden crear diccionarios vacios
print("Diccionarios vacios: ")
dicc1 = {} 
dicc2 = dict()
print(dicc1)
print(dicc2)
input()
patas = {'humano': 2, 'pulpo': 8, 'perro': 5, 'gato': 4}
print("Diccionario antes de agregar un valor: ")
print(patas)
input()
patas['cienpies'] = 100
print("Diccionario despues de agregar un valor: ")
print(patas)
input()
#Los perros en realidad tienen cuatro patas, cambiar valor en el diccionario
patas["perro"] = 4
print("Diccionario despues de cambiar un valor: ")
print(patas)
input()
patas =  {'cienpies': 100, 'humano': 2, 'gato': 4, 'pulpo': 8, 'perro': 4}
print("Diccionario antes de eliminar un elemento: ")
print(patas)
input()
#Eliminando el elemento del diccionario
del patas["pulpo"]
print("Diccionario despues de eliminar un elemento: ")
print(patas)
input()
patas =  {'cienpies': 100, 'humano': 2, 'gato': 4, 'pulpo': 8, 'perro': 4}
#Accediendo y mostrando por pantalla la cantidad de patas de un gato
print("El gato tiene ",patas['gato']," patas.")
input()
 
#11) Uso de funciones, de forma directa en el archivo y usando funciones importadas. /return.
#función sin parámetro local
def funcion_sin():
    V = True
    while V == True:
        try:
            print("Hola, soy una función sin parámetros.")
            num1 = float(input("Ingrese un número: "))
            num2 = float(input("Ingrese otro número: "))
            suma = num1 + num2
            V = False
        except:
            print("Son números, no caracteres.")
    return(suma)
#función con parámetro local
def funcion_con(n1, n2):
    print("Hola, soy una función con parámetros.")
    suma = n1 + n2
    return(suma)

#Llamar funciones locales:

#Sin parámetro:
valor_retornado = funcion_sin() #el valor se guardo en valor_retornado.
print(f"El resultado de la suma de la f sin parámetros es: {valor_retornado}")
#Con parámetro:
input()
V = True
while V == True:
    try:
            num1 = float(input("Ingrese un número: "))
            num2 = float(input("Ingrese otro número: "))
            valor_retornado_c = funcion_con(num1, num2)
            print(f"El resultado de la suma de la f con parámetros es: {valor_retornado_c}") 
            V = False
    except:
            print("Son números, no caracteres.")

#Llamar funciones externas:

#Sin parámetro ext:
input()
valor_retornado_ext = fn.funcion_ext_sin() #el valor se guardo en valor_retornado.
print(f"El resultado de la suma de la f sin parámetros es: {valor_retornado_ext}")
#Con parámetro ext:
input()
V = True
while V == True:
    try:
            num1 = float(input("Ingrese un número: "))
            num2 = float(input("Ingrese otro número: "))
            valor_retornado_ext_c = fn.funcion_ext_con(num1, num2)
            print(f"El resultado de la suma de la f con parámetros es: {valor_retornado_ext_c}") 
            V = False
    except:
            print("Son números, no caracteres.")



#13) Instalación de librerias / USO DE CMD para instalar, o instalación directa a través de anaconda
#EJEMPLOS DE LIBRERIAS EXISTENTES : https://www.crehana.com/ec/blog/desarrollo-web/librerias-python/
#instalación de numpy, 
#pip install numpy
#instalación de statistics,
#pip install statistics
#instalación módulo de matemáticas,
#pip install python-math
#instalación de pandas
#pip install pandas

#15) Trabajando con librerías, comandos de funciones.

#math
#obtener pi
numero_pi = mt.pi
print("Soy número pi: ",numero_pi)
#número de euler
numero_euler = mt.e
print("Soy número de Euler: ",numero_euler)
#factorial de un número
print(f"Soy factorial del número 6: {mt.factorial(6)}")

#random
#obtener número random
numero_random = rd.randint(0, 100)
print("Soy un número random: ", numero_random)

#numpy
#raíz cuadrada de un número
numero = 340
print("Soy la raíz cuadrada de 340: ",np.sqrt(numero))
#promedio
numeros = [300, 200, 339, 301, 1000, 1, 3949, 10000, 1, 1, 13, 17, 900, 1, 5000]
print("Soy el promedio de la lista números: ", np.mean(numeros)) 


###### Documentación para ver las funciones de las librerias y poder ocuparlas: 
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://j2logo.com/python/generar-numeros-aleatorios-en-python/
# https://python-para-impacientes.blogspot.com/2016/10/calculo-estadistico.html#:~:text=La%20función%20mean()%20devuelve,entre%20el%20número%20de%20elementos.
# https://pythondiario.com/2019/01/matrices-en-python-y-numpy.html
# https://www.w3schools.com/python/module_math.asp
# https://docs.python.org/3/library/statistics.html
#####