from random import randint
respuesta = "s"
puntajejugador = 0
puntajecomputadora = 0
while respuesta == "s":
    print("*" * 55)
    print("            piedra , papel o tijera")
    print("*" * 55)
    jugador = input("escribir tu jugada: piedra, papel o tijera: ")

    eleccion = ["piedra", "papel", "tijera"]
    computadora = eleccion[randint(0, 2)]
    print("la computadora elige: ", computadora)

    if computadora == jugador:
        print("hay un empate")
    elif computadora == "piedra" and jugador == "tijera":
        print("la computadora gana. la piedra le gana a tijera")
        puntajecomputadora += 1
    elif computadora == "tijera" and jugador == "papel":
        print("la computadora gana. la tijera le gana a papel")
        puntajecomputadora += 1
    elif computadora == "papel" and jugador == "piedra":
        print("la computadora gana. papel le gana a piedra")
        puntajecomputadora += 1
    elif jugador == "piedra" and computadora == "tijera":
        print("el jugador gana. la piedra le gana a pierdra")
        puntajejugador += 1
    elif jugador == "tijera" and computadora == "papel":
        print("el jugador gana. la tijera le gana a papel")
        puntajejugador += 1
    elif jugador == "papel" and computadora == "piedra":
        print("el jugador gana, papel le gana a piedra")
        puntajejugador += 1
    print("el puntaje del jugador es: ", puntajejugador)
    print("el puntaje de la computadora es: ", puntajecomputadora)
    respuesta = input("desea seguir jugando: si(s) - no(n)")