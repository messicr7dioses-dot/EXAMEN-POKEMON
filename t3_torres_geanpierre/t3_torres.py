TAMAÑO_N = 9
ENERGIA_MAXIMA = 18
START_X, START_Y = 0, 8
FIN_X, FIN_Y = 8, 0

LABERINTO = [
    [ 1,  1,  1,  1, 99,  1,  1,  1,  1], # Fila 0
    [ 1, 99, 99,  1, 99,  1, 99,  1, 99], # Fila 1
    [ 1,  1, 99,  1,  1,  1, 99,  1, 99], # Fila 2
    [99,  1, 99,  1, 99, 99, 99,  1, 99], # Fila 3
    [ 1,  1, 99, -1,  1,  1,  1,  3, 99], # Fila 4
    [-2, 99, 99,  1, 99, 99, 99,  1,  1], # Fila 5
    [ 1, 99,  1, -1,  1,  1,  1,  1, 99], # Fila 6
    [ 1, 99, 99, 99, 99,  2, 99,  1, 99], # Fila 7
    [ 0,  1,  3,  1,  1,  1, 99,  1,  1]  # Fila 8
]

def imprimir_laberinto(matriz):
    print("Leyenda: [ I ] = Inicio, [ F ] = Fin, [███] = Muro")
    for i in range(TAMAÑO_N):
        for j in range(TAMAÑO_N):
            val = matriz[i][j]
            if i == START_X and j == START_Y:
                print(f"[ I({val})]", end="")
            elif i == FIN_X and j == FIN_Y:
                print(f"[ F({val})]", end="")
            elif val == 99:
                print("[ ███ ]", end="")
            else:
                print(f"[{val:4}]", end="")
        print()

def imprimir_solucion(solucion, laberinto):
    print("Leyenda: [ * ] = Camino, [ . ] = No es camino, [███] = Muro")
    for i in range(TAMAÑO_N):
        for j in range(TAMAÑO_N):
            if i == START_X and j == START_Y:
                print("[ I ]", end="")
            elif i == FIN_X and j == FIN_Y:
                print("[ F ]", end="")
            elif laberinto[i][j] == 99:
                print("[███]", end="")
            elif solucion[i][j] == 1:
                print("[ * ]", end="")
            else:
                print("[ . ]", end="")
        print()

def resolver_laberinto_util(lab, x, y, energia_gastada, sol):
    
    if (x < 0 or x >= TAMAÑO_N or 
        y < 0 or y >= TAMAÑO_N or 
        lab[x][y] == 99 or 
        sol[x][y] == 1):
        return False

    if energia_gastada > ENERGIA_MAXIMA:
        return False

    sol[x][y] = 1

    if x == FIN_X and y == FIN_Y:
        return True

    movimientos = [(0, -1), (1, 0), (-1, 0), (0, 1)]

    for dx, dy in movimientos:
        new_x, new_y = x + dx, y + dy
        
        costo_siguiente_celda = 0
        
        if 0 <= new_x < TAMAÑO_N and 0 <= new_y < TAMAÑO_N:
            
            if new_x == FIN_X and new_y == FIN_Y:
                costo_siguiente_celda = 0
            else:
                costo_siguiente_celda = lab[new_x][new_y]

        nueva_energia_gastada = energia_gastada + costo_siguiente_celda

        if resolver_laberinto_util(lab, new_x, new_y, nueva_energia_gastada, sol):
            return True

    sol[x][y] = 0
    return False

def iniciar_solucion():
    
    print("--- RESOLVEDOR DE LABERINTO CON BACKTRACKING ---")
    print("\nLaberinto Original:")
    
    imprimir_laberinto(LABERINTO)
    
    solucion = [[0 for _ in range(TAMAÑO_N)] for _ in range(TAMAÑO_N)]
    
    energia_inicial = LABERINTO[START_X][START_Y]
    
    if resolver_laberinto_util(LABERINTO, START_X, START_Y, energia_inicial, solucion):
        print("\n-------------------------------------------------")
        print("✅ ¡ÉXITO! Se encontró un camino a la salida.")
        print(f"   El camino no gasta más de {ENERGIA_MAXIMA} unidades de energía.")
        print("-------------------------------------------------")
        print("\nMatriz de Solución (Camino marcado con *):")
        imprimir_solucion(solucion, LABERINTO)
    else:
        print("\n-------------------------------------------------")
        print("❌ PERDISTE GAME OVER No se encontró un camino válido")
        print(f"   que cumpla la restricción de {ENERGIA_MAXIMA} unidades de energía.")
        print("-------------------------------------------------")
        print("\nMatriz (muestra el último intento fallido):")
        imprimir_solucion(solucion, LABERINTO)

if __name__ == "__main__":
    iniciar_solucion()
