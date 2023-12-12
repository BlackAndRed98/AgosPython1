

my_string_variable = "my string variable "
# print(my_string_variable)


my_bool_variable = False
# print(my_bool_variable)


#
# Ejercicio 1
# Joel Garcia Cascalló
# 2023
#

# Instrucciones de salida
print('Primera frase.')  # Hay un salto de línea al final de cada frase
print('Segunda frase.')
print('Tercera frase.')

# Escribe un programa llamado Exercici1.py que haga una cuenta atrás de 10 hasta 0, con un número por línea,
# y al final diga DESPEGUE!

print(10)
print(9)
print(8)
print(7)
print(6)
print(5)
print(4)
print(3)
print(2)
print(1)
print(0)
print("Despegue!")


#
# Ejercicio 2
# Joel Garcia Cascalló
# 2023
#

# Instrucciones de salida
# Podemos evitar el salto de línea y los espacios
# print('Primera frase.', end='')
# print('Segunda frase.', end='')
# print('Tercera frase.', end='')

# Escribe un programa llamado Exercici2.py que muestre por pantalla diferentes colores separados por comas, usando una
# instrucción por color, pero que todos se vean a la misma línea.

print("Blanco", end=",")
print("negro", end=",")
print("morado", end=",")
print("gris")

#
# Exercici3
# Joel Garcia Cascalló
# 2023
#

# Instrucciones de salida
print("Lista de la compra:")  # Podemos añadir un salto de línea
print('\t* Pan.')  # Podemos añadir una tabulación
print('\t* Tomates.')

# Escribe un programa llamado Exercici3.py que muestre la lista de los ingredientes de tu receta de cocina preferida,
# usando el formato que hay al ejemplo (salto de línea y tabulaciones).

print("Lista de mi receta: \n\t* Fideos \n\t* Manteca ")

#
# Ejercicio 4
# Joel Garcia Cascalló
# 2023
#

# Instrucciones de salida y variables

# El primer uso de una variable siempre es la ASIGNACIÓN (A python no hay que declarar la variable por separado, porque asume
# el tipo de datos según el valor asignado)
# El nombre de la variable (identificador) se escoge libremente respetando ciertas normas:
# - No puede tener espacios
# - Tiene que empezar por una letra
# - No puede ser una palabra reservada
nomAlumne = 'Joan'

# Después de asignar un valor a una variable, se puede consultar cuál es este valor, por ejemplo mostrándolo con una
# instrucción de salida

print('Hola')
# Podemos mostrar el contenido de una variable
print(nomAlumne)

# En una misma instrucción se pueden mostrar literales y contenidos de variables. Así, se añade un espacio.
print('Adiós ', nomAlumne)
print(f'Adios {nomAlumne}')

# Así, NO se añade ningún espacio.
print('Adiós ', end='')
print(nomAlumne)

# Si la variable es una cadena de caracteres (string) se puede concatenar con el operador +. Así, NO se añade ningún espacio
print('Adiós ' + nomAlumne)

# Otra manera de hacerlo con la función formado(). Permite un mejor control de espacios.
# print('Adiós {}!'. formato(nomAlumne))

# También se pueden modificar los valores de las variables
nomAlumne = 'Marta'
print('Hola nueva alumna ', nomAlumne)

# Escribe un programa Exercici4.py que te salude por tu nombre, y después te agradezca haber venido usando tu nombre
# a la frase. Finalmente, también se tiene que despedir usando tu nombre. Tienes que hacer que sea fácil modificar el nombre
# (con una sola modificación), usando una variable.


Nombrevariable = "Franco"
print(f"Bienvenido {Nombrevariable} \nLe doy la bienvenida {Nombrevariable} \nMe despido un saludo {Nombrevariable} ")


# nom = input("Introdueix el teu nom: ")


# salutacions = f"Hola {nom}, benvigunt al ejercici 4."
# print(salutacions)


# gracies = f"Gràcies per estar aquí {nom}. "
# print(gracies)

# comiat = f"Adeu! Que tinguis un bon dia {nom}. "
# print(comiat)


#
# Ejercicio 5
# Joel Garcia Cascalló
# 2023
#

# Variables y tipos de datos
# Si el valor asignado a la variable es un número entero SIN comillas simples, esta asume que la variable es un
# NÚMERO, y por tanto permite efectuar operaciones numéricas.
variable_numerica = 10
print('variable_numerica: ', variable_numerica)

# print('variable_numerica concatenada: ' + variable_numerica)
# ERROR, no se puede concatenar con + porque la variable no es una cadena (string)!

print('variable_numerica modificada con operaciones matemáticas:',
      variable_numerica + 1)
# Si la variable es de un tipo numérico, se pueden efectuar operaciones matemáticas con ella

print('variable_numerica de tipo', type(variable_numerica))
# La función type() nos muestra el tipo de datos de una variable que le pasamos por paréntesis.

# Si el valor asignado es un número CON comillas (o cualquier frase con comillas), se asume que la variable es de tipo
# cadena o string en inglés, y por tanto permite efectuar operaciones propias de los strings.
# Las comillas pueden ser simples o dobles, pero tienen que ser las mismas cuando vallas y cuando obras.
# Si dentro de una cadena de caracteres delimitada con un tipo de comillas introduces el otro, python la considerará
# un carácter.
variable_cadena = '10'
print('variable_cadena:', variable_cadena)

# Se puede concatenar si la variable es de tipo string
print('variable_cadena concatenada: ' + variable_cadena)

# print('variable_cadena modificada con operaciones matemáticas:', variable_cadena + 1)
# ERROR, no se pueden efectuar operaciones matemáticas con strings
print('variableCadena de tipos', type(variable_cadena))

# Si el valor asignado es un número decimal, python asume que la variable es de tipo FLOAT (número con coma flotante)
# Los números decimales a python se escriben con PUNTO, como podéis ver.
variable_decimal = 10.55
print('variable_decimal:', variable_decimal)
print('variable_decimal de tipo', type(variable_decimal))

# Si el valor asignado es True o False (verdadero o falso) SIN comillas, se asume el tipo booleano.
# Este tipo es el que se evalúa a las CONDICIONES
variable_booleana = True
print('variable_booleana:', variable_booleana)
print('variable_booleana de tipo', type(variable_booleana))

# Escribe un programa llamado Exercici5.py que haga el siguiente:
# - Tienes que usar variables para tu refresco preferido y para su precio.
# - A partir de estas variables tienes que calcular la mitad de este precio, y hacer que se imprima por pantalla
# que se ha visto este refresco a un súpermercat a aquel precio, especificando tanto el nombre del refresco como el precio.

refresco = "cocacola"
precio = 5
mitad = precio / 2
print(
    f"El precio de tu {refresco} esta {precio} , hemos visto en el super que esta a {mitad}  ")
