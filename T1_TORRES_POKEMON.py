# ===========================
# EXAMEN POKEMON - TORRES GEAN PIERRE
# ===========================

import random

# ---------------------------
# Clase Entrenador
# ---------------------------
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre


# ---------------------------
# Clase Pokemon
# ---------------------------
class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.vida_max = random.randint(150, 400)
        self.vida_actual = self.vida_max

    def recuperar(self):
        self.vida_actual = self.vida_max

    def __str__(self):
        return f"{self.nombre} | Ataque Máx: {self.max_ataque} | Vida: {self.vida_actual}/{self.vida_max}"


# ---------------------------
# Variables globales
# ---------------------------
entrenador1 = None
pokemon1 = None
entrenador2 = None
pokemon2 = None
ganadas = 0
perdidas = 0


# ---------------------------
# Funciones
# ---------------------------
def crearEntrenadorPokemon(n):
    global entrenador1, pokemon1, entrenador2, pokemon2

    if n == 1:
        nombre_entrenador = input("Ingrese su nombre de Entrenador: ")
        nombre_pokemon = input("Ingrese el nombre de su Pokemon: ")
        entrenador1 = Entrenador(nombre_entrenador)
        pokemon1 = Pokemon(nombre_pokemon)
        print("\nSu Pokémon ha sido creado:")
        print(pokemon1)

    elif n == 2:
        nombre_entrenador = input("Ingrese el nombre del Entrenador rival: ")
        nombre_pokemon = input("Ingrese el nombre del Pokemon rival: ")
        entrenador2 = Entrenador(nombre_entrenador)
        pokemon2 = Pokemon(nombre_pokemon)
        print("\nEl Pokémon rival ha sido creado:")
        print(pokemon2)


def valorDeAtaque(n):
    if n == 1:
        return random.randint(0, pokemon1.max_ataque)
    else:
        return random.randint(0, pokemon2.max_ataque)


def defender(n, ataque):
    dado = random.randint(1, 6)
    if dado == 6:
        ataque = 0  # esquiva total

    if n == 1:
        pokemon1.vida_actual -= ataque
        return pokemon1.vida_actual
    else:
        pokemon2.vida_actual -= ataque
        return pokemon2.vida_actual


# ---------------------------
# Algoritmos extra
# ---------------------------
# Fuerza bruta: encontrar Pokémon con mayor vida actual
def pokemon_con_mas_vida():
    if pokemon1.vida_actual >= pokemon2.vida_actual:
        return pokemon1
    else:
        return pokemon2

# Ordenamiento: burbuja de los ataques de un turno
def ordenar_daños(lista_daños):
    n = len(lista_daños)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_daños[j] > lista_daños[j + 1]:
                lista_daños[j], lista_daños[j + 1] = lista_daños[j + 1], lista_daños[j]
    return lista_daños


# ---------------------------
# Programa principal
# ---------------------------
if __name__ == "__main__":
    crearEntrenadorPokemon(1)  # siempre inicia jugador con su Pokémon

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("P - Pelear")
        print("F - Finalizar juego")
        opcion = input("Elija una opción: ").upper()

        if opcion == "F":
            print("\n=== FIN DEL JUEGO ===")
            print(f"Entrenador: {entrenador1.nombre}")
            print(f"Pokemon final: {pokemon1}")
            print(f"Encuentros ganados: {ganadas}")
            print(f"Encuentros perdidos: {perdidas}")
            break

        elif opcion == "P":
            # Se crea el rival
            crearEntrenadorPokemon(2)

            # Recuperar vida antes de cada pelea
            pokemon1.recuperar()
            pokemon2.recuperar()

            print("\n--- INICIO DE LA PELEA ---")
            daños_turno = []  # lista para aplicar ordenamiento

            turno = 1
            while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
                print(f"\n--- Turno {turno} ---")

                # Ataca jugador
                ataque1 = valorDeAtaque(1)
                vida_rival = defender(2, ataque1)
                daños_turno.append(ataque1)
                print(f"{pokemon1.nombre} ataca con {ataque1}. Vida de {pokemon2.nombre}: {vida_rival}")

                if vida_rival <= 0:
                    print(f"\n¡{entrenador1.nombre} gana con {pokemon1.nombre}!")
                    ganadas += 1
                    break

                # Ataca rival
                ataque2 = valorDeAtaque(2)
                vida_jugador = defender(1, ataque2)
                daños_turno.append(ataque2)
                print(f"{pokemon2.nombre} ataca con {ataque2}. Vida de {pokemon1.nombre}: {vida_jugador}")

                if vida_jugador <= 0:
                    print(f"\n¡{entrenador2.nombre} gana con {pokemon2.nombre}!")
                    perdidas += 1
                    break

                turno += 1

            # Mostrar ordenamiento de daños del combate
            print("\n--- ORDEN DE DAÑOS (menor a mayor con Bubble Sort) ---")
            print(ordenar_daños(daños_turno))

            # Mostrar Pokémon con más vida (fuerza bruta)
            print(f"\nEl Pokémon con más vida al final es: {pokemon_con_mas_vida().nombre}")

        else:
            print("Opción inválida, intente de nuevo.")
