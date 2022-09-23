#Se importa para obtener función de números aleatorios
import random

#VARIABLES
puntaje = 0
print("Puntaje: ", puntaje)

contador = 0
correctas = 0

print("Bienvenido a tu programa ideal para practicar lo que quieras:) \n ¿Qué quieres practicar hoy? \n")
opcion = int(input("1. Triángulos \n2. Cuadrados \n3. Pentágonos \n4. Hexágonos \n5. Salir \n"))

#FUNCIONES 

#Verificar si es correcto o incorrecto
def verificar(respuesta, valor):
    acum = 0

    if (respuesta == valor):
        print("¡Felicidades! Tu respuesta es correcta:D")
        acum = acum +  100

    else:
        print("¡Lo siento! Tu respuesta es incorrecta:(")
        acum = acum - 50

    return acum

def infoRespuesta():
    print("¿Cuál es el perímetro de la figura con lado", lado, "?")
    print("¿Y cuál es su área?")

#OPCIONES

#Triángulos
if (opcion == 1):
    rep = int(input("¿Estás liste para empezar o quieres seguir practicando? \n1. Sí \n2. No \n"))

    while (rep == 1):     
        contador = contador + 1

        base = random.randint(10, 20)
        altura = random.randint(15,25)
        print("¿Cuál es el área del triángulo con base", base, "y altura", altura, "?")

        area = (base*altura)/2
        respuesta = float(input("Respuesta: "))

        puntaje = puntaje + verificar(respuesta, area)
        if (respuesta == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)

        rep = int(input("¿Estás liste para empezar o quieres seguir practicando? \n1. Sí \n2. No \n"))

    print("Vuelve pronto:) \nTu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

#Cuadrados
elif (opcion == 2):
    rep = int(input("¿Estás liste para empezar o quieres seguir practicando? \n1. Sí \n2. No \n"))

    while (rep == 1):
        contador = contador + 2

        lado = random.randint(10, 20)
        infoRespuesta()

        respuestaP = int(input("Respuesta perímetro: "))
        respuestaA = int(input("Respuesta área: "))
        perimetro = lado*4
        area = lado*lado

        verificar(respuestaP, perimetro)
        verificar(respuestaA, area)

        puntaje = puntaje + verificar(respuestaA, area) + verificar(respuestaP, perimetro)
        if (respuestaP == perimetro):
            correctas = correctas + 1
        if (respuestaA == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)

        rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))

    print("Vuelve pronto:) \nTu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

#Pentágonos
elif (opcion == 3):
    rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))

    while (rep == 1):
        contador = contador + 2

        lado = random.randint(10, 20)
    
        infoRespuesta()

        perimetro = lado*5
        area = (perimetro*lado)/2
        respuestaP = int(input("Respuesta perímetro: "))
        respuestaA = int(input("Respuesta área: "))

        verificar(respuestaP, perimetro)
        verificar(respuestaA, area)

        puntaje = puntaje + verificar(respuestaA, area) + verificar(respuestaP, perimetro)
        if (respuestaP == perimetro):
            correctas = correctas + 1
        if (respuestaA == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)

        rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))

    print("Vuelve pronto:) \nTu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

#Hexágonos
elif (opcion == 4):
    rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))

    while (rep == 1):
        contador = contador + 2

        lado = random.randint(10, 20)
    
        infoRespuesta()

        perimetro = lado*6
        area = (perimetro*lado)/2
        respuestaP = int(input("Respuesta perímetro: "))
        respuestaA = int(input("Respuesta área: "))

        verificar(respuestaP, perimetro)
        verificar(respuestaA, area)

        puntaje = puntaje + verificar(respuestaA, area) + verificar(respuestaP, perimetro)
        if (respuestaP == perimetro):
            correctas = correctas + 1   
        if (respuestaA == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)
        
        rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))
    
    print("Vuelve pronto:) \nTu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

#Salir
elif (opcion == 5):
    print("¡Hasta pronto! :D")

#Cualquier otro número
else:
    print("Opción no válida")
