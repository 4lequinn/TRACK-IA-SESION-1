#funciones externas
def funcion_ext_sin():
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

def funcion_ext_con(n1, n2):
    print("Hola, soy una función con parámetros.")
    suma = n1 + n2
    return(suma)