import random

# Mostrar mensaje de bienvenida

def mostrar_bienvenida():
    print("¡Bienvenido al juego de GATO!")

# Mostrar menú y obtener opción del usuario

def mostrar_menu():
    print("...Menú...:")
    print("1. jugar solo (jugador 1 VS bot)")
    print("2. jugar dos jugadores (j1 VS j2)")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Inicializar el tablero de juego

def inicializar_tablero():
    return [' ' for _ in range(9)]

# Mostrar el tablero

def mostrar_tablero(tablero):
    print(f"""
     {tablero[0]} | {tablero[1]} | {tablero[2]}
    -----------
     {tablero[3]} | {tablero[4]} | {tablero[5]}
    -----------
     {tablero[6]} | {tablero[7]} | {tablero[8]}
    """)

# Realizar un movimiento

def realizar_movimiento(tablero, posicion, jugador):
    if tablero[posicion] == ' ':
        tablero[posicion] = jugador
        return True
    return False

# Verificar si hay un ganador

def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6)              # Diagonales
    ]
    for comb in combinaciones_ganadoras:
        if all(tablero[i] == jugador for i in comb):
            return True
    return False

# Verificar si hay un empate

def verificar_empate(tablero):
    return all(espacio != ' ' for espacio in tablero)

# Obtener movimiento de la computadora

def movimiento_computadora(tablero):
    posiciones_libres = [i for i in range(9) if tablero[i] == ' ']
    return random.choice(posiciones_libres)

# Jugar una partida

def jugar_partida(jugadores):
    tablero = inicializar_tablero()
    turno = 0
    while True:
        mostrar_tablero(tablero)
        jugador_actual = jugadores[turno % 2]
        if jugador_actual == 'bot':
            posicion = movimiento_computadora(tablero)
        else:
            posicion = int(input(f"Turno de {jugador_actual}, ingrese posición (0-8): "))
        if realizar_movimiento(tablero, posicion, jugador_actual):
            if verificar_ganador(tablero, jugador_actual):
                mostrar_tablero(tablero)
                print(f"¡{jugador_actual} ha ganado!")
                break
            elif verificar_empate(tablero):
                mostrar_tablero(tablero)
                print("¡Es un empate!")
                break
            turno += 1
        else:
            print("Posición no válida, intente de nuevo.")

# Función principal
def main():
    mostrar_bienvenida()
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            jugar_partida(['j1', 'bot'])
        elif opcion == '2':
            jugar_partida(['j1', 'j2'])
        elif opcion == '3':
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

# Ejecutar el juego
if __name__ == "__main__":
    main()
