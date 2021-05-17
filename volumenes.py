from math import pi


PI = 3.1415926535

print("""Hola, con este programa podrás calcular el volumen de un cilindro. 
Por favor, ingresa los datos que se te piden (en centímetros)""")

radio = float(input('¿Cuál es el radio de la figura?: '))
altura = float(input ('¿Cuál es la altura de la figura?: '))

radio_cuadrado = radio ** 2
area_base = (PI * radio_cuadrado)
volumen = area_base * altura
volumen = round(volumen, 2)
print('El volumen de tu cilindro es: ' + str(volumen) + ' centímetros cúbicos')