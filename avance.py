#   Se importa para obtener función de números aleatorios y matemáticas
import random
import math

#   VARIABLES
puntaje = 0
print("Puntaje: ", puntaje)

contador = 0
correctas = 0


#   LISTAS
preguntas = []

#   MATRICES
matriz = []
i = 0


#   BIENVENIDA
print("Bienvenido a tu programa ideal para practicar lo que quieras:) \n ¿Qué quieres practicar hoy? \n")
opcion = int(input("1. Triángulos \n2. Cuadrados \n3. Pentágonos \n4. Hexágonos \n5. Círculos \n6. Salir \n"))


#   FUNCIONES 

#       Verifica si la respuesta es CORRECTA o INCORRECTA
def verificar(respuesta, valor):
    acum = 0

    if (respuesta == valor):
        print("¡Felicidades! Tu respuesta es correcta:D")
        acum = acum +  100
        preguntas.append("Correcta")    

    if (respuesta != valor):
        print("¡Lo siento! Tu respuesta es incorrecta:(")
        acum = acum - 50
        preguntas.append("Incorrecta")

    return acum

#       Muestra al usuario las preguntas a responder
def infoRespuesta():
    print("¿Cuál es el perímetro de la figura con lado", lado, "?")
    print("¿Y cuál es su área?")

#       Muestra al usuario qué RESPONDIÓ a una pregunta y si la tuvo CORECTA o INCORRECTA
def consultar(num, matriz):
    resp = num - 1
    resp2 = resp//2
    resp3 = resp2 - 1
    
    print("La pregunta número ", num, " fue: ", preguntas[resp])
    print("Tu respuesta fue: ", matriz[resp2][resp3])
    print("¡Hasta pronto!")

#       Pregunta qué pregunta quiere CONSULTAR (saber la respuesta)
def preguntar(consult):
    if (consult == 1):
        num = int(input("¿Cuál pregunta quieres consultar? "))
        consultar(num, matriz)
    else:
        print("¡Hasta pronto! :)")

#       Agrega la respuesta a la MATRIZ de RESPUESTAS
def respuestas(i, matriz, respuestaP, respuestaA): 
        matriz.append([])
        matriz[i].append(respuestaP)
        matriz[i].append(respuestaA)

        return matriz

#   OPCIONES

#       1 = Triángulos
if (opcion == 1):
    rep = int(input("¿Estás liste para empezar? \n1. Sí \n2. No \n"))

    while (rep == 1):     
        contador = contador + 2

        base = random.randint(10, 20)
        altura = random.randint(15,25)
        print("¿Cuál es el área del triángulo con base", base, "y altura", altura, "?")

        lado2 = random.randint(10, 15)
        lado3 = random.randint(10, 15)
        print("¿Cuál es el perímetro del triángulo con lados", lado2, "y", lado3, "?")

        area = (base*altura)/2
        perimetro = base + lado2 + lado3

        respuestaA = float(input("Respuesta área: "))
        respuestaP = int(input("Respuesta perímetro: "))

        matriz = respuestas(i, matriz, respuestaP, respuestaA)
        i += 1

        verificar(respuestaP, perimetro)
        verificar(respuestaA, area)

        puntaje = puntaje + verificar(respuestaA, area) + verificar(respuestaP, perimetro)
        if (respuestaP == perimetro):
            correctas = correctas + 1
        if (respuestaA == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)

        rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))

    print("Tu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

    consult = int(input("¿Quieres consultar alguna pregunta? \n1. Sí \n2. No \n"))
    preguntar(consult)

#       2 = Cuadrados
elif (opcion == 2):
    rep = int(input("¿Estás liste para empezar? \n1. Sí \n2. No \n"))

    while (rep == 1):
        contador = contador + 2

        lado = random.randint(10, 20)
        infoRespuesta()

        respuestaP = int(input("Respuesta perímetro: "))
        respuestaA = int(input("Respuesta área: "))

        perimetro = lado*4
        area = lado*lado

        matriz = respuestas(i, matriz, respuestaP, respuestaA)
        i += 1

        verificar(respuestaP, perimetro)
        verificar(respuestaA, area)

        puntaje = puntaje + verificar(respuestaA, area) + verificar(respuestaP, perimetro)
        if (respuestaP == perimetro):
            correctas = correctas + 1
        if (respuestaA == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)

        rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))

    print("Tu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

    consult = int(input("¿Quieres consultar alguna pregunta? \n1. Sí \n2. No \n"))
    preguntar(consult)

#       3 = Pentágonos
elif (opcion == 3):
    rep = int(input("¿Estás liste para empezar? \n1. Sí \n2. No \n"))

    while (rep == 1):
        contador = contador + 2

        lado = random.randint(10, 20)
    
        infoRespuesta()

        perimetro = lado*5
        area = (perimetro*lado)/2
        respuestaP = int(input("Respuesta perímetro: "))
        respuestaA = int(input("Respuesta área: "))

        matriz = respuestas(i, matriz, respuestaP, respuestaA)
        i += 1

        verificar(respuestaP, perimetro)
        verificar(respuestaA, area)

        puntaje = puntaje + verificar(respuestaA, area) + verificar(respuestaP, perimetro)
        if (respuestaP == perimetro):
            correctas = correctas + 1
        if (respuestaA == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)

        rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))

    print("Tu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

    consult = int(input("¿Quieres consultar alguna pregunta? \n1. Sí \n2. No \n"))
    preguntar(consult)

#       4 = Hexágonos
elif (opcion == 4):
    rep = int(input("¿Estás liste para empezar? \n1. Sí \n2. No \n"))

    while (rep == 1):
        contador = contador + 2

        lado = random.randint(10, 20)
    
        infoRespuesta()

        perimetro = lado*6
        area = (perimetro*lado)/2
        respuestaP = int(input("Respuesta perímetro: "))
        respuestaA = int(input("Respuesta área: "))

        matriz = respuestas(i, matriz, respuestaP, respuestaA)
        i += 1

        verificar(respuestaP, perimetro)
        verificar(respuestaA, area)

        puntaje = puntaje + verificar(respuestaA, area) + verificar(respuestaP, perimetro)
        if (respuestaP == perimetro):
            correctas = correctas + 1   
        if (respuestaA == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)
        
        rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))
    
    print("Tu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

    consult = int(input("¿Quieres consultar alguna pregunta? \n1. Sí \n2. No \n"))
    preguntar(consult)


#       5 = Círculos
elif (opcion == 5):
    rep = int(input("¿Estás liste para empezar? \n1. Sí \n2. No \n"))

    while (rep == 1):
        contador = contador + 2

        radio = random.randint(10, 20)

        print("¿Cuál es el perímetro y área de un círculo con radio de ", radio, "?")

        perimetro = 2*3.1416*radio
        area = 3.1416*radio*radio
        respuestaP = int(input("Respuesta perímetro: "))
        respuestaA = int(input("Respuesta área: "))

        matriz = respuestas(i, matriz, respuestaP, respuestaA)
        i += 1

        verificar(respuestaP, perimetro)
        verificar(respuestaA, area)

        puntaje = puntaje + verificar(respuestaA, area) + verificar(respuestaP, perimetro)
        if (respuestaP == perimetro):
            correctas = correctas + 1
        if (respuestaA == area):
            correctas = correctas + 1

        print("Puntaje: ", puntaje)

        rep = int(input("¿Quieres seguir practicando? \n1. Sí \n2. No \n"))

    print("Tu puntaje final es: ", puntaje)
    print("Realizaste ", contador, "ejercicios, de los cuales ", correctas, " fueron correctos")

    consult = int(input("¿Quieres consultar alguna pregunta? \n1. Sí \n2. No \n"))
    preguntar(consult)

#       6 = Salir
elif (opcion == 6):
    print("¡Hasta pronto! :D")

#       Cualquier otro número (NO VÁLIDO)
else:
    print("Opción no válida")