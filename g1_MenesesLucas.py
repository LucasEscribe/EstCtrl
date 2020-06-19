''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    Escribir un programa que pregunte el nombre del usuario en la consola 
    y después de que el usuario lo introduzca muestre por pantalla 
    <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
    mayúsculas y <n> es el número de letras que tienen el nombre.
'''
# Coloque la resolución del Ejercicio 1 debajo de esta línea

n = 0
nombre=str.upper(input("Escriba el nombre de usuario: "))

for i in nombre:
    n += 1

print(nombre, " tiene ", n ," letras")

'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    Escribir un programa que pida al usuario dos números, que luego 
    calcule y muestre por pantalla su división. 
    Si el divisor es cero el programa debe mostrar un error e imprimir 
    por pantalla el resultado e indicar si es par o impar.
'''
# Coloque la resolución del Ejercicio 2 debajo de esta línea

op1=(float(input("Introduce el divisor: ")))

op2=(float(input("Introduce el dividendo: ")))

if op2 <= 0:
    print("No se puede dividir entre cero. Intente de nuevo.")
    exit()

else:    
	print ("La división es: " + str(op1/op2))

# Otra resolución del Ejercicio 2:

try:
    op1=(float(input("Introduce el divisor: ")))
    op2=(float(input("Introduce el dividendo: ")))

    div=op1/op2
    print ("La división es: " + str(div))

    if int(div) % 2 == 0:
        print("Resultado de la división es PAR")
    else:
        print("Resultado de la división es IMPAR")

except ZeroDivisionError:

	print("No se puede dividir entre cero. Intente de nuevo.")

except ValueError:

	print("Debe ingresar sólo números. Intente de nuevo. ")	

except NameError:

	exit()

'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3: 
    Escribir un programa que pida al usuario un número entero 
    y muestre por pantalla un triángulo rectángulo como el de más abajo, 
    de altura el número introducido.

    *
    **
    ***
    ****
    *****
'''
# Coloque la resolución del Ejercicio 3 debajo de esta línea

altoTriangulo=(int(input("Introduce un número: ")))
asterisco = ""

for i in range(altoTriangulo):
    asterisco = asterisco + " *"
    print(asterisco)
    

'''
    -----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Dados los datos de un municipio: zona, sexo y edad de cada uno de 
    sus habitantes, encontrar:
    a) porcentaje de varones menores de 15 años para cada zona
    b) porcentaje de varones menores de 15 años para todo el municipio
    A su vez debera imprimir además del porcentaje mencionado arriba, 
    la cantidad de varones menores de 15 años total de toda la zona y del municipio.
    Los datos vienen ordenados por zona.Con dato de zona igual a 0, se indica el fin.
'''
# Coloque la resolución del Ejercicio 4 debajo de esta línea

seguir = True
totalMunicipio = 0
totalVaronesMenores = 0
surVaronesMenores = 0
norteVaronesMenores = 0
esteVaronesMenores = 0
oesteVaronesMenores = 0

while seguir:
    zona=str.upper(input("Escriba la zona del usuario: norte, sur, este u oeste. \nEscriba 0 para salir: "))
    
    if zona == "0":
        seguir = False
        break

    sexo=str.upper(input("Indique el sexo del usuario. F para mujer o M para hombre: "))
    edad=int(input("Escriba la edad del usuario: "))
    
    if edad < 15 and sexo == "M":
        totalVaronesMenores += 1
        if zona == "NORTE":
            norteVaronesMenores += 1
        elif zona == "SUR":
            surVaronesMenores += 1
        elif zona == "ESTE":
            esteVaronesMenores += 1
        elif zona == "OESTE":
            oesteVaronesMenores += 1
    
    totalMunicipio += 1

if totalVaronesMenores > 0:
    print("porcentaje de varones menores de 15 años para todo el municipio: ", (totalVaronesMenores*100)/totalMunicipio)

    try:
        print("porcentaje de varones menores de 15 años para cada zona: ")
        print("Zona norte: ", (norteVaronesMenores*100)/totalMunicipio)
        print("Zona sur: ", (surVaronesMenores*100)/totalMunicipio)
        print("Zona este: ", (esteVaronesMenores*100)/totalMunicipio)
        print("Zona oeste: ", (oesteVaronesMenores*100)/totalMunicipio)
    except ZeroDivisionError:
        print("No hay estadísticas para las demás zonas")