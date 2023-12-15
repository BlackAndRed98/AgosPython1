
# Conceptos


nombre = "Agostina"
edad = 25

numero = 10
decimal = 3.14
texto = "Hola Mundo "
verdadero = True

suma = 5 + 3
resta = 10 - 2
multiplicacion = 4 * 6
division = 15 / 3
igualdad = (5 + 3) == (10 - 2)

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Bucles WHILE
contador = 0
agostina = int(input("Edad agostina : "))
while agostina > 18:
    agostina -= 1
    print(agostina)

# Bucles FOR
for contador in range(0, 20):
    contador += 1
    print(contador)
