# EJERCICIO 1:
# Mayor o Menor De Edad?
edad=input("Ingrese la edad de la persona: ")
try:
    edad=int(edad)
    if 0 <= edad < 18:
        print("Es menor de edad.")
    elif 18 <= edad < 110:
        print("Es mayor de edad.")
except ValueError:
    print("Edad incorrecta. Debe ser un número entero")


# EJERCICIO 2:
# Intentos fallidos para ingresar a cuenta.
passServer= "abc123"
baneo=False

for i in range(5):
    passUser=str(input("Ingrese su contraseña: "))
    if passServer==passUser:
        print("Contraseña correcta. Bienvenido!")
        break
    else:
        print("Contraseña falsa. Utilizaste ", i+1, " de 5 intentos")
        if i >=4:
            print("Cuenta bloqueada. Comuniquese con el administrador del sistema.")
            baneo=True

# EJERCICIO 3:
# Calculador de Resultado final de cuestionario.
try:
    totPreguntas=int(input("Ingrese la cantidad de preguntas que tiene el cuestionario: "))
    totCorrectas=int(input("Ingrese la cantidad de respuestas correctas: "))

    porcentCorrecto = (totCorrectas*100)/totPreguntas
    #print(porcentCorrecto)

    if porcentCorrecto >= 90:
        print("resultado EXCELENTE!")
    elif 70 <= porcentCorrecto < 90:
        print("resultado Bueno")
    elif 60 <= porcentCorrecto < 70:
        print("resultado Aprobado")
    elif porcentCorrecto < 60:
        print("resultado No alcanzó")
except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")

# EJERCICIO 4:
# Día con mayores Ventas.
try:
    ventas1=int(input("Ingrese las ventas del día 1: "))
    ventas2=int(input("Ingrese las ventas del día 2: "))

    if ventas1 > ventas2:
        print("Se vendió más el día 1")
    elif ventas1 < ventas2:
        print("Se vendió más el día 2")
    elif ventas1 == ventas2:
        print("Se vendió lo mismo ambos días")
except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")

# EJERCICIO 5:
# Pizza Vegetariana.

ingPizza= ("Mozzarella", "Tomate")
ingVeg= ("Pimentos", "Rúcula")
ingNoVeg= ("Jamón", "Panceta")

try:
    pizzaElegida = int(input("Presione 1: pizza vegetariana o presione 2: pizza No vegetariana "))
   
    if pizzaElegida == 1:
        print("Los ingredientes de la pizza son: " + str(ingPizza))

        ingElegido= int(input("Presione 1 para agregar " + str(ingVeg[0]) + " o presione 2 para agregar " + str(ingVeg[1])))
       
        if ingElegido == 1:
            print("Los ingredientes de su pizza son: " + str(ingPizza) + " con agregado de: " + str(ingVeg[0]))
        elif ingElegido == 2:
            print("Los ingredientes de su pizza son: " + str(ingPizza) + " con agregado de: " + str(ingVeg[1]))
        else:
            pass
   
    elif pizzaElegida == 2:
        print("Los ingredientes de la pizza son: " + str(ingPizza))
  
        ingElegido= int(input("Presione 1 para agregar " + str(ingNoVeg[0]) + " o presione 2 para agregar " + str(ingNoVeg[1])))
  
        if ingElegido == 1:
            print("Los ingredientes de su pizza son: " + str(ingPizza) + " con agregado de: " + str(ingNoVeg[0]))
        elif ingElegido == 2:
            print("Los ingredientes de su pizza son: " + str(ingPizza) + " con agregado de: " + str(ingNoVeg[1]))
        else:
            pass
    else:
        pass

except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")

# EJERCICIO 6:
# Grupos Por Nombre y Turno.
try:
    nombre=str.lower(input("Ingrese su nombre: "))
    turno=str.lower(input("Escriba 'Tarde' o 'Noche' según su turno: "))

    if (nombre < "m" and turno == "tarde") or (nombre > "n" and turno == "noche"):
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")
except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")


# Hasta acá fueron los ejercicios del video "Introducción a Estructuras de Control".

# EJERCICIO 7:
# Años de insecticida.

try:
    agnosInsecticida=int(input("¿Hace cuántos años utiliza DDT como insecticida? "))    
except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")
    exit()

if 0 < agnosInsecticida <= 10:
    print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación.")
elif agnosInsecticida > 10:
    print("Por favor solicite revisión de suelos en su plantación.")
else:
    pass

# EJERCICIO 8:
# Contaminación del agua.

from tkinter import *
from tkinter import messagebox as MessageBox

try:
    tamagno=int(input("""Indique el número que corresponde al tamaño del pescado estudiado:
    1: Tamaño Normal
    2: Tamaño por debajo de lo Normal
    3: Tamaño un poco por encima de lo Normal
    4: Tamaño sobredimensionado
    """))
except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")
    exit()

if tamagno==1:
    MessageBox.showwarning("Tamaño Normal","Pez en buenas condiciones")
elif tamagno==2:
    MessageBox.showwarning("Tamaño por debajo de lo Normal","Pez con problemas de nutrición")
elif tamagno==3:
    MessageBox.showwarning("Tamaño un poco por encima de lo Normal","Pez con síntomas de organismo contaminado")
elif tamagno==4:
    MessageBox.showwarning("Tamaño sobredimensionado", "Pez contaminado")
else:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")
    exit()

# EJERCICIO 9:
# Uso de fertilizantes por hectárea.

try:
    compuestoHectarea=int(input("Cuántos metros cuadrados de compuesto en el suelo existen por hectárea? "))
    vegMatorral=str.lower(input("Existe vegetción matorral en la hectárea? ¿SI o NO? "))
except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")
    exit()

if compuestoHectarea < 1000 or (vegMatorral == "si" or vegMatorral == "sí"):
    print("No es factible la utilización de fertilizantes.")
else:
    if 10000 > compuestoHectarea >= 1000 and vegMatorral == "no":
        print("Puede utilizar fertilizantes en esa hectárea.")
    else:
        print("Ha ocurrido un error. Ingrese los datos nuevamente.")
        exit()

# EJERCICIO 10:
# Selector de recetas ecológicas.

ingComunes= ("Verdura", "Berenjena")
ingReceta1= ("Lenteja", "Apio")
ingReceta2= ("Morrón", "Cebolla")
mostrar = "Su receta lleva: "

try:
    recetaElegida = int(input("Presione 1 para elegir receta de Lentejas y Apio \
                                presione 2 para elegir receta de Morrón y Cebolla"))
   
    if recetaElegida == 1:
        seleccion=ingComunes+ingReceta1
        
        for i in range(3):
            ingredientes=(int(input("Seleccione 3 ingredientes: \
                1 para elegir " + seleccion[0] + " \
                2 para elegir " + seleccion[1] + " \
                3 para elegir " + seleccion[2] + " \
                4 para elegir " + seleccion[3])))
            if ingredientes == 1:
                mostrar = mostrar + str(seleccion[0]) + " "
            elif ingredientes == 2:
                mostrar = mostrar + str(seleccion[1]) + " "
            elif ingredientes == 3:
                mostrar = mostrar + str(seleccion[2]) + " "
            elif ingredientes == 4:
                mostrar = mostrar + str(seleccion[3]) + " "
            else:
                pass

    if recetaElegida == 2:
        seleccion=ingComunes+ingReceta2
        for i in range(3):
            ingredientes=(int(input("Seleccione 3 ingredientes: \
                1 para elegir " + seleccion[0] + " \
                2 para elegir " + seleccion[1] + " \
                3 para elegir " + seleccion[2] + " \
                4 para elegir " + seleccion[3])))
            if ingredientes == 1:
                mostrar = mostrar + str(seleccion[0]) + " "
            elif ingredientes == 2:
                mostrar = mostrar + str(seleccion[1]) + " "
            elif ingredientes == 3:
                mostrar = mostrar + str(seleccion[2]) + " "
            elif ingredientes == 4:
                mostrar = mostrar + str(seleccion[3]) + " "
            else:
                pass

    print("Seleccionó la receta " + str(recetaElegida) + ". " + str(mostrar))

except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")

# EJERCICIO 11:
# Recolección de residuos urbanos.

try:
    barrio=str.lower(input("Ingrese el nombre del barrio: "))
    centro=str.lower(input("¿El tipo de barrio es Céntrico? Escriba SI o NO"))
except ValueError:
    print("Ha ocurrido un error. Ingrese los datos nuevamente.")
    exit()

if (barrio < "m" and (centro == "si" or centro == "sí")) or (barrio > "n" and centro == "no"):
    print("Pertenece a la sección A")
else:
    print("Pertenece a la sección B")

# Hasta acá fueron los ejercicios de Nivel 1: Desafíos Condicionales en "Introducción a Estructuras de Control".

# EJERCICIO 12:
# 