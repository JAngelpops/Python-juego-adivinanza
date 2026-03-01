import random


def adivinanza_numero():
    # Generar un numero del 1-100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Instrucciones cdel juego
    print("Bienvenido al juego de adivinanza de numero!")
    print("!debes adivinar un numero que se encuentra entre el 1 y el 100¡")
    print("!Buena suerte¡")

    # Bucle del juego
    while not adivinado:
        # solicitar que se introduzca un numero del 1 al 100
        adivinanza = input("Introduce tu adivinanza: ")
        intentos += 1

        # validar que la entrada sea un numero entero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)

            # Validar que el numero ingresado este entre el 1 y el 100
            if adivinanza > numero_secreto:
                print(
                    f"El numero ingresado: {adivinanza} es mayor que el numero secreto."
                )
            elif adivinanza < numero_secreto:
                print(
                    f"El numero ingresado: {adivinanza} es menor que el numero secreto."
                )
            else:
                adivinado = True
                print(
                    f"¡Felicidades! Has adivinado el numero secreto: {numero_secreto} en {intentos} intentos."
                )
        else:
            print(
                "¡Entrada no valida! Por favor, introduce un numero entero entre el 1 y el 100."
            )


adivinanza_numero()
