#Se importa para obtener función de números aleatorios
import random

print("Bienvenido a tu programa ideal para practicar lo que quieras:) \n ¿Qué quieres practicar hoy? \n")
opcion = int(input("1. Triángulos \n2. Cuadrados \n3. Pentágonos \n4. Hexágonos \n5. Heptágonos \n6. Octágonos \n7. Eneágono \n8. Salir \n"))


#FUNCIONES 
#VARIABLES


#Respuesta correcta
def correcto(respuesta, valor):
    if (respuesta == valor):
        print("¡Felicidades! Tu respuesta es correcta:D")
        puntaje == puntaje +  100
        print("Tu puntaje actual es: ", puntaje)

#Respuesta incorrecta
def incorrecto(respuesta, valor):
    if (respuesta != valor):
        print("¡Lo siento! Tu respuesta es incorrecta:(")

        if (puntaje <= 0):
            #puntaje = 0
            print("Tu puntaje actual es: ", puntaje)
        else:
           #puntaje = puntaje + 50
            print("Tu puntaje actual es: ", puntaje)

#Verificar si es correcto o incorrecto
def verificar(respuesta, valor):
    correcto(respuesta, valor)  
    incorrecto(respuesta, valor)


#OPCIONES

#Triángulos

puntaje = 0
print("Puntaje: ", puntaje)

if (opcion == 1):
    base = random.randint(10, 20)
    altura = random.randint(15,25)
    print("¿Cuál es el área del triángulo con base", base, "y altura", altura, "?")

    area = (base*altura)/2
    respuesta = float(input("Respuesta: "))

    verificar(respuesta, area)


#Cuadrados
elif (opcion == 2):
    lado = random.randint(10, 20)
    print("¿Cuál es el perímetro del cuadrado con lado", lado, "?")
    print("¿Y cuál es su área?")

    perimetro = lado*4
    area = lado*lado
    respuestaP = int(input("Respuesta perímetro: "))
    respuestaA = int(input("Respuesta área: "))

    verificar(respuestaP, perimetro)
    verificar(respuestaA, area)
