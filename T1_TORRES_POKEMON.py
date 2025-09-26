import random

# ===================== CLASES =====================

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.vida_max = random.randint(150, 400)
        self.vida_actual = self.vida_max

    def recuperar(self):
        # Vuelve a tener su vida máxima
        self.vida_actual = self.vida_max


# ===================== FUNCIONES =====================

def crearEntrenadorPokemon(num):
    if num == 1:
        print("\n=== CREACIÓN DE TU ENTRENADOR Y POKÉMON ===")
    else:
        print("\n=== CREACIÓN DEL ENTRENADOR RIVAL Y SU POKÉMON ===")
    
    nombre_entrenador = input("Ingrese el nombre del entrenador: ")
    nombre_pokemon = input("Ingrese el nombre del Pokémon: ")

    entrenador = Entrenador(nombre_entrenador)
    pokemon = Pokemon(nombre_pokemon)

    print(f"\nEntrenador: {entrenador.nombre}")
    print(f"Pokémon: {pokemon.nombre}")
    print(f"Ataque máximo: {pokemon.max_ataque}")
    print(f"Vida máxima: {pokemon.vida_max}")
    print(f"Vida actual: {pokemon.vida_actual}")

    return entrenador, pokemon


def valorDeAtaque(num, pokemon1, pokemon2):
    if num == 1:
        atacante = pokemon1
    else:
        atacante = pokemon2
    
    ataque = random.randint(0, atacante.max_ataque)
    return ataque


def defender(num, ataque, pokemon1, pokemon2):
    if num == 1:
        defensor = pokemon1
    else:
        defensor = pokemon2

    # Lanzamos un dado entre 1 y 6
    dado = random.randint(1, 6)
    if dado == 6:
        ataque = 0  # el ataque se anula

    defensor.vida_actual -= ataque
    return defensor.vida_actual


# ===================== PROGRAMA PRINCIPAL =====================

def main():
    # Crear al primer entrenador y pokemon (usuario)
    entrenador1, pokemon1 = crearEntrenadorPokemon(1)

    victorias = 0
    derrotas = 0

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        opcion = input("¿Desea Pelear (P) o Finalizar (F)? ").upper()

        if opcion == "F":
            # Finalizar el juego
            print("\n=== RESUMEN FINAL ===")
            print(f"Entrenador: {entrenador1.nombre}")
            print(f"Pokémon: {pokemon1.nombre}")
            print(f"Ataque máximo: {pokemon1.max_ataque}")
            print(f"Vida máxima: {pokemon1.vida_max}")
            print(f"Encuentros ganados: {victorias}")
            print(f"Encuentros perdidos: {derrotas}")
            break

        elif opcion == "P":
            # Recuperamos vida antes de iniciar la pelea
            pokemon1.recuperar()

            # Crear rival
            entrenador2, pokemon2 = crearEntrenadorPokemon(2)

            # Pelea
            print("\n=== COMIENZA LA PELEA ===")
            turno = 1  # Empieza el jugador
            while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
                if turno == 1:
                    ataque = valorDeAtaque(1, pokemon1, pokemon2)
                    vida_restante = defender(2, ataque, pokemon1, pokemon2)
                    print(f"\n{pokemon1.nombre} ataca con {ataque} de daño.")
                    print(f"{pokemon2.nombre} ahora tiene {vida_restante} de vida.")
                    turno = 2
                else:
                    ataque = valorDeAtaque(2, pokemon1, pokemon2)
                    vida_restante = defender(1, ataque, pokemon1, pokemon2)
                    print(f"\n{pokemon2.nombre} ataca con {ataque} de daño.")
                    print(f"{pokemon1.nombre} ahora tiene {vida_restante} de vida.")
                    turno = 1

            # Resultado
            if pokemon1.vida_actual > 0:
                print(f"\nGanador: {entrenador1.nombre} con {pokemon1.nombre}")
                victorias += 1
            else:
                print(f"\nGanador: {entrenador2.nombre} con {pokemon2.nombre}")
                derrotas += 1

        else:
            print("Opción inválida. Intente de nuevo.")


# ===================== EJECUCIÓN =====================
main()
